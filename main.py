import os

from scripts.ingest import ingest_workflow
from scripts.query import query_workflow
from scripts.lint import lint_workflow
from tools import load_instruction,call_llm

agent_instructions = load_instruction("agent.md")
user_query = input("请输出需求：")
action = call_llm(agent_instructions,f"""user query:{user_query}
                只输出要执行的action：
                ingest/query/lint/ingest,query/query,lint/ingest,lint/ingest,query,lint""").strip()

answer = None
context = None

if "ingest" in action:
    pdf_files = ["wiki document.pdf"]
    file_path = input("请输入要ingest的新pdf文件路径（回车跳过）：").strip()
    if file_path:
        pdf_files.append(file_path)
    for pdf in pdf_files:
        if os.path.exists(pdf):
            ingest_workflow(pdf)
        else:
            print(f"未找到文件:{pdf}")

if "query" in action:
    answer,context = query_workflow(user_query)

if "lint" in action:
    lint_result = lint_workflow(user_query,answer,context)
    while lint_result == "FAIL":
        answer,context = query_workflow(user_query)
        lint_result = lint_workflow(user_query,answer,context)

if answer != None:
    print(answer)
else:
    print("workflow执行完成")




