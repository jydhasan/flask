from flask import Flask, render_template, request

app = Flask(__name__)

# Define the quiz questions and answers
questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['Paris', 'London', 'Rome', 'Madrid'],
        'answer': 'Paris'
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['Mars', 'Venus', 'Jupiter', 'Saturn'],
        'answer': 'Mars'
    },
    {
        'question': 'What is the chemical symbol for gold?',
        'options': ['Au', 'Ag', 'Fe', 'Hg'],
        'answer': 'Au'
    }
]

# Store the user's score
score = 0
# Define a custom Jinja2 filter for getting the length of a list


@app.template_filter('length')
def length_filter(lst):
    return len(lst)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global score

    if request.method == 'POST':
        # Get the selected answer from the form
        selected_option = request.form['option']
        # Get the current question index
        question_index = int(request.form['question_index'])

        # Check if the selected answer is correct
        if selected_option == questions[question_index]['answer']:
            score += 1

        # Move to the next question
        if question_index < len(questions) - 1:
            next_question_index = question_index + 1
            return render_template('quiz.html', question=questions[next_question_index], question_index=next_question_index)
        else:
            return render_template('result.html', score=score)

    # Display the first question
    return render_template('quiz.html', question=questions[0], question_index=0)


if __name__ == '__main__':
    app.run(debug=True)
