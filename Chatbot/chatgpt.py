
import gradio as gr


import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# OpenAI Chat 호출 함수
def chat_with_openai(message, history):
    # Gradio의 history 포맷 → OpenAI 포맷으로 변환
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    for user_msg, ai_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": ai_msg})
    messages.append({"role": "user", "content": message})

    # Chat 기반 모델 호출 예
    resp = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role":"system","content":"You are a scholarly assistant."},
            {"role":"user","content":"공룡이 나오는 영화 추천해줘."}
        ]
    )
    reply = resp.choices[0].message.content

    history.append((message, reply))
    return history, history

# Gradio UI 구성
with gr.Blocks() as demo:
    gr.Markdown("## 💬 ChatGPT with OpenAI API")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Enter your message")
    clear = gr.Button("Clear")

    state = gr.State([])

    msg.submit(chat_with_openai, [msg, state], [chatbot, state])
    clear.click(lambda: ([], []), inputs=[], outputs=[chatbot, state])

# 앱 실행
if __name__ == "__main__":
    demo.launch()
