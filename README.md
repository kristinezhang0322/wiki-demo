python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
## Introduction
A workflow-based intelligent wiki Q&A system designed for an interactive exhibition demo
User can ask questions related to the exhibition content, and the system retrieves relevant information from the wiki knowledge base to generate response.

## Project Structure
  ## Main Files
  - 'agent.md' Instructions and workflow configuration for the agent
  - 'main.py' Main application entry point
  - 'tools.py' Python utility functions used by the workflows
  ## Virtual Environment
  - '.venv' Local python virtual environment
  - 'requirements.txt' Project dependencies
  ## Prompts
  - 'ingest_prompt.txt' Instructions for the ingest workflow
  - 'query_prompt.txt' Instructions for the query workflow
  - 'lint_prompt.txt' Instructions for the lint workflow
  ## Skills
    - wiki_skills
      - 'wiki skill.md' General rules shared across the 3 workflows
      - 'ingest_skill.md' Skills used by the ingest workflow
      - 'query_skill.md' Skills used by the query workflow
      - 'lint_skill.md' Skills used by the lint workflow
    - other_skills
      - 'other skill.md' General rules for external skills
      - 'agent-browser-clawdbot-SKILL' Web search skill
      - 'agent-builder-SKILL' Skill for building customized agents
  ## Scripts
  - 'ingest.py' Implementation of the ingest workflow
  - 'query.py' Implementation of the query workflow
  - 'lint.py' Implementation of the lint workflow
  ## References
  - 'wiki document.pdf' Reference material used for the exhibition demo
  ## Database
  - 'wiki.db' SQLite database storing processed Wiki content
  ## .vscode
  - 'settings.json' VS code workspace settings


## Design Principles
- prompt
  defines workflow objectives
- skill
  defines workflow capabilities
- script
  implements workflow execution
- tool
  provides reusable functions
- workflow selection
  selects appropriate skills based on user query

## Agent Workflow
  user query
  ↓
  select skill
  ↓
  execute workflow
  ↓
  call tools 
  ↓
  generate answer
  ↓
  security/content/form check

## Run
python main.py: 本地demo
agent.md + scripts/*.py: Claude Code/CodeX
