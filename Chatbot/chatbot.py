from transformers import pipeline

qna = pipeline("question-answering")

answer = qna(
    question="What is the capital of France?",
    context="The capital of France is Paris."
)

import gradio as gr

def answer_question(question, context):
    result = qna(question=question, context=context)
    return result['answer'] 

demo = gr.Interface(
    fn=answer_question,
    inputs=["text", "text"],
    outputs="text",
    title="Question Answering"
)
demo.launch(share=True)
