import time

class Question:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display_question(self):
        print(self.question)
        for i, choice in enumerate(self.choices):
            print(f"{i + 1}. {choice}")

    def check_answer(self, user_choice):
        return self.choices[user_choice - 1] == self.answer

def run_quiz(questions):
    score = 0
    for question in questions:
        print("\n" + "=" * 50)
        question.display_question()
        print("=" * 50)
        user_choice = int(input("Enter your answer (1-4): "))
        if question.check_answer(user_choice):
            score += 1
            print("\nCorrect answer!")
        else:
            print("\nIncorrect answer!")

        # Pause for a moment before displaying the next question
        time.sleep(2)

    print("\n" + "=" * 50)
    print("Quiz completed! Your score is:", score, "/", len(questions))
    print("=" * 50)

# Define your questions here
question_1 = Question("What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"], "Paris")
question_2 = Question("Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], "Mars")
question_3 = Question("Who painted the Mona Lisa?", ["Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", "Michelangelo"], "Leonardo da Vinci")

# Create a list of your questions
quiz_questions = [question_1, question_2, question_3]

# Run the quiz
run_quiz(quiz_questions)
