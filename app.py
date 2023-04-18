import gradio as gr
from src.gradio import app

if __name__ == "__main__":
    demo = gr.Interface(fn=app, inputs="text", outputs="text")

    demo.launch(share=True) 

    
   