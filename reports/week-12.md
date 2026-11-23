# Week 12 Progress Report — Core Functionality

## 1. Completed Work

During this week, I implemented the core functionality of BookMatch AI.

- Created a working Streamlit application interface.
- Created a local JSON book catalog containing 6 books in Kazakh, Russian, and English.
- Implemented `load_books()` to load book data from the JSON file.
- Implemented `search_books()` to search books by language, genre, and keywords.
- Implemented `get_book_details()` to retrieve information about a book by its ID.
- Added input validation and error handling for invalid search parameters and book IDs.
- Integrated OpenRouter API using the OpenAI Python library.
- Added an AI chat interface with conversation history.
- Configured environment variables to keep the API key outside the source code.

## 2. Important Commits

**Commit:** `0e053ac`

**Message:** `feat: complete week 12 core BookMatch AI application`

The implementation was pushed to the GitHub repository.

## 3. Current Functionality

The application currently supports:

- Selecting a preferred book language.
- Selecting a favorite genre.
- Searching and displaying books from the local JSON catalog.
- Viewing book titles, authors, descriptions, and difficulty levels.
- Asking questions through the AI chat interface.
- Maintaining chat history during the current Streamlit session.

The AI chat currently responds to general user questions. Automatic LLM tool selection and execution are planned for Week 13.

## 4. Testing

Implemented and executed 9 automated tests using pytest.

All 9 tests passed successfully.

Tests cover:
- Loading the book catalog.
- Searching by language.
- Searching by genre.
- Retrieving book details.
- Handling books that do not exist.
- Validating language and genre inputs.
- Handling invalid input types and book IDs.

## 5. Problems and Solutions

**Problem:** The new project environment did not initially include pytest.

**Solution:** Installed pytest and updated `requirements.txt`.

**Problem:** The local project folder was not connected to the GitHub repository.

**Solution:** Cloned the existing GitHub fork and copied the implementation files into it, preserving the original repository history and reports.

## 6. What I Learned

- How to build a basic application using Streamlit.
- How to organize book data in JSON.
- How to separate application logic into Python modules.
- How to connect an application to an LLM through OpenRouter.
- How to validate function inputs and write automated tests.
- How to manage project dependencies and publish code using Git.

## 7. Next Week's Plan

- Implement at least two callable tools for the AI agent.
- Define tool descriptions and argument schemas.
- Allow the LLM to select the appropriate tool.
- Execute selected tools in Python.
- Return tool results to the LLM to generate grounded book recommendations.
