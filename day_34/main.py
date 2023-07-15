from question_model import Question
# from data import question_data
import html
from quiz_brain import QuizBrain
import requests

question_bank = []
parameter = {
    "amount": 10,
    "type": "boolean"
}
question = requests.get("https://opentdb.com/api.php", params=parameter)
question_data = question.json()["results"]
for question in question_data:
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
