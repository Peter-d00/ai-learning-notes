"""Day 01 · 环境自检脚本

运行方式：
    python code/day01/env_check.py

这个脚本不做复杂的事，只做三件事：
1. 打印当前 Python 环境和解释器路径
2. 用几个基础语法（列表、函数、f-string）做一次自检
3. 打上今天的日期，作为学习记录
"""

import platform
import sys
from datetime import datetime


def line(title: str) -> None:
    """打印一个带下划线的小标题。"""
    print(f"\n{title}")
    print("-" * 40)


def average(values: list[int]) -> float:
    """计算平均值。"""
    return sum(values) / len(values)


line("1. Python 环境")
print(f"版本   : {sys.version.split()[0]}")
print(f"解释器 : {sys.executable}")
print(f"系统   : {platform.system()} {platform.release()}")

line("2. 基础语法自检")
numbers = [3, 8, 15, 22, 7]
print(f"列表   : {numbers}")
print(f"总和   : {sum(numbers)}")
print(f"最大值 : {max(numbers)}")
print(f"平均值 : {average(numbers):.2f}")

line("3. 打卡")
today = datetime.now().strftime("%Y-%m-%d")
print(f"日期   : {today}")
print("状态   : 环境就绪，可以开始写代码了")
