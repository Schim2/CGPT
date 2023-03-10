import streamlit as st
from streamlit_chat import message
import openai
import os

openai.api_key = os.getenv("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")

def openai_create(prompt):
    response = openai.Completion.create(
        model="chatbot-v1",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.1,
        presence_penalty=0.1,
        stop=[" Human:", " TextWizardAI:"]
    )

    return response.choices[0].text

def chatgpt_clone(input_, history=None):
    history = history or []
    history.append(input_)
    inp = ' '.join(history)
    output = openai_create(inp)
    return output

st.set_page_config(
    page_title="TextWizardAI Chatbot",
    page_icon=":robot:"
)

st.header("TextWizardAI Chatbot")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text

user_input = get_text()

if user_input:
    output = chatgpt_clone(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
