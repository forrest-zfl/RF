from docx import Document

# 将员工真实的信息以字典的形式进行保存
person_list = [
    {
        "name":"欣迪",
        "id":"333222444555666999",
        "sdate":"2018年3月1日",
        "edate":"2022年2月10日",
        "department":"技术部",
        "position":"数据分析专家",
        "company":"深圳腾讯科技有限公司"
    },
    {
        "name":"文定",
        "id":"323242464785676954",
        "sdate":"2019年4月11日",
        "edate":"2022年2月15日",
        "department":"行政部",
        "position":"打手",
        "company":"赣州天上人间会所"
    },
    { 
        "name":"周超",
        "id":"643242466485673954",
        "sdate":"2017年5月21日",
        "edate":"2022年2月14日",
        "department":"后厨部",
        "position":"配菜员",
        "company":"深圳金威源餐饮有限公司"
 },
    {
        "name":"李军",
        "id":"443245466455673954",
        "sdate":"2019年8月21日",
        "edate":"2022年2月13日",
        "department":"后勤部",
        "position":"大茶壶",
        "company":"重庆怡红院高级会所"
    }
]

# 对列表进行循环遍历,批量生成word文件
for person in person_list:
    # print(person)
    # 读取离职证明模板文件
    doc = Document(r"C:\python基础\26-python办公自动化-操作word\resources\离职证明模板.docx")
    # 循环遍历模板文件中所有的段落,查找占位符
    for p in doc.paragraphs:
        # print(p.text)
        if "{" not in p.text:
            continue
        # 不能直接修改段落内容,否则会丢失样式,所以需要对段落中的元素进行遍历并进行查找和替换
        for run in p.runs:
            # print(run.text)
            if '{' not in run.text:
                continue
            # 找到占位符的开始位置{ 和结束位置 }  进行内容替换
            start,end = run.text.find("{"),run.text.find("}")
            # print(start,end)
            key,place_holder = run.text[start+1:end],run.text[start:end+1]
            # print(key,place_holder)  # key === >name   place_holder  ==== > {name}

            run.text = run.text.replace(place_holder,person[key])
            # print(run.text)

    # 每个人的信息保存一个word文档
    doc.save(f"{person['name']}的离职证明.docx")
