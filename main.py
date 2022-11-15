from question_model import QuestionModel
from data import question_data

question_bank = []
for new_q in question_data:
    new_q_text = new_q["text"]
    new_q_answer = new_q["answer"]
    question = QuestionModel(new_q_text, new_q_answer)
    question_bank.append(question)

print(question_bank[0].answer)
