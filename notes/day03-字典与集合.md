# Day 03 · 字典与集合（学习卡片）

**日期：2026-10-23**

## 一、字典 dict

键值对，用一个标签（键）取一个值。**JSON 就是字典。**

```python
student = {"name": "刘煜贤", "age": 22, "city": "赣州"}

student["name"]           # 取值 → 刘煜贤
student.get("phone", "没填")  # 取不到给默认值，不报错
student["goal"] = "深圳"   # 新增
student["age"] = 23        # 修改
del student["city"]        # 删除
len(student)               # 有几个键值对
"name" in student          # True
```

**注意**：`student["phone"]` 取不存在的键会 `KeyError`；`.get()` 不会。

遍历：

```python
for key in student:                 # 只拿键
for key, value in student.items():  # 同时拿键和值（最常用）
```

## 二、集合 set

无序、不重复、判断"在不在"特别快。

```python
s = {1, 2, 2, 3}       # {1, 2, 3}
set([78, 92, 78])      # {78, 92}   去重
92 in s                # 判断，比列表快
a & b                  # 交集
a | b                  # 并集
a - b                  # 差集
```

## 三、字典排序（重要）

```python
sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
```

`lambda kv: kv[1]` = "排序时看第 2 个元素（次数）"。

## 四、和 AI 的关系

- 调大模型 API，返回的是 JSON → 解析后就是字典
- 请求参数也是字典 → `{"messages": [...], "model": "..."}`
- 做 RAG 时的文档元数据、检索结果，都是字典

**字典不熟，AI 接口就没法调。**

## 今天要交的作业

- `code/day03/01_dict.py` — 4 个 TODO
- `code/day03/02_set.py` — 3 个 TODO
- `code/day03/03_homework.py` — 4 个 TODO（词频统计）

## 自查标准

1. 三个文件都能跑，不报错
2. 能不看资料说出：`[]` 和 `.get()` 的区别
3. 能说出：什么时候用列表、什么时候用字典、什么时候用集合

## 明天计划

文件读写 + JSON 存取 → 把词频统计结果写进文件
