
import streamlit as st

from src.book_tools import search_books
from src.llm import ask_ai


# Page settings
st.set_page_config(
    page_title="BookMatch AI",
    page_icon="📚",
    layout="centered"
)


# App title
st.title("📚 BookMatch AI")
st.write("Your personal book recommendation assistant.")

st.divider()


# BOOK SEARCH SECTION
st.header("🔍 Find Books")
st.write("Choose your preferences to find a suitable book.")

language = st.selectbox(
    "Choose your language",
    ["Kazakh", "Russian", "English"]
)

genre = st.selectbox(
    "Choose your favorite genre",
    [
        "All genres",
        "Psychology & Self-development",
        "Fiction",
        "Adventure & Fantasy",
        "Mystery & Detective"
    ]
)

if st.button("Find Books"):
    selected_genre = None if genre == "All genres" else genre

    books = search_books(
        language=language,
        genre=selected_genre
    )

    if books:
        st.subheader("Books found")

        for book in books:
            with st.container(border=True):
                st.markdown(f"### {book['title']}")
                st.write(f"Author: {book['author']}")
                st.write(f"Language: {book['language']}")
                st.write(f"Genre: {book['genre']}")
                st.write(book["description"])
                st.write(f"Difficulty: {book['difficulty']}")
    else:
        st.info("No books found. Try different preferences.")


# AI CHAT SECTION
st.divider()
st.header("🤖 Chat with BookMatch AI")
st.write("Ask me about books, reading, motivation or personal development.")


# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Get a new message
user_prompt = st.chat_input("Ask something about books...")


if user_prompt:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_prompt
    })

    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Build conversation context
    conversation = ""

    for message in st.session_state.messages:
        conversation += (
            f"{message['role'].capitalize()}: "
            f"{message['content']}\n"
        )

    # Ask AI
    with st.chat_message("assistant"):

        with st.spinner("BookMatch AI is thinking..."):

            try:
                answer = ask_ai(conversation)

                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as error:
                st.error(
                    "Sorry, something went wrong while connecting to AI."
                )
                st.caption(f"Technical details: {error}")
