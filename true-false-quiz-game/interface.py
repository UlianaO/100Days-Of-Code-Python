from tkinter import *
from quiz_brain import QuizBrain
BG_COLOR = "#FFF8D6"
CARD_THEME = "#375362"
QUESTION_FONT = ("Ariel", 18, "italic")
CORRECT_BG = "#98D8AA"
WRONG_BG = "#FEA1A1"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("CS QUIZ")
        self.window.config(padx=10, pady=15, bg=BG_COLOR)

        # Labels
        self.score_lbl = Label(text="Score:", fg=CARD_THEME, bg=BG_COLOR, font=QUESTION_FONT)
        self.score_lbl.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg=CARD_THEME)
        self.questions = self.canvas.create_text(150, 125,
                                                 text="Text",
                                                 fill="white",
                                                 font=QUESTION_FONT,
                                                 width=260)
        self.canvas.grid(row=1, column=0, columnspan=3, pady=50)

        # Buttons
        true_img = PhotoImage(file="imgs/true.png")
        self.true_btn = Button(image=true_img, command=self.true_click)
        self.true_btn.grid(row=2, column=0)

        false_img = PhotoImage(file="imgs/false.png")
        self.false_btn = Button(image=false_img, command=self.false_click)
        self.false_btn.grid(row=2, column=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=CARD_THEME)
        if self.quiz.still_has_questions():
            self.score_lbl.config(text=f"Score: {self.quiz.score} ")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.questions, text=q_text)
        # No more questions
        else:
            self.canvas.itemconfig(self.questions, text="You`ve reached the end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_click(self):
        is_correct = self.quiz.is_user_correct("True")
        self.answer(is_correct)

    def false_click(self):
        is_correct = self.quiz.is_user_correct("False")
        self.answer(is_correct)

    def answer(self, is_right):
        if is_right:
            self.canvas.config(bg=CORRECT_BG)
        else:
            self.canvas.config(bg=WRONG_BG)
        self.window.after(1000, self.get_next_question)
