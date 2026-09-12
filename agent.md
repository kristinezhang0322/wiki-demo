#  Virtual Environment
Use '.venv' as the project's virtual environment. Before running the project, make sure the virtual environment is activated.
#  Agent Overview
This agent is a wiki-based Q&A system designed for an interactive exhibition demo
The agent uses 'wiki skill.md' to manage the wiki knowledge base, answer user questions and invoke the appropriate wiki workflow
It also uses 'other skill.md' to manage external capabilities, such as web search and customized agent creation

# Trigger：
- Uploading documents to the wiki knowledge base
- Asking questions related to wiki content
- Updating the wiki knowledge base
- Validating generated answers
- Searching the web for additional information when the wiki does not contain sufficient information
- Saving records of user questions

For detailed workflow rules, see:
- 'skills/wiki_skills/wiki skill.md'
- 'skills/other_skills/other skill.md'
