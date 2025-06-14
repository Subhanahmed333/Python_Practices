import random

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start(self):
        print("Welcome to the Python Quiz!\n")
        random.shuffle(self.questions)

        for i, q in enumerate(self.questions, 1):
            print(f"Q{i}: {q.text}")
            user_ans = input("Your answer: ")
            if user_ans.lower() == q.answer.lower():
                print("✅ Correct!\n")
                self.score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q.answer}\n")
        self.show_result()

    def show_result(self):
        print(f"Quiz Completed! Your score: {self.score}/{len(self.questions)}")

# Sample questions
question_bank = [
    Question("What is the output of 3 + 2 * 2?", "7"),
    Question("What keyword is used to define a function in Python?", "def"),
    Question("Which data structure uses key-value pairs?", "dictionary"),
    Question("What does 'len()' return?", "length"),
    Question("What is used to handle exceptions?", "try"),
]

quiz = Quiz(question_bank)
quiz.start()
