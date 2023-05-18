from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_ques = Question(question_text, question_answer)
    question_bank.append(new_ques)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.play_game()
    print()
print("Out of question")