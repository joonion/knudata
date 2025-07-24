import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Chat 기반 모델 호출 예
resp = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role":"system","content":"You are a scholarly assistant."},
        {"role":"user","content":"공룡이 나오는 영화 추천해줘."}
    ]
)
print(resp.choices[0].message.content)
