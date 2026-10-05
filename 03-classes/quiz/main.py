"""Build a question bank and ask each question once."""

import html
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data["results"]:
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)
print("Let's play TRUE or FALSE! Get as many points as you can...\n\n")

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz\n")
print(f"- - - FINAL SCORE: {quiz_brain.total_score}/{len(quiz_brain.question_list)} - - -\n")
