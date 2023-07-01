import os
import gradio as gr
from google.cloud import translate_v2 as translate

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/mruchus/translate.json"

def translate_text(text, target='en'):
    translate_client = translate.Client()

    result = translate_client.translate(
        text, target_language=target)

    # print(f'Text: {result["input"]}')
    # print(f'Translation: {result["translatedText"]}')
    # print(f'Detected source language: {result["detectedSourceLanguage"]}')

    return result["translatedText"]

def to_gradio():
    demo = gr.Interface(fn=translate_text, inputs="text", outputs="text")
    demo.launch(share=True)

to_gradio()




