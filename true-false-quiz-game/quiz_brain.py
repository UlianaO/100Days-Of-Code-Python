class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]  # goes through q`s one by one
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        if self.is_user_correct(user_answer, current_question.answer):
            self.score += 1
            print(f"Correct. Your score is {self.score}")
        else:
            print(f"Wrong. The right answer is {current_question.answer}. Your score is still {self.score}")

    def is_user_correct(self, user_answer, correct_answer):
        return user_answer.lower() == correct_answer.lower()

    def is_empty(self):
        # if len(self.question_list) < self.question_number:
        #     return False
        # else:
        #     return True
        # same as:
        return len(self.question_list) <= self.question_number
