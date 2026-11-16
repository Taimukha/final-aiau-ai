# Semester Week 11 Progress Report

## Completed Work

- Continued planning the BookMatch AI project after completing the Week 10 proposal.
- Reviewed the planned C Level architecture and the requirements for LLM tool calling.
- Defined the initial technology stack: Python, Streamlit, OpenRouter, and a local JSON book catalog.
- Identified the two main tools: `search_books` and `get_book_details`.
- Clarified the expected user interaction flow: book preferences, recommendations, follow-up questions, comparisons, and reading plans.
- Prepared the implementation plan for the first working prototype.

## Important Commits

- Week 10 proposal and progress report commits were completed previously.
- No application code commits have been completed for Week 11 yet.

## Current Functionality

The project proposal and system design are ready.

The application is not yet implemented. The next step is to create a basic Streamlit interface and establish a real LLM API connection.

## Problems Encountered

- Selecting a suitable LLM model that supports tool calling.
- Planning how to connect the Streamlit interface to the model API.
- Keeping the first implementation simple enough to test and explain.

## Solutions

- Selected OpenRouter as the planned API provider.
- Decided to implement the project incrementally, beginning with a basic chatbot.
- Planned to add book search and book details tools after verifying the LLM connection.
- Kept the initial catalog limited to approximately 18 books.

## What I Learned

- The importance of separating the user interface, model interaction, and tool execution logic.
- Why a working LLM connection should be tested before implementing the complete agent.
- How a local JSON catalog can serve as a structured data source for model-callable tools.
- Why the project should be developed and tested in small stages.

## Next Week

1. Create the Python project structure.
2. Install Streamlit and the required API libraries.
3. Configure the LLM API key securely using environment variables.
4. Implement and test a basic Streamlit chatbot.
5. Begin preparing the local `books.json` catalog.
6. Commit working code and record the results.
