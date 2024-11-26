from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    questiontext = question["question"]
    questionanswer = question["correct_answer"]

    new_question = Question(questiontext, questionanswer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
else:
    quiz.end_quiz()





