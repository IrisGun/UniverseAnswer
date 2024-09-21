from flask import Flask, jsonify, render_template
import pandas as pd
import random

app = Flask(__name__)

def load_answers():
    try:
        df = pd.read_excel('data/answers.xlsx')
        print(df)  # Debug: Check if DataFrame is loaded correctly
        if 'answers' not in df.columns:
            raise ValueError("Column 'answer' not found in the Excel file.")
        return df['answers'].tolist()
    except Exception as e:
        print(f"Error loading answers: {e}")  # Debug: Log the error
        raise


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/answer_page')
def answer_page():
    return render_template('answer_page.html')



@app.route('/random_answer')
def random_answer():
    answers = load_answers()
    random_answer = random.choice(answers)
    return jsonify(answer=random_answer)

if __name__ == '__main__':
    app.run()



