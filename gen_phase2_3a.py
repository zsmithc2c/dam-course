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

# ── L09: SQL Mini-Project Pokemon ──
cells_09 = [
    md("cell-001", [
        "# DAM - Lesson 9: SQL Mini-Project -- Pokemon Dataset\n",
        "**Code2College | Data Analysis & Management**\n",
        "\n",
        "Estimated time: 130 minutes\n",
        "\n",
        "Time to put your SQL skills to the test! You'll query a real Pokemon dataset with 12 challenges of increasing difficulty."
    ]),
    md("cell-002", [
        "## Learning Objectives\n",
        "\n",
        "By the end of this lesson, you will be able to:\n",
        "- Load a CSV dataset into an SQLite database using Pandas\n",
        "- Write SELECT queries with WHERE, ORDER BY, and LIMIT\n",
        "- Use GROUP BY with aggregate functions (COUNT, AVG, MAX)\n",
        "- Write subqueries to filter based on computed values\n",
        "- Combine multiple conditions in complex WHERE clauses"
    ]),
    code("cell-003", [
        "# Setup: Import libraries and load Pokemon data into SQLite\n",
        "import sqlite3\n",
        "import pandas as pd\n",
        "\n",
        "# Load the Pokemon CSV\n",
        f"df = pd.read_csv('{BASE}/phase_2/pokemon.csv')\n",
        "print(f\"Loaded {len(df)} Pokemon\")\n",
        "\n",
        "# Create an in-memory SQLite database and load the data\n",
        "conn = sqlite3.connect(':memory:')\n",
        "df.to_sql('pokemon', conn, if_exists='replace', index=False)\n",
        "\n",
        "# Helper function to run SQL queries\n",
        "def run_sql(query):\n",
        "    return pd.read_sql(query, conn)\n",
        "\n",
        "# Preview the data\n",
        "run_sql('SELECT * FROM pokemon LIMIT 5')"
    ]),
    code("cell-004", [
        "# See all column names and their types\n",
        "run_sql(\"PRAGMA table_info(pokemon)\")"
    ]),
    md("cell-005", [
        "---\n",
        "## Easy Challenges (1-4)\n",
        "\n",
        "### Challenge 1: SELECT All Pokemon\n",
        "Write a query to select ALL columns from the pokemon table. How many rows are there?"
    ]),
    code("cell-006", [
        "# Challenge 1: SELECT all Pokemon\n",
        "# YOUR SQL QUERY HERE\n",
        "query_1 = \"\"\"\n",
        "\n",
        "\"\"\"\n",
        "result_1 = run_sql(query_1)\n",
        "print(f\"Total Pokemon: {len(result_1)}\")\n",
        "result_1.head(10)\n",
        "\n",
        "# ANSWER: SELECT * FROM pokemon"
    ]),
    md("cell-007", [
        "### Challenge 2: Fire-Type Pokemon\n",
        "Select all Pokemon where `type1` is 'Fire'. Show their name, type1, and attack."
    ]),
    code("cell-008", [
        "# Challenge 2: Fire-type Pokemon\n",
        "# YOUR SQL QUERY HERE\n",
        "query_2 = \"\"\"\n",
        "\n",
        "\"\"\"\n",
        "run_sql(query_2)\n",
        "\n",
        "# ANSWER: SELECT name, type1, attack FROM pokemon WHERE type1 = 'Fire'"
    ]),
    md("cell-009", [
        "### Challenge 3: Strongest Attackers\n",
        "Select name and attack for all Pokemon, sorted by attack from highest to lowest. Show the top 10."
    ]),
    code("cell-010", [
        "# Challenge 3: Top 10 attackers\n",
        "# YOUR SQL QUERY HERE\n",
        "query_3 = \"\"\"\n",
        "\n",
        "\"\"\"\n",
        "run_sql(query_3)\n",
        "\n",
        "# ANSWER: SELECT name, attack FROM pokemon ORDER BY attack DESC LIMIT 10"
    ]),
    md("cell-011", [
        "### Challenge 4: Fast Pokemon\n",
        "Find all Pokemon with speed greater than 100. Show their name, type1, and speed, sorted by speed descending."
    ]),
    code("cell-012", [
        "# Challenge 4: Fast Pokemon\n",
        "# YOUR SQL QUERY HERE\n",
        "query_4 = \"\"\"\n",
        "\n",
        "\"\"\"\n",
        "run_sql(query_4)\n",
        "\n",
        "# ANSWER: SELECT name, type1, speed FROM pokemon WHERE speed > 100 ORDER BY speed DESC"
    ]),
    md("cell-013", [
        "---\n",
        "## Medium Challenges (5-8)\n",
        "\n",
        "### Challenge 5: Pokemon Count by Type\n",
        "Use GROUP BY to count how many Pokemon belong to each primary type (`type1`). Order by count descending."
    ]),
    code("cell-014", [
        "# Challenge 5: Count by type\n",
        "# YOUR SQL QUERY HERE\n",
        "query_5 = \"\"\"\n",
        "\n",
        "\"\"\"\n",
        "run_sql(query_5)\n",
        "\n",
        "# ANSWER: SELECT type1, COUNT(*) AS count FROM pokemon GROUP BY type1 ORDER BY count DESC"
    ]),
    md("cell-015", [
        "### Challenge 6: Average HP by Type\n",
        "Find the average HP for each primary type. Which type has the highest average HP?"
    ]),
    code("cell-016", [
        "# Challenge 6: Average HP by type\n",
        "# YOUR SQL QUERY HERE\n",
        "query_6 = \"\"\"\n",
        "\n",
        "\"\"\"\n",
        "run_sql(query_6)\n",
        "\n",
        "# ANSWER: SELECT type1, ROUND(AVG(hp), 1) AS avg_hp FROM pokemon GROUP BY type1 ORDER BY avg_hp DESC"
    ]),
    md("cell-017", [
        "### Challenge 7: Types with High Average Attack\n",
        "Find types where the average attack is greater than 80. Use GROUP BY with HAVING."
    ]),
    code("cell-018", [
        "# Challenge 7: Types with high average attack\n",
        "# YOUR SQL QUERY HERE\n",
        "query_7 = \"\"\"\n",
        "\n",
        "\"\"\"\n",
        "run_sql(query_7)\n",
        "\n",
        "# ANSWER: SELECT type1, ROUND(AVG(attack), 1) AS avg_attack FROM pokemon GROUP BY type1 HAVING AVG(attack) > 80 ORDER BY avg_attack DESC"
    ]),
    md("cell-019", [
        "### Challenge 8: Dual-Type Pokemon\n",
        "Find all Pokemon that have BOTH a type1 AND a type2 (type2 is not NULL). Show name, type1, and type2. Limit to 15."
    ]),
    code("cell-020", [
        "# Challenge 8: Dual-type Pokemon\n",
        "# YOUR SQL QUERY HERE\n",
        "query_8 = \"\"\"\n",
        "\n",
        "\"\"\"\n",
        "run_sql(query_8)\n",
        "\n",
        "# ANSWER: SELECT name, type1, type2 FROM pokemon WHERE type2 IS NOT NULL AND type2 != '' LIMIT 15"
    ]),
    md("cell-021", [
        "---\n",
        "## Hard Challenges (9-12)\n",
        "\n",
        "### Challenge 9: Above-Average Attack\n",
        "Use a **subquery** to find all Pokemon whose attack is above the overall average attack. Show name and attack."
    ]),
    code("cell-022", [
        "# Challenge 9: Above-average attack (subquery)\n",
        "# YOUR SQL QUERY HERE\n",
        "query_9 = \"\"\"\n",
        "\n",
        "\"\"\"\n",
        "result_9 = run_sql(query_9)\n",
        "print(f\"{len(result_9)} Pokemon have above-average attack\")\n",
        "result_9.head(10)\n",
        "\n",
        "# ANSWER: SELECT name, attack FROM pokemon WHERE attack > (SELECT AVG(attack) FROM pokemon) ORDER BY attack DESC"
    ]),
    md("cell-023", [
        "### Challenge 10: Multi-Condition Filter\n",
        "Find Water-type Pokemon with HP > 80 AND speed > 60. Sort by total stats (hp + attack + defense + speed) descending."
    ]),
    code("cell-024", [
        "# Challenge 10: Complex multi-condition filter\n",
        "# YOUR SQL QUERY HERE\n",
        "query_10 = \"\"\"\n",
        "\n",
        "\"\"\"\n",
        "run_sql(query_10)\n",
        "\n",
        "# ANSWER: SELECT name, hp, attack, defense, speed, (hp + attack + defense + speed) AS total FROM pokemon WHERE type1 = 'Water' AND hp > 80 AND speed > 60 ORDER BY total DESC"
    ]),
    md("cell-025", [
        "### Challenge 11: Legendary Pokemon Analysis\n",
        "Find all Legendary Pokemon. Compare their average stats to non-legendary Pokemon."
    ]),
    code("cell-026", [
        "# Challenge 11: Legendary analysis\n",
        "# Part A: Select all legendary Pokemon with their key stats\n",
        "# YOUR SQL QUERY HERE\n",
        "query_11a = \"\"\"\n",
        "\n",
        "\"\"\"\n",
        "print(\"Legendary Pokemon:\")\n",
        "print(run_sql(query_11a))\n",
        "\n",
        "# Part B: Compare average stats (legendary vs non-legendary)\n",
        "# YOUR SQL QUERY HERE\n",
        "query_11b = \"\"\"\n",
        "\n",
        "\"\"\"\n",
        "print(\"\\nLegendary vs Non-Legendary averages:\")\n",
        "run_sql(query_11b)\n",
        "\n",
        "# ANSWER:\n",
        "# query_11a = \"SELECT name, type1, hp, attack, defense, speed FROM pokemon WHERE legendary = 1 ORDER BY attack DESC\"\n",
        "# query_11b = \"SELECT legendary, ROUND(AVG(hp),1) AS avg_hp, ROUND(AVG(attack),1) AS avg_attack, ROUND(AVG(defense),1) AS avg_defense, ROUND(AVG(speed),1) AS avg_speed FROM pokemon GROUP BY legendary\""
    ]),
    md("cell-027", [
        "### Challenge 12: Your Own Query\n",
        "Write your own creative SQL query! Explore something interesting about the Pokemon data."
    ]),
    code("cell-028", [
        "# Challenge 12: Your creative query\n",
        "# What question are you trying to answer? Write it as a comment:\n",
        "# Question: \n",
        "\n",
        "# YOUR SQL QUERY HERE\n",
        "query_12 = \"\"\"\n",
        "\n",
        "\"\"\"\n",
        "run_sql(query_12)"
    ]),
    md("cell-029", [
        "## Submission\n",
        "\n",
        "Congratulations on completing the Pokemon SQL Mini-Project! To get credit:\n",
        "\n",
        "1. Make sure all 12 challenges are completed\n",
        "2. Save this notebook (File > Save a copy in Drive)\n",
        "3. Return to **HireWheel** and complete the UCASE submission:\n",
        "   - **Understand:** Describe the Pokemon dataset\n",
        "   - **Clues:** What data quality issues did you find?\n",
        "   - **Assemble:** Paste your 3 most complex queries\n",
        "   - **Solve:** Describe 2-3 interesting findings\n",
        "   - **Examine:** What additional questions would you explore?"
    ])
]

# ── L11: Data Retrieval & Analysis ──
cells_11 = [
    md("cell-001", [
        "# DAM - Lesson 11: Data Retrieval & Analysis\n",
        "**Code2College | Data Analysis & Management**\n",
        "\n",
        "Estimated time: 150 minutes\n",
        "\n",
        "Welcome to Phase 3! You'll analyze the Netflix dataset — exploring content types, countries, and genres with Pandas and Matplotlib."
    ]),
    md("cell-002", [
        "## Learning Objectives\n",
        "\n",
        "By the end of this lesson, you will be able to:\n",
        "- Load and explore a real-world dataset (Netflix titles)\n",
        "- Identify and handle missing (null) values\n",
        "- Use `value_counts()` for categorical analysis\n",
        "- Create bar charts with Matplotlib\n",
        "- Create pie charts to show proportions"
    ]),
    code("cell-003", [
        "# Setup: Import libraries and load the Netflix dataset\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        f"df = pd.read_csv('{BASE}/phase_3/netflix_titles.csv')\n",
        "print(f\"Loaded {len(df)} Netflix titles\")\n",
        "print(f\"Columns: {df.columns.tolist()}\")\n",
        "df.head()"
    ]),
    md("cell-004", [
        "## Exercise 1: Initial Exploration\n",
        "\n",
        "Get a quick overview of the dataset using the tools you learned in Lesson 5."
    ]),
    code("cell-005", [
        "# Exercise 1: Explore the Netflix dataset\n",
        "\n",
        "# Task 1: Check the shape\n",
        "# TODO: your code here\n",
        "print(\"Shape:\", )\n",
        "\n",
        "# Task 2: Run .info() to see data types and non-null counts\n",
        "# TODO: your code here\n",
        "\n",
        "\n",
        "# Task 3: Run .describe() — what does it tell you?\n",
        "# TODO: your code here\n",
        "\n",
        "\n",
        "# ANSWER:\n",
        "# print(\"Shape:\", df.shape)\n",
        "# df.info()\n",
        "# df.describe()"
    ]),
    md("cell-006", [
        "## Exercise 2: Finding Null Values\n",
        "\n",
        "Real-world data always has missing values. Let's find them."
    ]),
    code("cell-007", [
        "# Exercise 2: Check for null values\n",
        "\n",
        "# Task 1: Count null values in each column\n",
        "# TODO: your code here\n",
        "null_counts = \n",
        "print(\"Null values per column:\")\n",
        "print(null_counts)\n",
        "print()\n",
        "\n",
        "# Task 2: What percentage of each column is null?\n",
        "# TODO: your code here (hint: divide by len(df) and multiply by 100)\n",
        "null_pct = \n",
        "print(\"Null percentage:\")\n",
        "print(null_pct)\n",
        "\n",
        "# ANSWER:\n",
        "# null_counts = df.isnull().sum()\n",
        "# null_pct = (df.isnull().sum() / len(df) * 100).round(1)"
    ]),
    md("cell-008", [
        "## Exercise 3: Handling Null Values\n",
        "\n",
        "For analysis, we need to decide: fill missing values or drop them?"
    ]),
    code("cell-009", [
        "# Exercise 3: Handle null values\n",
        "\n",
        "# Task 1: Fill null values in the 'country' column with 'Unknown'\n",
        "# TODO: your code here\n",
        "\n",
        "\n",
        "# Task 2: Fill null values in the 'director' column with 'Not Listed'\n",
        "# TODO: your code here\n",
        "\n",
        "\n",
        "# Task 3: Verify the nulls are fixed\n",
        "print(\"Remaining nulls in country:\", df['country'].isnull().sum())\n",
        "print(\"Remaining nulls in director:\", df['director'].isnull().sum())\n",
        "\n",
        "# ANSWER:\n",
        "# df['country'] = df['country'].fillna('Unknown')\n",
        "# df['director'] = df['director'].fillna('Not Listed')"
    ]),
    md("cell-010", [
        "## Exercise 4: Categorical Analysis with `value_counts()`\n",
        "\n",
        "Let's see what types of content Netflix offers and which countries produce the most."
    ]),
    code("cell-011", [
        "# Exercise 4: Analyze categorical columns\n",
        "\n",
        "# Task 1: Count content by type (Movie vs TV Show)\n",
        "# TODO: your code here\n",
        "type_counts = \n",
        "print(\"Content by type:\")\n",
        "print(type_counts)\n",
        "print()\n",
        "\n",
        "# Task 2: Find the top 10 countries by number of titles\n",
        "# TODO: your code here\n",
        "country_counts = \n",
        "print(\"Top 10 countries:\")\n",
        "print(country_counts)\n",
        "\n",
        "# ANSWER:\n",
        "# type_counts = df['type'].value_counts()\n",
        "# country_counts = df['country'].value_counts().head(10)"
    ]),
    md("cell-012", [
        "## Exercise 5: Bar Chart — Content by Type\n",
        "\n",
        "Visualize the content type distribution with a bar chart."
    ]),
    code("cell-013", [
        "# Exercise 5: Create a bar chart of content types\n",
        "\n",
        "# TODO: Create a bar chart showing Movie vs TV Show counts\n",
        "# Hint: use plt.bar() or type_counts.plot(kind='bar')\n",
        "\n",
        "plt.figure(figsize=(8, 5))\n",
        "# TODO: your code here\n",
        "\n",
        "plt.title('Netflix Content by Type')\n",
        "plt.xlabel('Type')\n",
        "plt.ylabel('Number of Titles')\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# ANSWER:\n",
        "# plt.figure(figsize=(8, 5))\n",
        "# type_counts.plot(kind='bar', color=['#E50914', '#221f1f'])\n",
        "# plt.title('Netflix Content by Type')\n",
        "# plt.xlabel('Type')\n",
        "# plt.ylabel('Number of Titles')\n",
        "# plt.tight_layout()\n",
        "# plt.show()"
    ]),
    md("cell-014", [
        "## Exercise 6: Pie Chart — Top 5 Countries\n",
        "\n",
        "Show the proportion of content from the top 5 producing countries."
    ]),
    code("cell-015", [
        "# Exercise 6: Create a pie chart of top 5 countries\n",
        "\n",
        "# Get top 5 countries\n",
        "top_5 = df['country'].value_counts().head(5)\n",
        "\n",
        "# TODO: Create a pie chart\n",
        "plt.figure(figsize=(8, 8))\n",
        "# Hint: plt.pie(top_5, labels=top_5.index, autopct='%1.1f%%')\n",
        "# TODO: your code here\n",
        "\n",
        "plt.title('Top 5 Countries by Netflix Content')\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# ANSWER:\n",
        "# plt.figure(figsize=(8, 8))\n",
        "# plt.pie(top_5, labels=top_5.index, autopct='%1.1f%%', startangle=90)\n",
        "# plt.title('Top 5 Countries by Netflix Content')\n",
        "# plt.tight_layout()\n",
        "# plt.show()"
    ]),
    md("cell-016", [
        "## Submission\n",
        "\n",
        "Great work on your first data analysis project! To get credit:\n",
        "\n",
        "1. Make sure all 6 exercises are completed with charts displayed\n",
        "2. Save this notebook (File > Save a copy in Drive)\n",
        "3. Return to **HireWheel** and complete the UCASE submission:\n",
        "   - **Understand:** Rows, columns, nulls found\n",
        "   - **Clues:** What did value_counts reveal?\n",
        "   - **Assemble:** Paste your bar chart code\n",
        "   - **Solve:** 2-3 insights about Netflix data\n",
        "   - **Examine:** What questions need more advanced analysis?"
    ])
]

os.makedirs("/tmp/dam-build/notebooks/phase_2", exist_ok=True)
os.makedirs("/tmp/dam-build/notebooks/phase_3", exist_ok=True)

with open("/tmp/dam-build/notebooks/phase_2/DAM_Lesson_09_SQL_Mini_Project_Pokemon.ipynb", "w") as f:
    json.dump(make_nb(cells_09), f, indent=1)
with open("/tmp/dam-build/notebooks/phase_3/DAM_Lesson_11_Data_Retrieval_Analysis.ipynb", "w") as f:
    json.dump(make_nb(cells_11), f, indent=1)

print("L09 and L11 written.")
