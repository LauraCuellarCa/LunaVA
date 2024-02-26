from langchain.chat_models import AzureChatOpenAI
from dotenv import load_dotenv
import os
import streamlit as st
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from plugins.news_integration import news_response
from plugins.weather_integration import weather_response

# Load environment variables at the top to avoid errors
load_dotenv()

# I was not able to get the key to work loading from the env why?
API_WEATHER_KEY = os.getenv("API_WEATHER_KEY")
NEWSAPI_KEY = os.getenv("NEWS_API_KEY")

# Load GPT model
gpt_turbo = AzureChatOpenAI(deployment_name="gpt-turbo", temperature=0.5)
list_shown = []

# Main function
def run_luna():
    st.title('🌚  Welcome to Luna')
    st.subheader('Hi, I am Luna!\n I am here to assist you in starting & ending your day in the best way possible. \n What can I do for you? :)')

    # Initialize memory chain
    memory = ConversationBufferMemory()
    chain = ConversationChain(llm=gpt_turbo, verbose=True, memory=memory)  # Fix here

    # Initialize streamlit chat history
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []

    # Access or update session_state.messages
    session = st.session_state['messages']


    # Display chat history
    for message in session:
        if message["content"] not in list_shown:
            print(f"message: {message}")
            with st.chat_message(message["role"]):
                list_shown.append(message["content"])
                st.markdown(message["content"])

    # Creating a text box
    user_query = st.chat_input("Ask me anything")

    # If query
    if user_query is not None:
        # Display user query on screen
        st.chat_message("user").markdown(user_query)
        session.append({"role": "user", "content": user_query})

        # Router
        # Identifying topic
        identifying_topic = f""" Instruction: You have to identify the topic of a user query and match it to one of the listed categories. 
        Return only a string with the name of the chosen category.
        Categories: weather, news, other "
        User query: {user_query}
        Answer:
        """

        query_topic = gpt_turbo.predict(identifying_topic)

        # Responding to weather questions
        if "weather" == query_topic:
            response = weather_response(user_query, chain)
            session.append({"role": "Luna", "content": response})
            if type(response) is not str:
                old_ans = response
                response = f"Failed to retrieve weather. Status code:{old_ans}"

        # Responding to news-related queries
        elif "news" == query_topic:
            response = news_response(user_query, chain, session)
            print(f"response: {response}")
            if type(response) is not str:
                response = f"Failed to retrieve news"

        # Responding to other queries
        else:
            response = gpt_turbo.predict(user_query)

        with st.chat_message("assistant", avatar="🌜"):
            st.markdown(response)

        # Add response to memory
        session.append({"role": "Luna", "content": response})
        print(f"session state message appended to memory: {response}")


# Run Luna app
run_luna()

