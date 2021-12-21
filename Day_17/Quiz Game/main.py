from question_model import CreateQuestion
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for dic in question_data:
    question_text = dic["question"]
    question_answer = dic["correct_answer"]
    new_question = CreateQuestion(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank) # This is a quiz object

while quiz.still_questions():
    quiz.next_question() # This calls the next_question method on the quiz object

print("You've completed the quiz.")
print(f"Your final score is {quiz.score}/{len(question_bank)}")

# for question in question_bank:
#     print(question.text)
#     print(question.answer)


