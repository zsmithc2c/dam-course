import json, os

def make_nb(cells):
    return {
        "nbformat": 4, "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.10.0"}
        },
        "cells": cells
    }
def md(id, src):
    return {"cell_type": "markdown", "id": id, "metadata": {}, "source": src}
def code(id, src):
    return {"cell_type": "code", "id": id, "metadata": {}, "source": src, "outputs": [], "execution_count": None}

BASE = "https://raw.githubusercontent.com/zsmithc2c/dam-course/main/datasets"

# ── L04: Arrays vs DataFrames ──
cells_04 = [
    md("cell-001", [
        "# DAM - Lesson 4: Arrays vs. DataFrames\n",
        "**Code2College | Data Analysis & Management**\n",
        "\n",
        "Estimated time: 110 minutes\n",
        "\n",
        "In this notebook, you'll compare NumPy arrays and Pandas DataFrames — two powerful tools for working with data."
    ]),
    md("cell-002", [
        "## Learning Objectives\n",
        "\n",
        "By the end of this lesson, you will be able to:\n",
        "- Create a Pandas DataFrame from a Python dictionary\n",
        "- Create a Pandas DataFrame from a NumPy array\n",
        "- Use `.loc[]` (label-based) and `.iloc[]` (position-based) to access data\n",
        "- Perform basic `groupby()` aggregation\n",
        "- Compare array operations to DataFrame operations"
    ]),
    code("cell-003", [
        "# Setup: Import libraries and load data\n",
        "import numpy as np\n",
        "import pandas as pd\n",
        "\n",
        f"df = pd.read_csv('{BASE}/phase_1/employee_data.csv')\n",
        "print(f\"Loaded {len(df)} rows\")\n",
        "df.head()"
    ]),
    md("cell-004", [
        "## Exercise 1: Create a DataFrame from a Dictionary\n",
        "\n",
        "Dictionaries map column names to lists of values — a natural way to build a DataFrame."
    ]),
    code("cell-005", [
        "# Exercise 1: Create a DataFrame from a dictionary\n",
        "# Create a DataFrame with these columns:\n",
        "#   'name': ['Alice', 'Bob', 'Charlie', 'Diana']\n",
        "#   'age': [25, 30, 35, 28]\n",
        "#   'department': ['Engineering', 'Marketing', 'Engineering', 'Sales']\n",
        "#   'salary': [75000, 65000, 80000, 70000]\n",
        "\n",
        "# TODO: your code here\n",
        "data = {\n",
        "    # Fill in the dictionary\n",
        "}\n",
        "my_df = pd.DataFrame(data)\n",
        "print(my_df)\n",
        "\n",
        "# ANSWER:\n",
        "# data = {\n",
        "#     'name': ['Alice', 'Bob', 'Charlie', 'Diana'],\n",
        "#     'age': [25, 30, 35, 28],\n",
        "#     'department': ['Engineering', 'Marketing', 'Engineering', 'Sales'],\n",
        "#     'salary': [75000, 65000, 80000, 70000]\n",
        "# }\n",
        "# my_df = pd.DataFrame(data)"
    ]),
    md("cell-006", [
        "## Exercise 2: Create a DataFrame from a NumPy Array\n",
        "\n",
        "You can convert a NumPy array into a DataFrame by adding column names."
    ]),
    code("cell-007", [
        "# Exercise 2: Convert a NumPy array to a DataFrame\n",
        "# Given this 2D array of student test scores:\n",
        "scores_array = np.array([\n",
        "    [85, 90, 78],\n",
        "    [92, 88, 95],\n",
        "    [73, 80, 85],\n",
        "    [90, 85, 92]\n",
        "])\n",
        "\n",
        "# TODO: Create a DataFrame with columns: 'Test_1', 'Test_2', 'Test_3'\n",
        "scores_df = \n",
        "print(scores_df)\n",
        "\n",
        "# TODO: Add a 'Student' column with names: ['Maria', 'James', 'Aisha', 'Carlos']\n",
        "\n",
        "print(scores_df)\n",
        "\n",
        "# ANSWER:\n",
        "# scores_df = pd.DataFrame(scores_array, columns=['Test_1', 'Test_2', 'Test_3'])\n",
        "# scores_df['Student'] = ['Maria', 'James', 'Aisha', 'Carlos']"
    ]),
    md("cell-008", [
        "## Exercise 3: `.loc[]` vs `.iloc[]`\n",
        "\n",
        "- `.loc[]` — selects by **label** (column name, row label)\n",
        "- `.iloc[]` — selects by **integer position** (row number, column number)"
    ]),
    code("cell-009", [
        "# Exercise 3: Practice .loc[] and .iloc[]\n",
        "# Using the employee DataFrame loaded at the top:\n",
        "print(df.head())\n",
        "print()\n",
        "\n",
        "# Task 1: Use .iloc[] to get the first 3 rows\n",
        "# TODO: your code here\n",
        "first_three = \n",
        "print(\"First 3 rows (iloc):\")\n",
        "print(first_three)\n",
        "print()\n",
        "\n",
        "# Task 2: Use .loc[] to get all rows where department is 'Engineering'\n",
        "# Hint: .loc[condition]\n",
        "# TODO: your code here\n",
        "engineering = \n",
        "print(\"Engineering department (loc):\")\n",
        "print(engineering)\n",
        "print()\n",
        "\n",
        "# Task 3: Use .iloc[] to get row 2, columns 0 through 2\n",
        "# TODO: your code here\n",
        "subset = \n",
        "print(\"Row 2, first 3 columns (iloc):\")\n",
        "print(subset)\n",
        "\n",
        "# ANSWER:\n",
        "# first_three = df.iloc[:3]\n",
        "# engineering = df.loc[df['department'] == 'Engineering']\n",
        "# subset = df.iloc[2, 0:3]"
    ]),
    md("cell-010", [
        "## Exercise 4: Basic GroupBy\n",
        "\n",
        "`groupby()` groups rows by a column, then applies an aggregate function (mean, sum, count, etc.)."
    ]),
    code("cell-011", [
        "# Exercise 4: GroupBy operations\n",
        "# Using the employee DataFrame:\n",
        "\n",
        "# Task 1: Find the average salary by department\n",
        "# TODO: your code here\n",
        "avg_by_dept = \n",
        "print(\"Average salary by department:\")\n",
        "print(avg_by_dept)\n",
        "print()\n",
        "\n",
        "# Task 2: Count the number of employees in each department\n",
        "# TODO: your code here\n",
        "count_by_dept = \n",
        "print(\"Employee count by department:\")\n",
        "print(count_by_dept)\n",
        "print()\n",
        "\n",
        "# Task 3: Find the max salary in each department\n",
        "# TODO: your code here\n",
        "max_by_dept = \n",
        "print(\"Max salary by department:\")\n",
        "print(max_by_dept)\n",
        "\n",
        "# ANSWER:\n",
        "# avg_by_dept = df.groupby('department')['salary'].mean()\n",
        "# count_by_dept = df.groupby('department')['name'].count()\n",
        "# max_by_dept = df.groupby('department')['salary'].max()"
    ]),
    md("cell-012", [
        "## Exercise 5: Arrays vs DataFrames — Side by Side\n",
        "\n",
        "Let's do the same operation with both a NumPy array and a Pandas DataFrame to see the differences."
    ]),
    code("cell-013", [
        "# Exercise 5: Compare array and DataFrame operations\n",
        "\n",
        "# NumPy approach: calculate mean salary\n",
        "salary_array = np.array([75000, 65000, 80000, 70000, 90000, 60000])\n",
        "numpy_mean = np.mean(salary_array)\n",
        "print(f\"NumPy mean salary: ${numpy_mean:,.0f}\")\n",
        "\n",
        "# NumPy approach: filter salaries above 70000\n",
        "high_salaries_np = salary_array[salary_array > 70000]\n",
        "print(f\"NumPy high salaries: {high_salaries_np}\")\n",
        "print()\n",
        "\n",
        "# TODO: Pandas approach - calculate mean salary using the employee df\n",
        "pandas_mean = \n",
        "print(f\"Pandas mean salary: ${pandas_mean:,.0f}\")\n",
        "\n",
        "# TODO: Pandas approach - filter rows where salary > 70000\n",
        "high_salaries_pd = \n",
        "print(\"Pandas high salary employees:\")\n",
        "print(high_salaries_pd)\n",
        "\n",
        "# ANSWER:\n",
        "# pandas_mean = df['salary'].mean()\n",
        "# high_salaries_pd = df[df['salary'] > 70000]"
    ]),
    md("cell-014", [
        "## Submission\n",
        "\n",
        "Nice work comparing arrays and DataFrames! To get credit:\n",
        "\n",
        "1. Make sure all 5 exercises above are completed\n",
        "2. Save this notebook (File > Save a copy in Drive)\n",
        "3. Return to **HireWheel** and paste your notebook URL\n",
        "4. Answer the exit ticket questions on the lesson page"
    ])
]

# ── L05: Working with DataFrames ──
cells_05 = [
    md("cell-001", [
        "# DAM - Lesson 5: Working with DataFrames\n",
        "**Code2College | Data Analysis & Management**\n",
        "\n",
        "Estimated time: 120 minutes\n",
        "\n",
        "This is your deep dive into Pandas DataFrames. You'll load multiple datasets and use the essential exploration tools."
    ]),
    md("cell-002", [
        "## Learning Objectives\n",
        "\n",
        "By the end of this lesson, you will be able to:\n",
        "- Load CSV files from URLs using `pd.read_csv()`\n",
        "- Inspect DataFrames with `.shape`, `.columns`, `.dtypes`\n",
        "- Generate summary statistics with `.describe()` and interpret each row\n",
        "- Use `.info()` to check data types and missing values\n",
        "- Analyze categorical data with `.value_counts()`\n",
        "- Sort data with `.sort_values()`\n",
        "- Filter rows with boolean indexing"
    ]),
    code("cell-003", [
        "# Setup: Import Pandas and Matplotlib\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "# Load the first dataset: Employee Data\n",
        f"df_emp = pd.read_csv('{BASE}/phase_1/employee_data.csv')\n",
        "print(f\"Employee data: {df_emp.shape[0]} rows, {df_emp.shape[1]} columns\")\n",
        "df_emp.head()"
    ]),
    md("cell-004", [
        "## Exercise 1: `.shape`, `.columns`, `.dtypes`\n",
        "\n",
        "These three attributes give you a quick snapshot of any DataFrame."
    ]),
    code("cell-005", [
        "# Exercise 1: Explore the employee DataFrame\n",
        "\n",
        "# Task 1: Print the shape (rows, columns)\n",
        "# TODO: your code here\n",
        "print(\"Shape:\", )\n",
        "\n",
        "# Task 2: Print all column names\n",
        "# TODO: your code here\n",
        "print(\"Columns:\", )\n",
        "\n",
        "# Task 3: Print the data type of each column\n",
        "# TODO: your code here\n",
        "print(\"Data types:\")\n",
        "print()\n",
        "\n",
        "# ANSWER:\n",
        "# print(\"Shape:\", df_emp.shape)\n",
        "# print(\"Columns:\", df_emp.columns.tolist())\n",
        "# print(\"Data types:\")\n",
        "# print(df_emp.dtypes)"
    ]),
    md("cell-006", [
        "## Exercise 2: `.describe()` — Summary Statistics\n",
        "\n",
        "`.describe()` gives you count, mean, std, min, 25%, 50%, 75%, max for every numeric column.\n",
        "\n",
        "- **count**: number of non-null values\n",
        "- **mean**: average value\n",
        "- **std**: standard deviation (spread)\n",
        "- **min/max**: smallest/largest values\n",
        "- **25%/50%/75%**: quartiles (50% = median)"
    ]),
    code("cell-007", [
        "# Exercise 2: Use .describe() and interpret the output\n",
        "\n",
        "# Task 1: Run describe() on the employee DataFrame\n",
        "# TODO: your code here\n",
        "\n",
        "\n",
        "# Task 2: Answer these questions in comments:\n",
        "# What is the average salary? \n",
        "# What is the salary range (max - min)?\n",
        "# What does the 50% (median) tell you compared to the mean?\n",
        "\n",
        "# TODO: Write your answers as comments\n",
        "# Average salary: $___\n",
        "# Salary range: $___\n",
        "# Median vs mean tells me: ___\n",
        "\n",
        "# ANSWER:\n",
        "# df_emp.describe()\n",
        "# Answers will vary based on dataset values"
    ]),
    md("cell-008", [
        "## Exercise 3: `.info()`\n",
        "\n",
        "`.info()` shows data types, non-null counts, and memory usage — great for spotting missing data."
    ]),
    code("cell-009", [
        "# Exercise 3: Use .info()\n",
        "\n",
        "# TODO: Run .info() on the employee DataFrame\n",
        "\n",
        "\n",
        "# Answer in comments:\n",
        "# Are there any columns with missing values? Which ones?\n",
        "# TODO: your answer\n",
        "\n",
        "# ANSWER:\n",
        "# df_emp.info()"
    ]),
    md("cell-010", [
        "## Exercise 4: `.value_counts()`\n",
        "\n",
        "`.value_counts()` counts how often each unique value appears in a column. Perfect for categorical data."
    ]),
    code("cell-011", [
        "# Exercise 4: value_counts on categorical columns\n",
        "\n",
        "# Task 1: Count how many employees are in each department\n",
        "# TODO: your code here\n",
        "dept_counts = \n",
        "print(\"Department counts:\")\n",
        "print(dept_counts)\n",
        "print()\n",
        "\n",
        "# Task 2: If there's a 'gender' or 'role' column, count those values too\n",
        "# TODO: your code here (pick any categorical column)\n",
        "\n",
        "\n",
        "# ANSWER:\n",
        "# dept_counts = df_emp['department'].value_counts()\n",
        "# print(dept_counts)"
    ]),
    md("cell-012", [
        "## Exercise 5: `.sort_values()`\n",
        "\n",
        "Sort your data by any column, ascending or descending."
    ]),
    code("cell-013", [
        "# Exercise 5: Sorting\n",
        "\n",
        "# Task 1: Sort employees by salary (highest first)\n",
        "# TODO: your code here\n",
        "sorted_df = \n",
        "print(\"Top earners:\")\n",
        "print(sorted_df.head())\n",
        "print()\n",
        "\n",
        "# Task 2: Sort employees by name (alphabetical)\n",
        "# TODO: your code here\n",
        "alpha_df = \n",
        "print(\"Alphabetical:\")\n",
        "print(alpha_df.head())\n",
        "\n",
        "# ANSWER:\n",
        "# sorted_df = df_emp.sort_values('salary', ascending=False)\n",
        "# alpha_df = df_emp.sort_values('name')"
    ]),
    md("cell-014", [
        "## Loading a Second Dataset: Student Grades\n",
        "\n",
        "Now let's practice with a different dataset to reinforce these skills."
    ]),
    code("cell-015", [
        "# Load the student grades dataset\n",
        f"df_grades = pd.read_csv('{BASE}/phase_1/student_grades.csv')\n",
        "print(f\"Student grades: {df_grades.shape[0]} rows, {df_grades.shape[1]} columns\")\n",
        "df_grades.head(10)"
    ]),
    md("cell-016", [
        "## Exercise 6: `.head()` and Filtering\n",
        "\n",
        "Use `.head(n)` to preview data and boolean indexing to filter rows."
    ]),
    code("cell-017", [
        "# Exercise 6: Preview and filter student grades\n",
        "\n",
        "# Task 1: Show the first 10 rows\n",
        "# TODO: your code here\n",
        "\n",
        "\n",
        "# Task 2: Filter students with a grade above 90\n",
        "# TODO: your code here\n",
        "high_achievers = \n",
        "print(\"High achievers (>90):\")\n",
        "print(high_achievers)\n",
        "\n",
        "# ANSWER:\n",
        "# df_grades.head(10)\n",
        "# high_achievers = df_grades[df_grades['grade'] > 90]"
    ]),
    md("cell-018", [
        "## Loading a Third Dataset: Country Stats\n",
        "\n",
        "One more dataset to practice the full exploration workflow."
    ]),
    code("cell-019", [
        "# Load the country stats dataset\n",
        f"df_countries = pd.read_csv('{BASE}/phase_1/country_stats.csv')\n",
        "print(f\"Country stats: {df_countries.shape[0]} rows, {df_countries.shape[1]} columns\")\n",
        "df_countries.head()"
    ]),
    md("cell-020", [
        "## Exercise 7: Full Exploration Challenge\n",
        "\n",
        "Apply everything you've learned to explore the country stats dataset."
    ]),
    code("cell-021", [
        "# Exercise 7: Explore country stats (apply all techniques!)\n",
        "\n",
        "# Task 1: Check the shape, columns, and dtypes\n",
        "# TODO: your code here\n",
        "\n",
        "\n",
        "# Task 2: Run .describe() — what is the mean population?\n",
        "# TODO: your code here\n",
        "\n",
        "\n",
        "# Task 3: Sort by population (largest first) — which country is #1?\n",
        "# TODO: your code here\n",
        "\n",
        "\n",
        "# Task 4: Filter countries with GDP above the median\n",
        "# Hint: use df['col'].median() to get the median\n",
        "# TODO: your code here\n",
        "\n",
        "\n",
        "# ANSWER:\n",
        "# print(df_countries.shape)\n",
        "# print(df_countries.columns.tolist())\n",
        "# print(df_countries.dtypes)\n",
        "# df_countries.describe()\n",
        "# df_countries.sort_values('population', ascending=False)\n",
        "# median_gdp = df_countries['gdp'].median()\n",
        "# df_countries[df_countries['gdp'] > median_gdp]"
    ]),
    md("cell-022", [
        "## Submission\n",
        "\n",
        "Excellent work exploring three different datasets! To get credit:\n",
        "\n",
        "1. Make sure all 7 exercises above are completed\n",
        "2. Save this notebook (File > Save a copy in Drive)\n",
        "3. Return to **HireWheel** and paste your notebook URL\n",
        "4. Answer the exit ticket questions on the lesson page"
    ])
]

os.makedirs("/tmp/dam-build/notebooks/phase_1", exist_ok=True)
with open("/tmp/dam-build/notebooks/phase_1/DAM_Lesson_04_Arrays_vs_DataFrames.ipynb", "w") as f:
    json.dump(make_nb(cells_04), f, indent=1)
with open("/tmp/dam-build/notebooks/phase_1/DAM_Lesson_05_Working_with_DataFrames.ipynb", "w") as f:
    json.dump(make_nb(cells_05), f, indent=1)
print("L04 and L05 written.")
