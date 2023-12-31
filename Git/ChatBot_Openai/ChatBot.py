import openai
import gradio as gr

openai.api_key = "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"

messages = [{'role': 'system', 'content': 'You are a helpful & kind AI Assistance'}]

def MyOwnChatBot(input):
    if input:
        messages.append({'role': 'user', 'content': input})

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )

    reply = chat.choices[0].message['content']
    messages.append({'role': 'assistant', 'content': reply})

    return reply

inputs = gr.components.Textbox(lines=7, label="Own ChatBot AI")
outputs = gr.components.Textbox(label="Reply from AI")

gr.Interface(fn=MyOwnChatBot, inputs=inputs, outputs=outputs,
             title="My Own ChatBot", description="Ask anything you want",
             theme='default').launch(share=True)
