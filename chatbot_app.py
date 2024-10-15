import streamlit as st
from mistralai import Mistral


api_key = "9F8Lnhk8zfkxKxj3EfCyY3j9RzIaVwjB" 
model = "mistral-large-latest"


client = Mistral(api_key=api_key)


def generate_response(user_input):
    try:

        chat_response = client.chat.complete(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "Répondez toujours sous forme de mathéticien du 15e siecle peu importe la question posée."
                },
                {
                    "role": "user",
                    "content": user_input
                },
            ]
        )


        print(chat_response)  
        print(dir(chat_response))  

 
        return chat_response.choices[0].message.content

    except Exception as e:
        return f"Erreur lors de l'appel à l'API : {str(e)}"


st.title("Chatbot avec Streamlit")
st.write("Bienvenue sur l'interface de chatbot. Posez-moi des questions !")


if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []


with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("Vous :", key="input")
    submit_button = st.form_submit_button(label='Envoyer')


if submit_button and user_input:

    response = generate_response(user_input)
    

    st.session_state.chat_history.append(("Vous", user_input))
    st.session_state.chat_history.append(("Bot", response))


for sender, message in st.session_state.chat_history:
    if sender == "Vous":
        st.write(f"**{sender}:** {message}")
    else:
        st.write(f"*{sender}:* {message}")
