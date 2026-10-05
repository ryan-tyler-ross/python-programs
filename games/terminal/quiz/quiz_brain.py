"""Keep the current question number and score together."""


class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.total_score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {question.text} (True/False): ").strip().lower()
        while answer not in ("true", "false"):
            answer = input("Please enter True or False: ").strip().lower()
        self.check_answer(answer, question.answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.total_score += 1
            print("You got it right!")
        else:
            print(f"That's wrong! The correct answer was {correct_answer}.")
        print(f"Score: {self.total_score}/{self.question_number}\n")
