import html
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.current_question = None
        self.score = 0

    def next_question(self):
        self.current_question = self.question_list[self.question_number]  # goes through q`s one by one
        self.question_number += 1
        return f"Q.{self.question_number}: {html.unescape(self.current_question.text)}"

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def is_user_correct(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score +=1
            return True
        else:
            return False

    def is_empty(self):
        # if len(self.question_list) < self.question_number:
        #     return False
        # else:
        #     return True
        # same as:
        return len(self.question_list) <= self.question_number
