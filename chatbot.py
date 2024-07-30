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

try:
    genai.configure(api_key=config['API']['APIKEY'])
except Exception as e:
    st.toast("Invalid Key!!!")

def clean_response(response):
    try:
        if response.startswith("Response:"):
            response = response[len("Response:"):].strip()
        return response
    except Exception as e:
        st.toast("Something Went Wrong!! - Error CLX")


def response_generator(user_query):
    try:
        prompt = f"""You are Empathia, a digital therapist/psychiatrist  using the Gemini 1.5 Flash model developed by Counsellor. Your purpose is to provide professional support and guidance tailored to the user's mental health needs. Maintain strict confidentiality and privacy. Respond with empathy, offer professional advice, and suggest coping strategies when appropriate. Do not handle emergency situations; instead, direct users to seek immediate assistance from qualified professionals. Always ask for the user's name when requested.
            Consider previous interactions in the conversation history to maintain continuity and context. Use information from past conversations to provide relevant and coherent responses. If the user references past discussions, acknowledge them and build upon that context.
            
            Example 1:
            User: "I've been feeling anxious about my upcoming presentation at work. How can I manage my anxiety?"
            Response: "It's completely normal to feel anxious about a big presentation. As we discussed previously, practicing relaxation techniques like deep breathing or progressive muscle relaxation can help. Additionally, you might want to review the strategies we talked about for managing stress. Preparing thoroughly and rehearsing can boost your confidence. If you need further support, reaching out to a colleague or a therapist might be beneficial."
            Example 2:
            User: "I'm struggling with low self-esteem and negative thoughts. What can I do to improve my self-image?"
            Response: "Improving self-esteem can be challenging. Reflecting on our earlier conversations, focusing on your strengths and achievements might be a good start. Remember to challenge negative thoughts and practice self-compassion. Engaging in activities you enjoy, as we discussed, can also boost your self-image. If these feelings persist, talking to a mental health professional could provide more tailored support."
            Example 3:
            User: "I often feel overwhelmed by my daily responsibilities. How can I better manage my stress?"
            Response: "Managing stress from daily responsibilities can be tough. Considering our previous discussions, breaking tasks into smaller steps and prioritizing them can help. Developing a routine that includes relaxation and self-care is also important. Techniques like mindfulness, which we talked about earlier, might be useful. If you continue to feel overwhelmed, discussing it with a therapist might offer additional strategies."

            Use the examples above to guide your responses. Address the user's query with empathy and provide actionable advice or coping strategies. Ensure that responses are supportive and tailored to the user's specific concerns. Always consider previous interactions to maintain context and continuity in the conversation.

            Past Conversations:
            {previous_convo}

            User: {user_query}
        """
    except Exception as e:
        st.toast("Something Went Wrong!! - Error PTX")

    generation_config = {
      "temperature": 0.5,
      "top_p": 0.95,
      "top_k": 64,
      "max_output_tokens": 2048,
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

    system_instruction = """
        Instructions for Interacting with Your Digital Therapist/Psychiatrist:

        1. Purpose:
        - This digital assistant serves as your mental health and therapy companion, providing professional support, guidance, and conversation tailored to your well-being.
        - Engage in open-ended conversations or ask specific questions related to your mental health concerns.

        2. Safety and Privacy:
        - Your privacy and confidentiality are of utmost importance. The digital assistant is programmed to maintain strict confidentiality and privacy standards.
        - Avoid sharing sensitive personal information that could compromise your privacy or safety.

        3. Interaction:
        - Type your thoughts, feelings, or concerns into the text input area to begin a conversation with your digital therapist/psychiatrist.
        - The assistant will respond with supportive, empathetic messages, offering professional guidance, reflections, and coping strategies.
        - Always introduce yourself with your name and the name of your therapist/psychiatrist when asked.

        4. Emergency Situations:
        - If you're experiencing a mental health crisis or emergency, please seek immediate assistance from a qualified mental health professional or emergency services.
        - The digital assistant is not equipped to handle emergency situations and should not be relied upon for urgent assistance.

        5. Model Information:
        - The assistant operates on the Gemini 1.5 Flash model developed by Counsellor.
        - The model has been configured with specific settings to ensure the quality, safety, and effectiveness of interactions.

        6.Feedback:
        Your feedback is valuable for improving this service and enhancing your experience. Feel free to share your thoughts, suggestions, or concerns with us.

        Remember, your digital therapist/psychiatrist is here to support you on your journey towards better mental health. Let's engage in meaningful conversations together!

    """
    try:
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            safety_settings=safety_settings,
            system_instruction=system_instruction
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
