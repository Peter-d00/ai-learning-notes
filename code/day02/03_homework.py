# ============================================================
# Day 02 · 综合练习：班级成绩统计
# ------------------------------------------------------------
# 把今天学的"变量 + 列表 + for 循环"全部用一遍。
# 目标：不查教程，自己把 5 个 TODO 写完。
# 运行：python code/day02/03_homework.py
# ============================================================

scores = [78, 92, 65, 88, 59, 100, 73, 85, 91, 60]


# ---------- TODO 1：平均分（保留 1 位小数）----------
# 提示：sum(scores) / len(scores)，f-string 里用 :.1f 保留一位小数

# 在这里写
# 一行版
print(f"平均分：{sum(scores) / len(scores):.1f}")

# 两步版（推荐，好读也好调试）
avg = sum(scores) / len(scores)
print(f"平均分：{avg:.1f}")

# ---------- TODO 2：最高分和最低分 ----------
# 提示：max() / min()
print(max(scores))
print(min(scores))
# 在这里写


# ---------- TODO 3：及格人数与及格率 ----------
# 提示：先 number = 0，然后用 for 循环遍历，
#       遇到 >= 60 的就 number += 1
#       及格率 = 及格人数 / 总人数 * 100

# 在这里写
number = 0
for s in scores:
    if s >= 60:
        number += 1

print(f"及格人数：{number}")
print(f"及格率：{number / len(scores) * 100:.1f}%")


# ---------- TODO 4：从高到低排序后打印 ----------
# 提示：sorted(scores, reverse=True)

# 在这里写
print(sorted(scores, reverse=True))

# ---------- TODO 5（进阶）：分数分档统计 ----------
# 优（>=90）、良（80-89）、中（70-79）、及格（60-69）、不及格（<60）
# 提示：用 if / elif / else 判断，每档先定义计数变量 = 0

# 在这里写
excellent = good = medium = passed = failed = 0

for s in scores:
    if s >= 90:
        excellent += 1
    elif s >= 80:
        good += 1
    elif s >= 70:
        medium += 1
    elif s >= 60:
        passed += 1
    else:
        failed += 1

print(f"优（>=90）  : {excellent}")
print(f"良（80-89） : {good}")
print(f"中（70-79） : {medium}")
print(f"及格（60-69）: {passed}")
print(f"不及格（<60）: {failed}")