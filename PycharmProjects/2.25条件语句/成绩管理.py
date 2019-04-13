grade = input("请输入成绩：")
while True:
    if not grade.isdigit():
        grade = input("成绩输入错误，请重新输入：")
        continue
    break
grade = int(grade)
if grade > 90:
    print(f"成绩为{grade}分，优秀。")
elif grade > 80:
    print(f"成绩为{grade}分，优良。")
elif grade >= 60:
    print(f"成绩为{grade}分，及格。")
else:
    print(f"成绩为{grade}分，不及格。")

