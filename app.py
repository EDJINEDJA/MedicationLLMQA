import gradio as gr
from src.gradio import greet

if __name__ == "__main__":
    demo = gr.Interface(fn=greet, inputs="text", outputs="text")

    demo.launch(share=True) 

    
   