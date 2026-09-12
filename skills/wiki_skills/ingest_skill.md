# 目标
接受用户上传的文档，将文档转化为Wiki context并对数据库进行更新
# 调用方式
执行：python scripts/ingest.py<file>
输入: - pdf文件
输出: - wiki context
      - 数据库更新结果     
# 可调用函数
- read_pdf(file)
- load_prompt(file)
- call_llm(prompt,user_input)
- write_db(title,content)
# skills
- clean_content
  对原始文档进行清洗，去掉多余的标点符号/空格/乱码等
- entity_extract
  提取文档中核心实体的概念、名称，构建内容结构
- relationship_extract
  总结实体之间的关系和结构，形成关联系统
- graph_construct
  根据实体关系构建图表/流程图等
- duplicate_detect
  检查数据库中的已有内容，避免重复写入
# 逻辑
- 根据文档内容决定是否更新已有Wiki
- 提取文档中的核心内容并进行模块化总结
- 将总结内容导入Wiki库中