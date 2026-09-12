from tools import *

def query_workflow(question):
    wiki_results=search_wiki(question)
    query_prompt=load_instruction("prompts/query_prompt.txt")
    query_skill=load_instruction("skills/wiki_skills/query_skill.md")
    context=str(wiki_results)
    instruction=f"""prompt:{query_prompt}
                    skills:{query_skill}
                    """
    user_input=f"""user question:{question}
                    wiki context:{context}
                    """
    answer=call_llm(instruction,user_input)
    save_history(question,answer)
    return answer,context