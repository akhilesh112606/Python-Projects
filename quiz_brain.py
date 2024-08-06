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
