# Semester Week 10 Progress Report

## Completed Work

- Selected the final project topic: **BookMatch AI — Personalized Book Recommendation Assistant**.
- Reviewed the project requirements and selected **C Level (Intermediate)**.
- Defined the main problem, target users, and expected functionality.
- Planned a multilingual book recommendation system supporting Kazakh, Russian, and English.
- Decided to start with approximately 18 books stored in a local JSON catalog.
- Designed two model-callable tools: `search_books` and `get_book_details`.
- Planned additional features, including book comparison, AI chat, a seven-day reading plan, and an Agent Activity panel.
- Completed the project proposal in `reports/proposal.md`.
- Prepared the GitHub repository for further development.

## Important Commits

- `docs: complete BookMatch AI project proposal` — Completed the Week 10 project proposal, including the project scope, proposed functions, tools, architecture, evaluation plan, and weekly milestones.

## Current Functionality

The project is currently in the planning stage.

The expected application workflow and tool architecture have been designed, but the Python implementation has not started yet.

The planned system will use Streamlit for the interface, an LLM API for generating responses, and a local JSON catalog for book information.

## Problems Encountered

- Choosing a project idea that is useful and achievable within the semester.
- Deciding how many books to include in the initial catalog.
- Designing an AI assistant that uses real model-selected tools rather than hardcoded responses.
- Balancing useful features with the C Level project requirements.

## Solutions

- Selected BookMatch AI because it addresses a practical problem and supports meaningful LLM tool calling.
- Limited the initial catalog to approximately 18 books, with the possibility of expanding it later.
- Planned two independently executable tools for book search and book details.
- Prioritized core agent functionality, reliability, and testing over unnecessary additional features.
- Defined a weekly implementation plan to manage project development.

## What I Learned

- How to define a clear problem statement and project scope.
- The difference between a regular chatbot and an AI agent that can select and execute tools.
- Why tool arguments must be validated before execution.
- How local structured data can help an AI assistant generate more reliable recommendations.
- Why testing, error handling, and execution logs are important for an AI agent.

## Next Week

In Week 11, I plan to:

1. Set up the Python development environment.
2. Create the initial project folder structure.
3. Install the required dependencies.
4. Build a basic Streamlit interface.
5. Connect the application to a real LLM API.
6. Test a simple user-to-model conversation.
7. Record progress and commits in the Week 11 report.
