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

cells_14 = [
    md("cell-001", [
        "# DAM - Lesson 14: Data Project -- Texas Car Accidents\n",
        "**Code2College | Data Analysis & Management**\n",
        "\n",
        "Estimated time: 160 minutes\n",
        "\n",
        "This is the most technically advanced lesson before your capstone. You'll analyze Texas car accident data using correlation analysis, heatmaps, regression plots, and geographic mapping."
    ]),
    md("cell-002", [
        "## Learning Objectives\n",
        "\n",
        "By the end of this lesson, you will be able to:\n",
        "- Compute a correlation matrix with `df.corr()`\n",
        "- Visualize correlations with `sns.heatmap()`\n",
        "- Create regression plots with `sns.regplot()`\n",
        "- Build geographic maps with Folium\n",
        "- Write analytical conclusions from complex data"
    ]),
    code("cell-003", [
        "# Setup: Import libraries\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "\n",
        "sns.set_theme()\n",
        "\n",
        "# Load the Texas accidents dataset\n",
        f"df = pd.read_csv('{BASE}/phase_3/tx_accidents_2022_sample.csv')\n",
        "print(f\"Loaded {len(df)} accident records\")\n",
        "print(f\"Columns: {df.columns.tolist()}\")\n",
        "df.head()"
    ]),
    md("cell-004", [
        "## Exercise 1: Initial Exploration\n",
        "\n",
        "Get familiar with the dataset before diving into analysis."
    ]),
    code("cell-005", [
        "# Exercise 1: Explore the Texas accidents dataset\n",
        "\n",
        "# Task 1: Check shape, dtypes, and info\n",
        "# TODO: your code here\n",
        "print(\"Shape:\", df.shape)\n",
        "print()\n",
        "df.info()\n",
        "print()\n",
        "\n",
        "# Task 2: Run describe() on numeric columns\n",
        "# TODO: your code here\n",
        "\n",
        "\n",
        "# Task 3: Check for null values\n",
        "# TODO: your code here\n",
        "print(\"\\nNull values:\")\n",
        "print(df.isnull().sum())"
    ]),
    md("cell-006", [
        "## Exercise 2: Correlation Matrix\n",
        "\n",
        "`df.corr()` computes the Pearson correlation between all numeric columns. Values range from -1 (strong negative) to +1 (strong positive). Values near 0 mean no linear relationship."
    ]),
    code("cell-007", [
        "# Exercise 2: Compute the correlation matrix\n",
        "\n",
        "# TODO: Select only numeric columns and compute correlation\n",
        "# Hint: df.select_dtypes(include='number').corr()\n",
        "numeric_df = df.select_dtypes(include='number')\n",
        "corr_matrix = \n",
        "\n",
        "print(\"Correlation matrix:\")\n",
        "print(corr_matrix.round(2))\n",
        "\n",
        "# ANSWER:\n",
        "# corr_matrix = numeric_df.corr()"
    ]),
    md("cell-008", [
        "## Exercise 3: Correlation Heatmap\n",
        "\n",
        "A heatmap makes it easy to spot strong correlations at a glance."
    ]),
    code("cell-009", [
        "# Exercise 3: Create a correlation heatmap\n",
        "\n",
        "plt.figure(figsize=(12, 8))\n",
        "\n",
        "# TODO: Create a heatmap with annotations\n",
        "# Hint: sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, fmt='.2f')\n",
        "\n",
        "plt.title('Correlation Heatmap: Texas Car Accidents', fontsize=14)\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# ANSWER:\n",
        "# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, fmt='.2f',\n",
        "#             square=True, linewidths=0.5)"
    ]),
    md("cell-010", [
        "## Exercise 4: Regression Plot\n",
        "\n",
        "`sns.regplot()` shows the relationship between two variables with a fitted regression line."
    ]),
    code("cell-011", [
        "# Exercise 4: Regression plot\n",
        "\n",
        "# TODO: Create a regression plot showing the relationship between\n",
        "# severity and another numeric variable (e.g., temperature, visibility)\n",
        "# Hint: sns.regplot(data=df, x='temperature', y='severity')\n",
        "\n",
        "plt.figure(figsize=(10, 6))\n",
        "# TODO: your code here\n",
        "\n",
        "plt.title('Relationship: Temperature vs Severity')\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# Try another pair of variables\n",
        "plt.figure(figsize=(10, 6))\n",
        "# TODO: your code here (try different x and y columns)\n",
        "\n",
        "plt.title('Your Second Regression Plot')\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# ANSWER:\n",
        "# sns.regplot(data=df, x='temperature', y='severity', scatter_kws={'alpha': 0.3})\n",
        "# sns.regplot(data=df, x='visibility', y='severity', scatter_kws={'alpha': 0.3})"
    ]),
    md("cell-012", [
        "## Exercise 5: Geographic Map with Folium\n",
        "\n",
        "Folium creates interactive maps. Let's map accident locations across Texas."
    ]),
    code("cell-013", [
        "# Exercise 5: Install Folium and create a base map\n",
        "!pip install folium -q\n",
        "import folium\n",
        "\n",
        "# TODO: Create a base map centered on Texas\n",
        "# Hint: folium.Map(location=[31.0, -100.0], zoom_start=6)\n",
        "texas_map = \n",
        "\n",
        "# Display the map\n",
        "texas_map\n",
        "\n",
        "# ANSWER:\n",
        "# texas_map = folium.Map(location=[31.0, -100.0], zoom_start=6)"
    ]),
    md("cell-014", [
        "## Exercise 6: Add Accident Markers\n",
        "\n",
        "Add markers for sample accidents to see where they cluster."
    ]),
    code("cell-015", [
        "# Exercise 6: Add markers to the map\n",
        "\n",
        "# Create a new map\n",
        "accident_map = folium.Map(location=[31.0, -100.0], zoom_start=6)\n",
        "\n",
        "# Take a sample of 200 accidents (too many markers slows down the map)\n",
        "sample = df.dropna(subset=['start_lat', 'start_lng']).sample(n=min(200, len(df)), random_state=42)\n",
        "\n",
        "# TODO: Add circle markers for each accident\n",
        "# Loop through sample rows and add markers\n",
        "for _, row in sample.iterrows():\n",
        "    # TODO: Add a CircleMarker at each accident location\n",
        "    # Hint:\n",
        "    # folium.CircleMarker(\n",
        "    #     location=[row['start_lat'], row['start_lng']],\n",
        "    #     radius=3,\n",
        "    #     color='red',\n",
        "    #     fill=True,\n",
        "    #     fill_opacity=0.6\n",
        "    # ).add_to(accident_map)\n",
        "    pass\n",
        "\n",
        "# Display the map\n",
        "accident_map\n",
        "\n",
        "# ANSWER:\n",
        "# for _, row in sample.iterrows():\n",
        "#     folium.CircleMarker(\n",
        "#         location=[row['start_lat'], row['start_lng']],\n",
        "#         radius=3,\n",
        "#         color='red',\n",
        "#         fill=True,\n",
        "#         fill_opacity=0.6\n",
        "#     ).add_to(accident_map)"
    ]),
    md("cell-016", [
        "## Exercise 7: Analysis Conclusions\n",
        "\n",
        "Summarize your findings from the correlation analysis, regression plots, and geographic map."
    ]),
    code("cell-017", [
        "# Exercise 7: Summary statistics for your conclusions\n",
        "\n",
        "# Calculate some summary stats to support your analysis\n",
        "print(\"=== Texas Car Accidents Analysis Summary ===\")\n",
        "print(f\"Total accidents in dataset: {len(df)}\")\n",
        "print(f\"Severity levels: {df['severity'].value_counts().to_dict() if 'severity' in df.columns else 'N/A'}\")\n",
        "print()\n",
        "\n",
        "# TODO: Add more summary statistics that support your findings\n",
        "# Suggestions:\n",
        "# - Average severity by weather condition\n",
        "# - Most common time of day for accidents\n",
        "# - City with most accidents\n",
        "\n",
        "\n",
        "# ANSWER:\n",
        "# if 'city' in df.columns:\n",
        "#     print(\"Top 10 cities by accident count:\")\n",
        "#     print(df['city'].value_counts().head(10))\n",
        "# if 'weather_condition' in df.columns:\n",
        "#     print(\"\\nAccidents by weather condition:\")\n",
        "#     print(df['weather_condition'].value_counts().head(10))"
    ]),
    md("cell-018", [
        "## Submission\n",
        "\n",
        "Outstanding work on this advanced analysis! To get credit:\n",
        "\n",
        "1. Make sure all 7 exercises are completed (including Folium map)\n",
        "2. Save this notebook (File > Save a copy in Drive)\n",
        "3. Return to **HireWheel** and complete the UCASE submission:\n",
        "   - **Understand:** Describe the dataset\n",
        "   - **Clues:** What did the correlation matrix reveal?\n",
        "   - **Assemble:** Paste your heatmap AND Folium map code\n",
        "   - **Solve:** Summary of findings\n",
        "   - **Examine:** Limitations and additional data needs"
    ])
]

with open("/tmp/dam-build/notebooks/phase_3/DAM_Lesson_14_Data_Project_TX_Accidents.ipynb", "w") as f:
    json.dump(make_nb(cells_14), f, indent=1)
print("L14 written.")
