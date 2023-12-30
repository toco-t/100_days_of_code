from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def main():
    question_bank = [
        Question(data["text"], data["answer"]) for data in question_data
    ]

    quiz = QuizBrain(question_bank)
    while quiz.has_next_question():
        quiz.next_question()

    print(f"Well done! Your final score is:\t"
          f"{quiz.score}/{quiz.question_number}")


if __name__ == "__main__":
    main()
