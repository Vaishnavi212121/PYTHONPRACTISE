import matplotlib.pyplot as plt
import pandas as pd

# 1. Simple line plot
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]
plt.plot(x, y)
plt.show()

# 2. Line plot with title and labels
plt.plot(x, y)
plt.title("Sales Report")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.show()

# 3. Line style
plt.plot(x, y, linestyle="--")
plt.title("Sales")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.show()

# 4. Markers
plt.plot(x, y, marker="o")
plt.title("Sales with Markers")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.show()


# 5. Grid
plt.plot(x, y, marker="o")
plt.title("Sales")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.grid()
plt.show()

# 6. Multiple lines
months = [1, 2, 3, 4, 5]
sales_2025 = [20, 30, 25, 40, 50]
sales_2026 = [25, 35, 30, 45, 60]
plt.plot(months, sales_2025, marker="o", label="2025")
plt.plot(months, sales_2026, marker="s", label="2026")
plt.title("Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid()
plt.show()


# 7. Customized line plot

plt.plot(
    x,
    y,
    marker="o",
    linestyle="--",
    linewidth=2,
    markersize=8
)

plt.title("Customized Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid()

plt.show()


# 8. Scatter plot

hours = [1, 2, 3, 4, 5, 6, 7, 8]
marks = [35, 40, 50, 55, 65, 70, 80, 90]

plt.scatter(hours, marks)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()


# 9. Bar chart

subjects = ["Python", "SQL", "AI", "ML", "DL"]
marks = [85, 90, 80, 88, 92]

plt.bar(subjects, marks)

plt.title("Subject Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()


# 10. Horizontal bar chart

plt.barh(subjects, marks)

plt.title("Subject Marks")
plt.xlabel("Marks")
plt.ylabel("Subjects")

plt.show()


# 11. Histogram

student_marks = [
    45, 50, 55, 60, 62, 65, 68, 70,
    72, 75, 78, 80, 82, 85, 88, 90,
    92, 95, 98
]

plt.hist(student_marks, bins=5)

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()


# 12. Pie chart

departments = ["AIML", "CSE", "ECE", "IT"]
students = [40, 35, 20, 25]

plt.pie(
    students,
    labels=departments,
    autopct="%1.1f%%"
)

plt.title("Students by Department")

plt.show()


# 13. Subplots

plt.subplot(1, 2, 1)

plt.plot(x, y)
plt.title("Line Plot")

plt.subplot(1, 2, 2)

plt.bar(x, y)
plt.title("Bar Chart")

plt.show()


# 14. Four subplots

plt.subplot(2, 2, 1)

plt.plot(x, y)
plt.title("Line")

plt.subplot(2, 2, 2)

plt.scatter(x, y)
plt.title("Scatter")

plt.subplot(2, 2, 3)

plt.bar(x, y)
plt.title("Bar")

plt.subplot(2, 2, 4)

plt.hist(y)
plt.title("Histogram")

plt.tight_layout()

plt.show()


# 15. Legend

python_marks = [70, 75, 80, 85, 90]
sql_marks = [65, 72, 78, 84, 88]

plt.plot(
    x,
    python_marks,
    marker="o",
    label="Python"
)

plt.plot(
    x,
    sql_marks,
    marker="s",
    label="SQL"
)

plt.title("Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.legend()
plt.grid()

plt.show()


