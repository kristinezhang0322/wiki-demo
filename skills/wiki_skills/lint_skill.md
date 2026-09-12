# 目标
检查刚刚生成的答案
# 调用方式
执行：python scripts/lint.py
输入：-user question
      -generated answer
      -Wiki content
输出：-PASS
      -WARNING
      -FAIL
# 可调用函数
- call_llm(prompt，user_input)
- load_prompt(file)
# skills
- content_check：
  检查答案是否与Wiki context中的一致
- security_check
  进行安全检查，保证没有公司/个人隐私信息泄露
  生成的答案符合政治、道德规范
- format_check
  检查输出格式是否正确
# 逻辑
- PASS:答案通过了所有检索，安全、准确、符合Wiki context
- WARNING:答案的部分信息不够完整或存在不确定性
- FAIL:出现虚构内容、危险内容、严重偏离Wiki context
# 输出
只输出PASS/WARNING/FAIL