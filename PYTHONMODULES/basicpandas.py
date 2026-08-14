import pandas as pd

# 1. Import Pandas and check version
print("1. Pandas Version:")
print(pd.__version__)

# 2. Create a Pandas Series from a list
print("\n2. Series from List:")
marks = pd.Series([85, 90, 78, 92, 88])
print(marks)

# 3. Create a Series from a dictionary
print("\n3. Series from Dictionary:")
student_marks = pd.Series({
    "Vaishnavi": 85,
    "Rahul": 90,
    "Sneha": 78,
    "Amit": 92
})
print(student_marks)

# 4. Create a Series with custom indexes
print("\n4. Series with Custom Index:")
subject_marks = pd.Series(
    [85, 90, 78, 92],
    index=["Maths", "Python", "SQL", "AI"]
)
print(subject_marks)

# 5. Create a DataFrame from a dictionary
print("\n5. DataFrame from Dictionary:")
data = {
    "Name": ["Vaishnavi", "Rahul", "Sneha", "Amit", "Priya", "Rohan", "Neha"],
    "Age": [21, 22, 20, 23, 21, 22, 20],
    "Marks": [85, 90, 78, 92, 88, 95, 79]
}
df = pd.DataFrame(data)
print(df)

# 6. Create a DataFrame from a list of dictionaries
print("\n6. DataFrame from List of Dictionaries:")
students = [
    {"Name": "Vaishnavi", "Age": 21, "Marks": 85},
    {"Name": "Rahul", "Age": 22, "Marks": 90},
    {"Name": "Sneha", "Age": 20, "Marks": 78}
]
df_students = pd.DataFrame(students)
print(df_students)

# 7. Display first 5 and last 5 rows
print("\n7. First 5 Rows:")
print(df.head())
print("\nLast 5 Rows:")
print(df.tail())
print(df)#header first 5 rows and last 5 rows

# 8. Check shape, columns, index and data types
print("\n8. DataFrame Information:")
print("Shape:", df.shape)
print("Columns:", df.columns)
print("Index:", df.index)
print("\nData Types:")
print(df.dtypes)

# 9. Use info() and describe()
print("\n9. DataFrame Info:")
df.info()
print("\nStatistical Description:")
print(df.describe())

# 10. Select single and multiple columns
print("\n10. Single Column:")
print(df["Name"])
print("\nMultiple Columns:")
print(df[["Name", "Marks"]])

# DATA SELECTION & MANIPULATION

# 11. Select rows using loc[]
print("\n11. Using loc[]:")
print(df.loc[0])
print("\nFirst 3 Rows:")
print(df.loc[0:2])

# 12. Select rows and columns using iloc[]
print("\n12. Using iloc[]:")
print(df.iloc[0:3, 0:2])

# 13. Filter rows using a single condition
print("\n13. Marks Greater Than 80:")
result = df[df["Marks"] > 80]
print(result)

# 14. Filter using multiple conditions
print("\n14. Marks Between 80 and 90:")
result = df[
    (df["Marks"] > 80) &
    (df["Marks"] < 90)
]
print(result)

# 15. Add a new column
print("\n15. Add Status Column:")
df["Status"] = [
    "Pass",
    "Pass",
    "Pass",
    "Pass",
    "Pass",
    "Pass",
    "Pass"
]
print(df)

# 16. Modify values in an existing column
print("\n16. Add 5 Marks:")
df["Marks"] = df["Marks"] + 5
print(df)

# 17. Delete a column
print("\n17. Delete Status Column:")
df = df.drop("Status", axis=1)
print(df)

# 18. Rename columns
print("\n18. Rename Columns:")
df = df.rename(columns={
    "Name": "Student_Name",
    "Marks": "Score"
})
print(df)

# 19. Sort DataFrame
print("\n19. Sort by Score - Ascending:")
print(df.sort_values("Score"))
print("\nSort by Score - Descending:")
print(df.sort_values("Score", ascending=False))

# 20. Set and reset index
print("\n20. Set Index:")
df = df.set_index("Student_Name")
print(df)
print("\nReset Index:")
df = df.reset_index()
print(df)

