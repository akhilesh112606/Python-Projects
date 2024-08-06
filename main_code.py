from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    temp_question = Question(data['text'], data['answer'])
    question_bank.append(temp_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You have completed the QUIZ\nYour Final Score : {quiz.score}")