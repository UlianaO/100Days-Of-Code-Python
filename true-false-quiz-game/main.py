# The exercise is done to practice syntax and OOP

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# Creating a list of objects from a list of dictionaries.
for q in question_data:
    question_text = q["text"]
    question_answer = q["answer"]
    # Converting to the object
    new_question_object = Question(question_text, question_answer)
    question_bank.append(new_question_object)

# Initializing a quiz out of the list of objects.
quiz = QuizBrain(question_bank)

while not quiz.is_empty():
    quiz.next_question()

print(f"/nYou have completed the quiz with {quiz.score}/{quiz.question_number} score.")