class QuizBrain:
    def __init__(self, question_bank):
        self.question_list = question_bank
        self.question_number: int = 0
        self.score = 0

    def still_has_questions(self)->bool:
        return self.question_number < len(self.question_list)

    def next_question(self)->None:
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False?): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer)->None:
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f'You got it right!')
        else: print(f'That\'s wrong.')
        print(f'The correct answer was {correct_answer}\nYour current score is {self.score}/{self.question_number}\n\n')