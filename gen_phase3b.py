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

# ── L12: Analysis Continued ──
cells_12 = [
    md("cell-001", [
        "# DAM - Lesson 12: Data Analysis Continued\n",
        "**Code2College | Data Analysis & Management**\n",
        "\n",
        "Estimated time: 130 minutes\n",
        "\n",
        "Continuing our Netflix analysis with histograms, box plots, groupby, and trend analysis."
    ]),
    md("cell-002", [
        "## Learning Objectives\n",
        "\n",
        "By the end of this lesson, you will be able to:\n",
        "- Create histograms to visualize numeric distributions\n",
        "- Create box plots to identify spread and outliers\n",
        "- Use `groupby()` for multi-dimensional analysis\n",
        "- Find top directors and common genres\n",
        "- Create year-over-year trend line charts"
    ]),
    code("cell-003", [
        "# Setup: Import libraries and load the Netflix dataset\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        f"df = pd.read_csv('{BASE}/phase_3/netflix_titles.csv')\n",
        "\n",
        "# Clean nulls (same as L11)\n",
        "df['country'] = df['country'].fillna('Unknown')\n",
        "df['director'] = df['director'].fillna('Not Listed')\n",
        "\n",
        "print(f\"Loaded {len(df)} Netflix titles\")\n",
        "df.head()"
    ]),
    md("cell-004", [
        "## Exercise 1: Histogram of Release Years\n",
        "\n",
        "A histogram shows the distribution of a numeric variable. Let's see when Netflix content was released."
    ]),
    code("cell-005", [
        "# Exercise 1: Histogram of release years\n",
        "\n",
        "# TODO: Create a histogram of the 'release_year' column\n",
        "# Hint: plt.hist(df['release_year'], bins=30)\n",
        "plt.figure(figsize=(10, 5))\n",
        "# TODO: your code here\n",
        "\n",
        "plt.title('Distribution of Netflix Content by Release Year')\n",
        "plt.xlabel('Release Year')\n",
        "plt.ylabel('Number of Titles')\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# ANSWER:\n",
        "# plt.figure(figsize=(10, 5))\n",
        "# plt.hist(df['release_year'], bins=30, color='#E50914', edgecolor='black')\n",
        "# plt.title('Distribution of Netflix Content by Release Year')\n",
        "# plt.xlabel('Release Year')\n",
        "# plt.ylabel('Number of Titles')\n",
        "# plt.tight_layout()\n",
        "# plt.show()"
    ]),
    md("cell-006", [
        "## Exercise 2: Box Plot\n",
        "\n",
        "Box plots show the median, quartiles, and outliers. Let's compare release years by content type."
    ]),
    code("cell-007", [
        "# Exercise 2: Box plot comparing Movie vs TV Show release years\n",
        "\n",
        "# TODO: Create a box plot\n",
        "# Approach: Create separate data for Movies and TV Shows, then plot side by side\n",
        "movies = df[df['type'] == 'Movie']['release_year']\n",
        "tv_shows = df[df['type'] == 'TV Show']['release_year']\n",
        "\n",
        "plt.figure(figsize=(8, 5))\n",
        "# TODO: your code here\n",
        "# Hint: plt.boxplot([movies, tv_shows], labels=['Movies', 'TV Shows'])\n",
        "\n",
        "plt.title('Release Year Distribution: Movies vs TV Shows')\n",
        "plt.ylabel('Release Year')\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# ANSWER:\n",
        "# plt.figure(figsize=(8, 5))\n",
        "# plt.boxplot([movies, tv_shows], labels=['Movies', 'TV Shows'])\n",
        "# plt.title('Release Year Distribution: Movies vs TV Shows')\n",
        "# plt.ylabel('Release Year')\n",
        "# plt.tight_layout()\n",
        "# plt.show()"
    ]),
    md("cell-008", [
        "## Exercise 3: GroupBy — Content Count by Country\n",
        "\n",
        "Use `groupby()` to count how many titles each country has produced."
    ]),
    code("cell-009", [
        "# Exercise 3: GroupBy country and type\n",
        "\n",
        "# Task 1: Count titles by country (top 15)\n",
        "# TODO: your code here\n",
        "country_type = \n",
        "print(\"Top 15 countries by title count:\")\n",
        "print(country_type)\n",
        "print()\n",
        "\n",
        "# Task 2: Create a bar chart of the top 10 countries\n",
        "top_10 = df['country'].value_counts().head(10)\n",
        "\n",
        "plt.figure(figsize=(10, 5))\n",
        "# TODO: your code here\n",
        "\n",
        "plt.title('Top 10 Countries by Netflix Content')\n",
        "plt.xlabel('Country')\n",
        "plt.ylabel('Number of Titles')\n",
        "plt.xticks(rotation=45, ha='right')\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# ANSWER:\n",
        "# country_type = df.groupby('country')['type'].count().sort_values(ascending=False).head(15)\n",
        "# top_10.plot(kind='bar', color='#E50914')"
    ]),
    md("cell-010", [
        "## Exercise 4: Director with Most Titles\n",
        "\n",
        "Who are the most prolific directors on Netflix?"
    ]),
    code("cell-011", [
        "# Exercise 4: Find directors with the most titles\n",
        "\n",
        "# TODO: Find the top 10 directors by title count\n",
        "# Hint: Exclude 'Not Listed' from the results\n",
        "directors = df[df['director'] != 'Not Listed']\n",
        "# TODO: your code here\n",
        "top_directors = \n",
        "print(\"Top 10 Directors on Netflix:\")\n",
        "print(top_directors)\n",
        "\n",
        "# ANSWER:\n",
        "# top_directors = directors['director'].value_counts().head(10)"
    ]),
    md("cell-012", [
        "## Exercise 5: Most Common Genres\n",
        "\n",
        "The `listed_in` column contains genres separated by commas. Let's split them to find the most common."
    ]),
    code("cell-013", [
        "# Exercise 5: Most common genres\n",
        "\n",
        "# Step 1: Split the 'listed_in' column and explode into individual genres\n",
        "# TODO: your code here\n",
        "# Hint: df['listed_in'].str.split(', ').explode().value_counts()\n",
        "genre_counts = \n",
        "print(\"Top 15 Genres:\")\n",
        "print(genre_counts)\n",
        "\n",
        "# Step 2: Create a horizontal bar chart of top 10 genres\n",
        "plt.figure(figsize=(10, 6))\n",
        "# TODO: your code here\n",
        "\n",
        "plt.title('Top 10 Netflix Genres')\n",
        "plt.xlabel('Number of Titles')\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# ANSWER:\n",
        "# genre_counts = df['listed_in'].str.split(', ').explode().value_counts()\n",
        "# print(genre_counts.head(15))\n",
        "# genre_counts.head(10).plot(kind='barh', color='#E50914')"
    ]),
    md("cell-014", [
        "## Exercise 6: Year-Over-Year Content Trend\n",
        "\n",
        "How has Netflix's content library grown over time? Create a line chart."
    ]),
    code("cell-015", [
        "# Exercise 6: Year-over-year trend line chart\n",
        "\n",
        "# TODO: Count titles per release year and create a line chart\n",
        "# Hint: df['release_year'].value_counts().sort_index()\n",
        "yearly = \n",
        "\n",
        "# Only show years from 2000 onward for clearer trend\n",
        "yearly_recent = yearly[yearly.index >= 2000]\n",
        "\n",
        "plt.figure(figsize=(12, 5))\n",
        "# TODO: your code here\n",
        "# Hint: plt.plot(yearly_recent.index, yearly_recent.values)\n",
        "\n",
        "plt.title('Netflix Content Added by Release Year (2000+)')\n",
        "plt.xlabel('Year')\n",
        "plt.ylabel('Number of Titles')\n",
        "plt.grid(True, alpha=0.3)\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# ANSWER:\n",
        "# yearly = df['release_year'].value_counts().sort_index()\n",
        "# yearly_recent = yearly[yearly.index >= 2000]\n",
        "# plt.plot(yearly_recent.index, yearly_recent.values, color='#E50914', linewidth=2)\n",
        "# plt.fill_between(yearly_recent.index, yearly_recent.values, alpha=0.2, color='#E50914')"
    ]),
    md("cell-016", [
        "## Submission\n",
        "\n",
        "Great analysis work! To get credit:\n",
        "\n",
        "1. Make sure all 6 exercises are completed with charts displayed\n",
        "2. Save this notebook (File > Save a copy in Drive)\n",
        "3. Return to **HireWheel** and complete the UCASE submission:\n",
        "   - **Understand:** What questions are you exploring?\n",
        "   - **Clues:** What did histograms and box plots reveal?\n",
        "   - **Assemble:** Paste your most interesting groupby code\n",
        "   - **Solve:** 3 most interesting trends or patterns\n",
        "   - **Examine:** How would you present these findings?"
    ])
]

# ── L13: Matplotlib & Seaborn ──
cells_13 = [
    md("cell-001", [
        "# DAM - Lesson 13: Matplotlib & Seaborn + Netflix Report\n",
        "**Code2College | Data Analysis & Management**\n",
        "\n",
        "Estimated time: 140 minutes\n",
        "\n",
        "Level up your visualizations with Seaborn! Then write a structured data analysis report."
    ]),
    md("cell-002", [
        "## Learning Objectives\n",
        "\n",
        "By the end of this lesson, you will be able to:\n",
        "- Use `sns.set_theme()` to apply professional themes\n",
        "- Create countplots, histplots, and boxplots with Seaborn\n",
        "- Compare Seaborn vs Matplotlib approaches\n",
        "- Customize color palettes\n",
        "- Write a structured data analysis report (Introduction, Methodology, Findings, Conclusion)"
    ]),
    code("cell-003", [
        "# Setup: Import libraries and load datasets\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "\n",
        "# Load Netflix data\n",
        f"df_netflix = pd.read_csv('{BASE}/phase_3/netflix_titles.csv')\n",
        "df_netflix['country'] = df_netflix['country'].fillna('Unknown')\n",
        "df_netflix['director'] = df_netflix['director'].fillna('Not Listed')\n",
        "\n",
        "# Load employee data for salary analysis\n",
        f"df_emp = pd.read_csv('{BASE}/phase_1/employee_data.csv')\n",
        "\n",
        "print(f\"Netflix: {len(df_netflix)} titles\")\n",
        "print(f\"Employee: {len(df_emp)} records\")"
    ]),
    md("cell-004", [
        "## Exercise 1: Seaborn Themes\n",
        "\n",
        "Seaborn instantly makes your charts look more professional with `sns.set_theme()`."
    ]),
    code("cell-005", [
        "# Exercise 1: Apply Seaborn themes\n",
        "\n",
        "# TODO: Apply the default Seaborn theme\n",
        "# Hint: sns.set_theme()\n",
        "\n",
        "# Create a simple chart to see the theme\n",
        "plt.figure(figsize=(8, 4))\n",
        "df_netflix['type'].value_counts().plot(kind='bar')\n",
        "plt.title('Netflix Content Types (with Seaborn theme)')\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# ANSWER:\n",
        "# sns.set_theme()"
    ]),
    md("cell-006", [
        "## Exercise 2: `sns.countplot()` vs `plt.bar()`\n",
        "\n",
        "Seaborn's countplot automatically counts and plots categorical data — no need to call `value_counts()` first."
    ]),
    code("cell-007", [
        "# Exercise 2: Compare countplot to bar chart\n",
        "\n",
        "fig, axes = plt.subplots(1, 2, figsize=(14, 5))\n",
        "\n",
        "# Left: Matplotlib approach (manual)\n",
        "type_counts = df_netflix['type'].value_counts()\n",
        "axes[0].bar(type_counts.index, type_counts.values, color=['#E50914', '#221f1f'])\n",
        "axes[0].set_title('Matplotlib: plt.bar()')\n",
        "axes[0].set_ylabel('Count')\n",
        "\n",
        "# Right: Seaborn approach (automatic)\n",
        "# TODO: Use sns.countplot() on axes[1]\n",
        "# Hint: sns.countplot(data=df_netflix, x='type', ax=axes[1])\n",
        "\n",
        "axes[1].set_title('Seaborn: sns.countplot()')\n",
        "\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# ANSWER:\n",
        "# sns.countplot(data=df_netflix, x='type', ax=axes[1], palette='Set2')"
    ]),
    md("cell-008", [
        "## Exercise 3: `sns.histplot()`\n",
        "\n",
        "Seaborn's histogram adds KDE (density curve) and looks better by default."
    ]),
    code("cell-009", [
        "# Exercise 3: Seaborn histogram of release years\n",
        "\n",
        "plt.figure(figsize=(10, 5))\n",
        "\n",
        "# TODO: Create a histogram with sns.histplot()\n",
        "# Include kde=True to show the density curve\n",
        "# Hint: sns.histplot(data=df_netflix, x='release_year', bins=30, kde=True)\n",
        "\n",
        "plt.title('Netflix Release Year Distribution')\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# ANSWER:\n",
        "# sns.histplot(data=df_netflix, x='release_year', bins=30, kde=True, color='#E50914')"
    ]),
    md("cell-010", [
        "## Exercise 4: `sns.boxplot()`\n",
        "\n",
        "Create a box plot comparing salary by department using the employee dataset."
    ]),
    code("cell-011", [
        "# Exercise 4: Box plot of salary by department\n",
        "\n",
        "plt.figure(figsize=(10, 5))\n",
        "\n",
        "# TODO: Create a boxplot with sns.boxplot()\n",
        "# Hint: sns.boxplot(data=df_emp, x='department', y='salary')\n",
        "\n",
        "plt.title('Salary Distribution by Department')\n",
        "plt.xticks(rotation=45, ha='right')\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# ANSWER:\n",
        "# sns.boxplot(data=df_emp, x='department', y='salary', palette='viridis')"
    ]),
    md("cell-012", [
        "## Exercise 5: Color Palette Exploration\n",
        "\n",
        "Seaborn offers many color palettes. Try different ones to see which tells your story best."
    ]),
    code("cell-013", [
        "# Exercise 5: Try different color palettes\n",
        "\n",
        "# See available palettes\n",
        "palettes = ['Set2', 'husl', 'viridis', 'coolwarm']\n",
        "\n",
        "fig, axes = plt.subplots(2, 2, figsize=(14, 10))\n",
        "\n",
        "for ax, pal in zip(axes.flat, palettes):\n",
        "    # TODO: Create a countplot on each axis with a different palette\n",
        "    # Hint: sns.countplot(data=df_netflix, x='type', palette=pal, ax=ax)\n",
        "    ax.set_title(f'Palette: {pal}')\n",
        "\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# ANSWER:\n",
        "# for ax, pal in zip(axes.flat, palettes):\n",
        "#     sns.countplot(data=df_netflix, x='type', palette=pal, ax=ax)\n",
        "#     ax.set_title(f'Palette: {pal}')"
    ]),
    md("cell-014", [
        "## Exercise 6: Seaborn Boxplot for Employee Salaries\n",
        "\n",
        "Create a detailed box plot exploring salary patterns in the employee data."
    ]),
    code("cell-015", [
        "# Exercise 6: Detailed employee salary analysis\n",
        "\n",
        "plt.figure(figsize=(12, 6))\n",
        "\n",
        "# TODO: Create a boxplot of salary by department\n",
        "# Add: showmeans=True, showfliers=True\n",
        "\n",
        "plt.title('Employee Salary Distribution by Department', fontsize=14)\n",
        "plt.xlabel('Department', fontsize=12)\n",
        "plt.ylabel('Salary ($)', fontsize=12)\n",
        "plt.xticks(rotation=45, ha='right')\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# ANSWER:\n",
        "# sns.boxplot(data=df_emp, x='department', y='salary', palette='Set2', showmeans=True)"
    ]),
    md("cell-016", [
        "## Exercise 7: Create a Polished Chart\n",
        "\n",
        "Combine everything: Seaborn style, custom colors, clear labels, meaningful title."
    ]),
    code("cell-017", [
        "# Exercise 7: Your best Seaborn chart\n",
        "\n",
        "# TODO: Create a polished chart using any Seaborn function\n",
        "# Requirements:\n",
        "#   - Custom color palette\n",
        "#   - Clear title and axis labels\n",
        "#   - figsize at least (10, 6)\n",
        "#   - plt.tight_layout()\n",
        "\n",
        "plt.figure(figsize=(10, 6))\n",
        "# TODO: your code here\n",
        "\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# ANSWER:\n",
        "# plt.figure(figsize=(10, 6))\n",
        "# top_countries = df_netflix[df_netflix['country'].isin(df_netflix['country'].value_counts().head(5).index)]\n",
        "# sns.countplot(data=top_countries, x='country', hue='type', palette='Set2')\n",
        "# plt.title('Content Types by Top 5 Countries', fontsize=14)\n",
        "# plt.xlabel('Country', fontsize=12)\n",
        "# plt.ylabel('Number of Titles', fontsize=12)\n",
        "# plt.xticks(rotation=45, ha='right')"
    ]),
    md("cell-018", [
        "---\n",
        "## Netflix Data Report\n",
        "\n",
        "Now write a structured analysis report using markdown cells. Fill in each section below."
    ]),
    md("cell-019", [
        "### Introduction\n",
        "\n",
        "*TODO: Write 2-3 sentences introducing your analysis. What dataset are you analyzing? What questions are you trying to answer?*\n",
        "\n",
        "(Replace this text with your introduction)"
    ]),
    md("cell-020", [
        "### Methodology\n",
        "\n",
        "*TODO: Describe the tools and techniques you used. What charts did you create and why? How did you handle missing data?*\n",
        "\n",
        "(Replace this text with your methodology)"
    ]),
    md("cell-021", [
        "### Findings\n",
        "\n",
        "*TODO: Present your 3-4 key findings. Reference specific charts and numbers. What patterns did you discover?*\n",
        "\n",
        "1. Finding 1: ...\n",
        "2. Finding 2: ...\n",
        "3. Finding 3: ..."
    ]),
    md("cell-022", [
        "### Conclusion\n",
        "\n",
        "*TODO: Summarize what you learned. What are the limitations of this analysis? What would you explore further?*\n",
        "\n",
        "(Replace this text with your conclusion)"
    ]),
    md("cell-023", [
        "## Submission\n",
        "\n",
        "You've created professional visualizations and written a data report! To get credit:\n",
        "\n",
        "1. Make sure all 7 exercises and 4 report sections are completed\n",
        "2. Save this notebook (File > Save a copy in Drive)\n",
        "3. Return to **HireWheel** and complete the UCASE submission:\n",
        "   - **Understand:** Focus question for your report\n",
        "   - **Clues:** Chart types you created and why\n",
        "   - **Assemble:** Best Seaborn visualization code\n",
        "   - **Solve:** Full report text\n",
        "   - **Examine:** What would you do with more data?"
    ])
]

with open("/tmp/dam-build/notebooks/phase_3/DAM_Lesson_12_Analysis_Continued.ipynb", "w") as f:
    json.dump(make_nb(cells_12), f, indent=1)
with open("/tmp/dam-build/notebooks/phase_3/DAM_Lesson_13_Matplotlib_Seaborn.ipynb", "w") as f:
    json.dump(make_nb(cells_13), f, indent=1)

print("L12 and L13 written.")
