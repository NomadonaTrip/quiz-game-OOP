from question_model import Question
from data import question_data


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):

        current_question = self.question_list[self.question_number]
        self.question_number += 1
        current_answer = input(f"Q.{self.question_number}. {current_question.text} (True/ False) ")
        correct_answer = current_question.answer
        is_correct = self.check_answer(current_answer, current_question.answer, self.score)
        if is_correct:
            print("You got it right!")
            self.score += 1
        else:
            print("Sorry, that was the wrong answer")
        print(f"The right answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def check_answer(self, current_answer, correct_answer, score):

        if current_answer.lower() == correct_answer.lower():
            return True
        else:
            return False

    def end_quiz(self):
        print("You have completed the quiz")
        print(f"Your final score is {self.score}/{self.question_number}")




