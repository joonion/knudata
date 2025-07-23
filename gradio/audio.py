import gradio as gr
import numpy as np

def reverse_audio(audio):
    sr, data = audio
    reverse_audio = (sr, np.flipud(data))
    return reverse_audio


mic = gr.Audio(
    sources="microphone", type="numpy", 
    label="Speak here"        
)

demo = gr.Interface(fn=reverse_audio, inputs=mic, outputs="audio")
demo.launch()