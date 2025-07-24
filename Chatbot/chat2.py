from transformers import pipeline
import gradio as gr

# QA 파이프라인 로딩
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def predict(message, history):
    # history를 하나의 문맥(context)로 통합
    context = ""
    for turn in history:
        if turn["role"] == "user":
            context += f"User: {turn['content']}\n"
        elif turn["role"] == "assistant":
            context += f"Assistant: {turn['content']}\n"

    # context가 없으면 오류 방지용 기본 문맥
    if context.strip() == "":
        context = "This is the beginning of a conversation between a user and an assistant."
        
    # QA pipeline에 입력
    result = qa_pipeline(question=message, context=context)
    answer = result["answer"]

    # history 갱신
    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": answer})
    return answer

demo = gr.ChatInterface(predict, type="messages")
demo.launch()
