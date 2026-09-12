# 目标
基于Wiki context，回答用户问题，并生成结构化答案
# 调用方式
执行：python scripts/query.py <question>
输入: -用户问题
输出: -回答内容
      -相关Wiki context
# 可调用函数
- search_wiki(question)
- load_prompt(file)
- call_llm(prompt,user_input)
- save_history(question,answer)
# skills
- classify_question
  将问题进行分类，内容型和关系型
- generate_question
  将关系问题的自然语言转化为图语言
- post_answer
  将图数据库中的语言转化为用户能看懂的可输出的自然语言
- synthesize_answer
  对搜寻到的资料进行整合、总结，生成简短答案
- calculate_tool
  需要时使用计算工具（涉及概率/成本等问题）
- diagram_result
  需要时输出图标答案
- store_memory
  将每次问答记录存储
- show_memory_logs
  用户需要时显示前三次的历史问答记录
- retrieval_memory
  去用户的历史问答记录中搜索与该问题相关的内容
- personalize_tone
  根据对用户身份的推测调整答案的语气
# 逻辑
- 根据Wiki context回答问题
- 根据问题类型决定回答结构
- 对于涉及流程/关系的问题，采用图表和文字结合的方式进行输出回答
- 对搜寻到的问题相关内容自行总结、简化，生成答案
- 对答案的语气进行调整和优化，采用适合用户身份的语气