import os
import openai
import gradio as gr
from google.cloud import translate_v2 as translate

# key (& location)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/mruchus/translate.json"

def rephrase_text(text):
    response = openai.Completion.create(
        engine="text-davinci-003",  # model
        prompt=f"{text}\n\n Rewrite the sentence in the style of a news article:",
        temperature=0.5, # randomness (lower == more deterministic)
        max_tokens=120 # 100 tokens ~= 75 words
    )

    # note: 'response.choices' contains model outputs, typically one unless specified otherwise
    return response.choices[0].text.strip()

def translate_text(text, target='en'):
    translate_client = translate.Client()

    result = translate_client.translate(
        text, target_language=target)

    # print(f'Text: {result["input"]}')
    # print(f'Translation: {result["translatedText"]}')
    # print(f'Detected source language: {result["detectedSourceLanguage"]}')

    return result["translatedText"]

def to_fancy(text):
    english_text = translate_text(text)
    print(english_text)
    fancy_english = rephrase_text(english_text)

    return fancy_english

def to_gradio():
    demo = gr.Interface(fn=to_fancy, inputs="text", outputs="text")
    demo.launch(share=True)

to_gradio()




