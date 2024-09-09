import gradio as gr

def trivia_quiz(message, history):
    questions = {
        "What is the capital of France?": "Paris",
        "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
        "What is the largest planet in our solar system?": "Jupiter"
    }
    question, answer = message.split(";")
    question = question.strip()
    answer = answer.strip()
    
    correct_answer = questions.get(question)
    if correct_answer:
        if correct_answer.lower() == answer.lower():
            return "Correct!"
        else:
            return f"Wrong! The correct answer is {correct_answer}."
    else:
        return "Question not found."

gr.ChatInterface(trivia_quiz).launch()
