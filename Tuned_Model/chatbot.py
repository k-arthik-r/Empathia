import streamlit as st
from db import get_user_queries, update_user_queries, clear_chats
import random
import time
from configparser import ConfigParser
import google.generativeai as genai

config = ConfigParser()
config.read("config.ini")

previous_convo = " "
r, g, b = (random.randint(0, 256) for _ in range(3))

def clean_response(response):
    try:
        if response.startswith("Response:"):
            response = response[len("Response:"):].strip()
        return response
    except Exception as e:
        st.toast("Something Went Wrong!! - Error CLX")


def response_generator(user_query):
    try:
        prompt = f"""Default:
            You are a highly trained therapist serving as a mental health and therapy assistant. Your role is to provide support, guidance, and conversation tailored to the user's well-being. Engage with the user in open-ended conversations or address specific questions related to their mental health concerns. Consider Previous Conversations while Answering.

            Instructions:
            - Respond with supportive and empathetic messages.
            - Offer guidance, reflections, and coping strategies.
            - Ensure confidentiality and privacy in all interactions.
            - Avoid providing emergency assistance; direct users to seek immediate help from qualified professionals in crises.

            Examples:

            User: I've been feeling very anxious lately and don't know what to do.
            Response: I'm sorry to hear that you're feeling this way. Anxiety can be overwhelming, but there are strategies that can help. Have you tried any relaxation techniques or mindfulness exercises? Sometimes, talking about what's on your mind can also provide some relief. I'm here to listen.

            User: I find it hard to stay motivated and often feel very down. What should I do?
            Response: It's tough when motivation is low and you're feeling down. It might help to set small, achievable goals for yourself and celebrate each accomplishment, no matter how small. Also, consider reaching out to friends or family for support. Remember, you're not alone, and it's okay to ask for help.

            Previous Conversations:
            {previous_convo}

            User: {user_query}
            Response: 
        """
    except Exception as e:
        st.toast("Something Went Wrong!! - Error PTX")

    generation_config = {
      "temperature": 0.4,
      "top_p": 0.95,
      "top_k": 64,
      "max_output_tokens": 4096,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    try:
        model = genai.GenerativeModel(
            model_name="tunedModels/mentalconvo-2vunn8rexq5u",
            generation_config=generation_config,
            safety_settings=safety_settings,
        )

        responseraw = model.generate_content([prompt])
        response = responseraw.text

        for word in response.split():
            yield word + " "
            time.sleep(0.05)
    except Exception as e:
        st.toast("Something Went Wrong!! - Error GENX")


def update_db(username, question, answer):
    try:
        user_queries = get_user_queries(username) or {}
        sanitized_question = question.replace(".", "__dot__")
        user_queries[sanitized_question] = answer
        update_user_queries(username, user_queries)
    except Exception as e:
        st.toast("Something Went Wrong!! - Error UPDB")

def chatbot_interface():
    try:
        initial = (st.session_state.name[0]).upper()
    except Exception as e:
        st.toast("Name Error!! - Error INP")

    global r, g, b    

    try:
        html_content = f"""
            <div id="sidebar-content">
                <div id="initial" style="
                    width: 55px;
                    height: 55px;
                    background-color: rgb({r}, {g}, {b});
                    border-radius: 50%;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    color: white;
                    font-size: 20px;
                    font-weight: bold;
                    user-select: none;">
                    {initial}
                </div>
                <div id="info">
                    <h2>{st.session_state.name}</h2>
                    <h5>{st.session_state.username}</h5>
                </div>
            </div>
        """
    except Exception as e:
        st.toast("Something Went Wrong!! - Error NNF")

    st.sidebar.markdown(html_content, unsafe_allow_html=True)


    st.markdown(
        """
        <style>
        #sidebar-content {
            display: flex;
            flex-direction:row;
            justify-content: center;
            align-items:center;
            background-color: #0e1117;
            color: white;
            padding:20px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 10px;
            gap: 15px;
        }

        #logged {
            font-size: 12px;
            color: grey;
        }

        #loggedin {
            font-size: 20px;
            color: white;
        }

        #initial {
            width: 50%;
            height: 100%;
        }

        #info{
            width: 60%;
            height: 100%;
            font-size: 10px
        }

        h2 {
            padding:0px;
        }

        h5 {
            padding:0px;
            color:grey;
        }

        </style>
        <br><br>
        """,
        unsafe_allow_html=True
    )
    try:
        if st.sidebar.button("Logout"):
            for key in st.session_state.keys():
                del st.session_state[key]
            st.rerun() 
    except Exception as e:
        st.toast("Something Went Wrong!! - Error LOUT")

    try:
        if st.sidebar.button("Clear Chats"):
            clear_chats(st.session_state.username)
    except Exception as e:
        st.toast("Something Went Wrong!! - Error CLRC")
    

    st.sidebar.subheader("Questions")

    try:
        user_queries = get_user_queries(st.session_state.username)
        questions = list(user_queries.keys()) if user_queries else []

        for i, question in enumerate(questions):
            if st.sidebar.button(question[0:55] + "...", key=f"button_{i}"):
                st.session_state.selected_question = question
    except Exception as e:
        st.toast("Something Went Wrong!! - Error QNF")


    st.subheader("Questionaries")

    try:
        if "selected_question" in st.session_state:
            selected_question = st.session_state.selected_question
            answer = user_queries[selected_question]

            with st.expander("QA", expanded=True):
                st.markdown(f"""
                    <div style="color: #FF7900;">
                        <strong>Query:</strong><br>
                    </div>{selected_question}
                    <div style="color: #228B22;">
                        <strong>Response:</strong><br>
                    </div>{answer} <br><br>
                """, unsafe_allow_html=True)

                if st.button("Close"):
                    st.session_state.pop("selected_question")
    except Exception as e:
        pass

    if "messages" not in st.session_state:
        st.session_state.messages = []

    try:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    except Exception as e:
        st.toast("Something Went Wrong!! - Error QAF")

    try:

        if prompt := st.chat_input("What is up?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                response_placeholder = st.empty() 
                full_response = ""
                for partial_word in response_generator(prompt):
                    full_response += partial_word
                    response_placeholder.markdown(full_response)
                cleaned_response = clean_response(full_response)
                response_placeholder.markdown(cleaned_response) 

                st.session_state.messages.append({"role": "assistant", "content": cleaned_response})
                global previous_convo
                one_convo = f"User: {prompt}\nResponse: {cleaned_response}"
                previous_convo = previous_convo + one_convo
                update_db(st.session_state.username, prompt, cleaned_response)
    except Exception as e:
        st.toast("Something Went Wrong!! - Error QACF")

if __name__ == '__main__':
    try:
        chatbot_interface()
    except Exception as e:
        st.toast("Something Went Wrong!! - Error CBIF")
