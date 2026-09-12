import sqlite3
from openai import OpenAI
from pypdf import PdfReader

client=OpenAI(
    api_key="sk-e19ef62f11ce4e099003844a09ed02f0",
    base_url="https://api.deepseek.com/v1")

conn=sqlite3.connect("wiki.db")
def call_llm(instruction,user_input):
    response=client.chat.completions.create(
        model="deepseek-chat",max_tokens=4000,
        messages=[{"role":"user","content":f"""{instruction}{user_input}"""}]
    )
    return response.choices[0].message.content

def read_pdf(file_path):
    reader=PdfReader(file_path)

    text=""

    for page in reader.pages:
        page_text=page.extract_text()

        if page_text:
            text+=page_text+"\n"

    return text

def write_db(title,content):
    conn=sqlite3.connect("wiki.db")
    cursor=conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS wiki_pages(id INTEGER PRIMARY KEY 
                   AUTOINCREMENT,title TEXT,content TEXT)""")
    cursor.execute("""INSERT INTO wiki_pages(title,content)
                   VALUES(?,?)""",(title,content))
    
    conn.commit()
    conn.close()

def search_wiki(question):
    conn=sqlite3.connect("wiki.db")
    cursor=conn.cursor()
    cursor.execute("""SELECT title,content FROM wiki_pages""")
    results=cursor.fetchall()
    conn.close()
    return results

def save_history(user_question,answer):
    conn=sqlite3.connect("wiki.db")
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS chat_history(id INTEGER PRIMARY KEY AUTOINCREMENT,question TEXT,answer TEXT)""")
    cursor.execute("""INSERT INTO chat_history(question,answer)VALUES(?,?)""",(user_question,answer))
    conn.commit()
    conn.close()

def load_instruction(file):
    with(open(file,"r",encoding="utf-8"))as f:
        instruction=f.read()
    return instruction
