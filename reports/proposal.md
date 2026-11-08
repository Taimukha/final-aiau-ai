# Project Proposal — Semester Week 10

## Project Title

**BookMatch AI — Personalized Book Recommendation Assistant**

## Problem Description

Many people want to read books but struggle to find suitable ones. Books may not match their interests, preferred language, or reading preferences. General recommendation lists often provide limited explanations.

BookMatch AI will help users discover suitable books through an AI-powered assistant. The system will recommend books from a local catalog and explain why they match the user's interests.

## Target Users

- Students and young adults who want to develop reading habits.
- People interested in self-development, fiction, mystery, and adventure.
- Readers who prefer Kazakh, Russian, or English books.
- Users who want personalized recommendations without spending too much time searching.

## Selected Difficulty

**C Level — Intermediate (LLM with Tool Calling)**

The application will use a real language model API and two model-callable tools. The model will decide which tools to use, receive their results, and generate grounded responses.

## Expected Functionality

1. Users can select their preferred book language and genre.
2. Users can describe their interests through a form or AI chat.
3. The assistant recommends up to three relevant books from a local catalog.
4. Each recommendation includes a short description, reasons for matching, and possible reading challenges.
5. Users can request more information about a selected book.
6. Users can compare books and ask follow-up questions.
7. Users can request a simple seven-day reading plan.
8. An Agent Activity panel shows actual tool execution logs.
9. The system handles missing books, invalid inputs, and API errors.

The initial catalog will contain approximately 18 books in Kazakh, Russian, and English. If fewer than three books match the filters, the assistant will explain this rather than invent additional books.

## Proposed Functions

### 1. `load_books()`

- **Purpose:** Load and validate book data from the local catalog.
- **Inputs:** Path to `books.json`.
- **Outputs:** List of valid book records or a controlled error.
- **Dependencies:** Python, JSON file.

### 2. `search_books(language, genre, query)`

- **Purpose:** Search the catalog using language, genre, and user interests.
- **Inputs:** Language, genre, optional search query.
- **Outputs:** Matching books with IDs, titles, authors, and short descriptions.
- **Dependencies:** `load_books()`, `books.json`.

### 3. `get_book_details(book_id)`

- **Purpose:** Retrieve verified information about a selected book.
- **Inputs:** Book ID.
- **Outputs:** Book title, author, description, topics, and possible reading challenges, or a not-found result.
- **Dependencies:** `load_books()`, `books.json`.

### 4. `validate_tool_arguments(tool_name, arguments)`

- **Purpose:** Check tool names, required parameters, and input types before execution.
- **Inputs:** Tool name and arguments provided by the LLM.
- **Outputs:** Validated arguments or a structured validation error.
- **Dependencies:** Python validation logic.

### 5. `run_agent(user_message, conversation_history)`

- **Purpose:** Send requests to the LLM, handle model-selected tool calls, and generate responses.
- **Inputs:** User message, conversation history, and selected form preferences.
- **Outputs:** Assistant response and tool execution information.
- **Dependencies:** LLM API, tool definitions, validation, and tool execution functions.

### 6. `generate_reading_plan(book, user_preferences)`

- **Purpose:** Prepare a simple seven-day reading plan using available book information and user preferences.
- **Inputs:** Selected book details and optional reading preferences.
- **Outputs:** Seven-day reading plan.
- **Dependencies:** Book information and LLM response generation.

### 7. `log_tool_execution(tool_name, arguments, result_status)`

- **Purpose:** Record actual tool execution for debugging and demonstration.
- **Inputs:** Tool name, safe argument summary, execution status, and optional error.
- **Outputs:** Structured log entry.
- **Dependencies:** Python, Streamlit session state.

## Proposed Agent Tools

### Tool 1: `search_books`

A model-callable tool that searches the local book catalog. The LLM can select this tool when the user requests book recommendations or searches for books with specific characteristics.

### Tool 2: `get_book_details`

A model-callable tool that retrieves detailed information about a specific book. The LLM can use it to explain a selected book or compare multiple books.

The tools will be independently testable. The application will validate model-generated arguments, execute the requested tools, and return the results to the LLM.

The LLM may call one tool, multiple tools, or no tools depending on the request.

## Model Selection

**Planned provider:** OpenRouter  
**Planned model:** A tool-calling-capable language model available through OpenRouter.

The final model will be selected after testing API compatibility, tool-calling support, and response quality.

**Programming language:** Python  
**User interface:** Streamlit  
**Data storage:** Local `books.json` file

## Architecture

The proposed workflow is:

1. The user enters preferences or a message in Streamlit.
2. The application sends the user request and relevant conversation context to the LLM.
3. The LLM decides whether to call `search_books` or `get_book_details`.
4. Python validates the tool arguments.
5. The requested tool executes using the local book catalog.
6. Tool results are returned to the LLM.
7. The LLM generates a response based on the available information.
8. The application displays the response and tool execution logs.

Conversation history will be maintained during the active Streamlit session. Tool calls will have execution limits to prevent uncontrolled loops.

## Example Requests

1. "Recommend easy-to-read Kazakh books about motivation."
2. "Find English mystery books with interesting stories."
3. "Tell me more about Atomic Habits."
4. "Compare Atomic Habits and Mindset. Which is more practical?"
5. "Create a seven-day reading plan for the book I selected."
6. "What is the difference between fiction and non-fiction?"

The final example may be answered without using a tool.

## Evaluation Plan

The application will be evaluated using at least eight test cases:

1. Successful recommendation request.
2. Correct filtering by book language.
3. Correct filtering by genre.
4. Successful book details retrieval.
5. Comparison of two available books.
6. A general question that does not require tools.
7. No matching books in the catalog.
8. Invalid or missing book ID.
9. Invalid tool arguments.
10. API or tool execution failure.

Evaluation will check tool selection, argument validation, response grounding, error handling, and execution logs.

The application will not claim that a book exists in the catalog when it is unavailable.

## Weekly Milestones

| Week | Planned Activities |
|---|---|
| Week 10 | Select the project topic, define scope, and complete the proposal. |
| Week 11 | Set up the Python project, Streamlit interface, and LLM API connection. |
| Week 12 | Prepare and validate the multilingual book catalog. |
| Week 13 | Implement and independently test the two model-callable tools. |
| Week 14 | Connect tools to the LLM and implement the agent workflow. |
| Week 15 | Add error handling, execution logs, and optional reading plans. |
| Week 16 | Run at least eight evaluation tests and improve reliability. |
| Week 17 | Finalize documentation, demonstrate the application, and prepare for defense. |
