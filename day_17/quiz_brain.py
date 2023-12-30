from question_model import Question


class QuizBrain:
    """
    Keep track of a quiz game.
    """

    def __init__(self, question_list: list[Question]):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        """
        Ask users the question at the current question number and increment the
        score if the correct answer is given.
        """
        next_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}:\t"
                       f"{next_question.text} (True/False):\t")

        if answer.lower() == next_question.answer.lower():
            self.score += 1
            print(f"BRILLIANT!")

        print(f"The correct answer was:\t{next_question.answer}\n"
              f"Your current score is:\t{self.score}/{self.question_number}\n")

    def has_next_question(self) -> bool:
        """
        Return True if there's still a question in a list, else False.

        :return: True if there's still a question, else False
        """
        return self.question_number < len(self.question_list)
