class Question:
    def __init__(self, question_text, question_answer):
        self.text = question_text
        self.answer = question_answer

question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.list = question_list
        self.score = 0

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            return True
        else:
            return False

    def still_has_questions(self):
        if self.question_number<len(self.list):
            return True
        else:
            return False
    def next_question(self):
        question = self.list[self.question_number].text
        self.question_number+=1
        decision = input(f"Q.{self.question_number} : {question}? True or False - ")
        if self.check_answer(decision, self.list[self.question_number-1].answer):
            print("Your Answer is Correct")
            self.score+=1
        else:
            print("Your Answer is Wrong")
        print(f"Your current score is {self.score}/{self.question_number}")


question_bank = []
for data in question_data:
    temp_question = Question(data['text'], data['answer'])
    question_bank.append(temp_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You have completed the QUIZ\nYour Final Score : {quiz.score}")