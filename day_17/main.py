from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    new_question = Question(data["text"], data["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

still_has_questions = quiz.still_has_questions()
while still_has_questions:
    quiz.next_question()