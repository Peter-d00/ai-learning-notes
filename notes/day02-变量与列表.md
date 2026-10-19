# Day 02 · 变量与列表（学习卡片）

**日期：2026-10-19**

## 一、变量

变量 = 贴了标签的盒子。赋值那一刻类型就确定。

```python
name = "刘煜贤"    # str   字符串
age = 22           # int   整数
height = 1.75      # float 小数
is_learning = True # bool  布尔值
```

查类型：`type(age)` → `<class 'int'>`

## 二、f-string（最常用的输出方式）

```python
print(f"{name} 今年 {age} 岁")
print(f"平均分：{avg:.1f}")    # .1f 表示保留 1 位小数
```

## 三、类型转换

| 写法 | 作用 |
| --- | --- |
| `int("18")` | 字符串 → 整数 |
| `float("3.5")` | 字符串 → 小数 |
| `str(18)` | 数字 → 字符串 |

## 四、字符串常用操作

```python
s = "  Python 很好用  "
s.strip()          # 去掉首尾空格
s.split(" ")       # 按空格切成列表
len(s)             # 长度
s[0:6]             # 切片，取前 6 个字符
```

## 五、列表

```python
scores = [78, 92, 65, 88, 59]
scores[0]        # 78，第一个（索引从 0 开始）
scores[-1]       # 59，最后一个
scores[1:3]      # [92, 65]，切片
scores.append(100)   # 末尾追加
scores.remove(59)    # 删除某个值
scores[0] = 80       # 修改
len / sum / max / min   # 常用内置函数
sorted(scores, reverse=True)  # 从大到小
```

## 六、for 循环

```python
for s in scores:
    print(s)
```

**注意**：Python 靠缩进划范围，冒号下面缩进的行属于循环体。

## 今天要交的作业

- `code/day02/01_variables.py` — 3 个 TODO
- `code/day02/02_lists.py` — 4 个 TODO
- `code/day02/03_homework.py` — 5 个 TODO

## 自查标准

1. 每个文件能正常运行，没有红色报错
2. 输出结果和你的预期一致
3. 不看教程能说出：变量是什么、列表怎么取值、for 循环怎么用

## 明天计划

字典（dict）与集合（set）→ 条件判断（if / elif / else）→ 综合练习
