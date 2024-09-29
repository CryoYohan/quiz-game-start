from question_model import Question
from data import question_data
from quiz_brain import *

question_bank = []
for i in range(0, len(question_data)):
    text, answer = question_data[i]['question'], question_data[i]['correct_answer']
    question = Question(text,answer)
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.next_question()
print(f'You\'ve completed the quiz!\nYour final score was: {quiz_brain.score}/{len(question_data)}')