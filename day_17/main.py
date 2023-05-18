import random
from day_17.data import question_data
class Question:
    def __init__(self, text, answer, total):
        self.text = text
        self.answer = answer
        total = 0
    def check(self, total):
        self.total += 1
number = random.randrange(0,len(question_data))
ask = question_data[number]['text']
answer = question_data[number]['answer']
print(ask)
reply = input('True or False ').title()
question = Question(ask, answer)
if reply == question.answer:

    print('1')
else:
    print('0')
# print(question.answer)

