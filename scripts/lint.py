from tools import *

def lint_workflow(question,answer,context):
    lint_prompt=load_instruction("prompts/lint_prompt.txt")
    lint_skill=load_instruction("skills/wiki_skills/lint_skill.md")
    instruction=f"""prompt:{lint_prompt}
                    skill:{lint_skill}
                    """
    user_input=f"""user question:{question}
                   wiki context:{context}
                   generated answer:{answer}
                   """
    lint_result=call_llm(instruction,user_input)
    return lint_result