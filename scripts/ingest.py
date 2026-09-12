from tools import *

def ingest_workflow(file_path):
    text=read_pdf(file_path)
    ingest_prompt=load_instruction("prompts/ingest_prompt.txt")
    ingest_skill=load_instruction("skills/wiki_skills/ingest_skill.md")
    instruction=f"""prompt:{ingest_prompt}
                    skill:{ingest_skill}
                    """
    user_input=f"""{text}"""
    wiki_content=call_llm(instruction,user_input)
    title=file_path.split("/")[-1]
    write_db(title,wiki_content)

    return wiki_content
