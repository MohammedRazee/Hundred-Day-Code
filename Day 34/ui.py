from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(
            150, 
            125, 
            width=280,
            text="Dat text", 
            fill=THEME_COLOR, 
            font=("Arial", 20, "italic")
        )

        true_image = PhotoImage(file="./images/true.png")
        false_image = PhotoImage(file="./images/false.png")
        self.true = Button(image=true_image, highlightthickness=0, command=lambda: self.user_choice("True"))
        self.false = Button(image=false_image, highlightthickness=0, command=lambda: self.user_choice("False"))

        self.score = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")

        self.score.grid(row=0,column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.true.grid(row=2, column=0)
        self.false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz")
            self.score.config(text=f"Final Score: {self.quiz.score} / {len(self.quiz.question_list)}")
            self.true.config(state="disabled")
            self.false.config(state="disabled")


    def user_choice(self, answer: str):
        if self.quiz.check_answer(user_answer=answer):
            self.feedback(True)
        else:
            self.feedback(False)
    
    def feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
            self.score.config(text=f"Score: {self.quiz.score}")
            self.window.after(1000, self.get_next_question)

        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)
