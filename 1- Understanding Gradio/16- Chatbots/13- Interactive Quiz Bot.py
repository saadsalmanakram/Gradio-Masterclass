import gradio as gr

def quiz_bot(message, history):
    questions = ["What is the capital of France?", "What is 2 + 2?"]
    answers = ["Paris", "4"]
    
    if not history:
        return questions[0]
    elif len(history) % 2 == 1:
        question_index = len(history) // 2
        if message == answers[question_index]:
            if question_index + 1 < len(questions):
                return questions[question_index + 1]
            else:
                return "Congratulations! You've completed the quiz."
        else:
            return "Try again."
    else:
        return "Please provide an answer to the question."

gr.ChatInterface(quiz_bot).launch()
