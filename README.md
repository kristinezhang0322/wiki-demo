python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
## Introduction
你是一个用workflow来实现的未来中心智能体展厅的Wiki智能问答系统，用户会在这里向你
提任何与展览内容相关的问题，你需要根据要求生成Wiki系统并给出解答

## Project Structure
  ## Main Files
  - agent.md 项目运行指导
  - main.py 主代码
  - tools.py 需要用到的python工具的代码
  ## Virtual Environment
  - .venv 虚拟环境安装包
  - requirements.txt 需要的安装包
  ## Prompts
  - ingest_prompt.txt ingest workflow的规则
  - query_prompt.txt query workflow的规则
  - lint_prompt.txt lint workflow的规则
  ## Skills
    - wiki_skills
      - wiki skill.md 三个workflow的调用总规则
      - ingest_skill.md ingest里要用到的具体skills
      - query_skill.md query里要用到的具体skills
      - lint_skill.md lint里要用到的具体skills
    - other_skills
      - other skill.md 外界skill的调用总规则
      - agent-browser-clawdbot-SKILL 网页搜索skill
      - agent-builder-SKILL 个性化agent建立skill
  ## Scripts
  - ingest.py ingest的具体代码
  - query.py query的具体代码
  - lint.py lint的具体代码
  ## References
  - wiki document.pdf 参考的讲解词资料
  ## Database
  - wiki.db wiki数据库
  ## .vscode
  - settings.json 隐藏运行代码时产生的_pycache_


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