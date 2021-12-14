from question_model import CreateQuestion
from data import question_data

question_bank = []
for dic in question_data:
    question_text = dic["text"]
    question_answer = dic["answer"]
    new_question = CreateQuestion(question_text, question_answer)
    question_bank.append(new_question)




