class Question:
    """
    Model a question and its answer.
    """

    def __init__(self, text: str, answer: str):
        self.text = text
        self.answer = answer
