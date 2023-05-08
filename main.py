# """Python file to serve as the frontend"""
# import streamlit as st
# #import creds
# from streamlit_chat import message

# from langchain.chains import ConversationChain
# from langchain.llms import OpenAI

# import os

# os.environ["OPENAI_API_KEY"]="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"


# def load_chain():
#     """Logic for loading the chain you want to use should go here."""
#     llm = OpenAI(temperature=0)
#     chain = ConversationChain(llm=llm)
#     return chain

# chain = load_chain()

# # From here down is all the StreamLit UI.
# st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
# st.header("Generative Chat Demo EB")

# if "generated" not in st.session_state:
#     st.session_state["generated"] = []

# if "past" not in st.session_state:
#     st.session_state["past"] = []

# #input = "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" ##################
# # my_dict= { "input" :"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"}

# def get_text():
#     input_text = st.text_input("You: ", "Hello, how are you?", key= "input") #creds.api_key ) ## key= my_dict.get("input")) # key="input") #   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
#     return input_text


# user_input = get_text()

# if user_input:
#     output = chain.run(input=user_input)

#     st.session_state.past.append(user_input)
#     st.session_state.generated.append(output)

# if st.session_state["generated"]:

#     for i in range(len(st.session_state["generated"]) - 1, -1, -1):
#         message(st.session_state["generated"][i], key=str(i))
#         message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")

import streamlit as st
from streamlit_chat import message
from langchain.chains import ConversationChain
from langchain.llms import OpenAI

import os

os.environ["OPENAI_API_KEY"] = "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"

def load_chain():
    """Logic for loading the chain you want to use should go here."""
    llm = OpenAI(temperature=0)
    chain = ConversationChain(llm=llm)
    return chain

def get_text():
    input_text = st.text_input("You: ", "Hello, I am Emmanuel, and you ?", key="input")
    return input_text


def main():
    chain = load_chain()

    # From here down is all the Streamlit UI.
    st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
    st.header("Generative Chat Demo Manu87DS")

    if "generated" not in st.session_state:
        st.session_state["generated"] = []

    if "past" not in st.session_state:
        st.session_state["past"] = []

    user_input = get_text()

    if user_input:
        output = chain.run(input=user_input)

        st.session_state.past.append(user_input)
        st.session_state.generated.append(output)

    if st.session_state["generated"]:
        for i in range(len(st.session_state["generated"]) - 1, -1, -1):
            message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")
            message(st.session_state["generated"][i], key=str(i))
            


if __name__ == "__main__":
    main()

