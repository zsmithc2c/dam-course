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

# ── L15: Final Project Starter ──
cells_15 = [
    md("cell-001", [
        "# DAM - Lesson 15: Final Project Starter\n",
        "**Code2College | Data Analysis & Management**\n",
        "\n",
        "Estimated time: 180 minutes\n",
        "\n",
        "This is YOUR project! Choose a dataset, form a research question, and begin your capstone analysis."
    ]),
    md("cell-002", [
        "## How to Use This Notebook\n",
        "\n",
        "This notebook is a **template** for your individual capstone project. Work through each section in order:\n",
        "\n",
        "1. Define your research question\n",
        "2. Load your chosen dataset\n",
        "3. Perform initial exploration\n",
        "4. Clean the data\n",
        "5. Begin your analysis\n",
        "6. Create initial visualizations\n",
        "\n",
        "You'll continue this work in Lesson 16."
    ]),
    code("cell-003", [
        "# Setup: Import your libraries\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "\n",
        "sns.set_theme()\n",
        "print(\"Libraries loaded! Ready to start your project.\")"
    ]),
    md("cell-004", [
        "---\n",
        "## Section 1: My Research Question\n",
        "\n",
        "A good research question is:\n",
        "- **Specific** — not too broad (\"What affects health?\" is too broad)\n",
        "- **Measurable** — can be answered with data\n",
        "- **Interesting** — something you're curious about\n",
        "\n",
        "Examples:\n",
        "- \"Do movies with higher budgets tend to earn more revenue?\"\n",
        "- \"What factors are most associated with air quality in US cities?\"\n",
        "- \"How has the popularity of different music genres changed over the decades?\""
    ]),
    md("cell-005", [
        "### My Research Question\n",
        "\n",
        "*TODO: Write your research question here. Be specific!*\n",
        "\n",
        "**Research Question:** \n",
        "\n",
        "**Why I chose this question:** \n",
        "\n",
        "**What I expect to find (hypothesis):** "
    ]),
    md("cell-006", [
        "---\n",
        "## Section 2: My Dataset\n",
        "\n",
        "Load your chosen dataset. You can use:\n",
        "- A dataset provided by your instructor\n",
        "- A public dataset from Kaggle, data.gov, or other sources\n",
        "- Any CSV file accessible via URL"
    ]),
    code("cell-007", [
        "# Section 2: Load your dataset\n",
        "\n",
        "# TODO: Replace the URL below with your dataset URL\n",
        "df = pd.read_csv('YOUR_DATASET_URL_HERE')\n",
        "\n",
        "print(f\"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns\")\n",
        "print(f\"Columns: {df.columns.tolist()}\")\n",
        "df.head()"
    ]),
    md("cell-008", [
        "---\n",
        "## Section 3: Initial Exploration\n",
        "\n",
        "Use the tools from Lessons 5 and 11 to understand your data."
    ]),
    code("cell-009", [
        "# Section 3: Initial Exploration\n",
        "\n",
        "# TODO: Run .shape, .info(), .describe()\n",
        "print(\"Shape:\", df.shape)\n",
        "print()\n",
        "\n",
        "# .info()\n",
        "df.info()\n",
        "print()\n",
        "\n",
        "# .describe()\n",
        "df.describe()"
    ]),
    code("cell-010", [
        "# Check for null values\n",
        "\n",
        "# TODO: Identify which columns have missing values and how many\n",
        "null_report = df.isnull().sum()\n",
        "null_report = null_report[null_report > 0]  # Only show columns with nulls\n",
        "print(\"Columns with missing values:\")\n",
        "print(null_report)\n",
        "print()\n",
        "\n",
        "# TODO: Run value_counts() on 2-3 categorical columns\n",
        "# Pick columns that are relevant to your research question\n"
    ]),
    md("cell-011", [
        "---\n",
        "## Section 4: Data Cleaning\n",
        "\n",
        "Clean your data based on what you found during exploration."
    ]),
    code("cell-012", [
        "# Section 4: Data Cleaning\n",
        "\n",
        "# TODO: Handle missing values\n",
        "# Options:\n",
        "#   df['column'] = df['column'].fillna('Unknown')   # Fill with a default\n",
        "#   df = df.dropna(subset=['important_column'])      # Drop rows missing key data\n",
        "#   df['column'] = df['column'].fillna(df['column'].median())  # Fill with median\n",
        "\n",
        "\n",
        "# TODO: Remove duplicates if needed\n",
        "# df = df.drop_duplicates()\n",
        "\n",
        "\n",
        "# TODO: Convert data types if needed\n",
        "# df['date_column'] = pd.to_datetime(df['date_column'])\n",
        "\n",
        "\n",
        "# Verify cleaning\n",
        "print(f\"After cleaning: {df.shape[0]} rows, {df.shape[1]} columns\")\n",
        "print(f\"Remaining nulls: {df.isnull().sum().sum()}\")"
    ]),
    md("cell-013", [
        "---\n",
        "## Section 5: Analysis\n",
        "\n",
        "Begin analyzing the data to answer your research question."
    ]),
    code("cell-014", [
        "# Section 5: Analysis\n",
        "\n",
        "# TODO: GroupBy analysis — group by a key column and compute aggregates\n",
        "# Example: df.groupby('category')['value'].mean()\n",
        "\n",
        "\n",
        "# TODO: Correlation analysis (if you have numeric columns)\n",
        "# Example: df.select_dtypes(include='number').corr()\n",
        "\n",
        "\n",
        "# TODO: Filtering — find interesting subsets of your data\n",
        "# Example: df[df['column'] > threshold]\n"
    ]),
    md("cell-015", [
        "---\n",
        "## Section 6: Visualizations\n",
        "\n",
        "Create charts that help answer your research question."
    ]),
    code("cell-016", [
        "# Section 6: Visualizations\n",
        "\n",
        "# TODO: Create at least 3 charts that support your analysis\n",
        "\n",
        "# Chart 1: Distribution (histogram or box plot)\n",
        "plt.figure(figsize=(10, 6))\n",
        "# TODO: your code here\n",
        "plt.title('Chart 1: [Your Title]')\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# Chart 2: Comparison (bar chart or grouped chart)\n",
        "plt.figure(figsize=(10, 6))\n",
        "# TODO: your code here\n",
        "plt.title('Chart 2: [Your Title]')\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# Chart 3: Relationship (scatter plot or heatmap)\n",
        "plt.figure(figsize=(10, 6))\n",
        "# TODO: your code here\n",
        "plt.title('Chart 3: [Your Title]')\n",
        "plt.tight_layout()\n",
        "plt.show()"
    ]),
    md("cell-017", [
        "## Submission\n",
        "\n",
        "Great start on your capstone! To get credit for Lesson 15:\n",
        "\n",
        "1. Complete Sections 1-6 above\n",
        "2. Save this notebook (File > Save a copy in Drive)\n",
        "3. Return to **HireWheel** and complete the UCASE submission:\n",
        "   - **Understand:** Describe your chosen dataset\n",
        "   - **Clues:** Initial hypotheses and expected patterns\n",
        "   - **Assemble:** Your analysis plan and steps\n",
        "   - **Solve:** Initial findings from exploration\n",
        "   - **Examine:** Challenges and data cleaning needed\n",
        "\n",
        "You'll continue and finalize this analysis in **Lesson 16**."
    ])
]

# ── L16: Final Project Work ──
cells_16 = [
    md("cell-001", [
        "# DAM - Lesson 16: Final Project -- Analysis & Presentation\n",
        "**Code2College | Data Analysis & Management**\n",
        "\n",
        "Estimated time: 180 minutes\n",
        "\n",
        "Finalize your analysis, create publication-quality charts, and write your report narrative."
    ]),
    md("cell-002", [
        "## Goals for This Lesson\n",
        "\n",
        "1. **Finalize your analysis** — complete any remaining groupby, correlation, or filtering work\n",
        "2. **Create publication-quality charts** — professional formatting, clear labels, high resolution\n",
        "3. **Write your report narrative** — structured analysis in markdown cells\n",
        "4. **Prepare for your presentation** — organize your findings into a clear story"
    ]),
    code("cell-003", [
        "# Setup: Import your libraries\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "\n",
        "sns.set_theme(style='whitegrid')\n",
        "\n",
        "# TODO: Load your dataset (same as Lesson 15)\n",
        "# df = pd.read_csv('YOUR_DATASET_URL_HERE')\n",
        "# Re-apply any data cleaning from Lesson 15\n",
        "\n",
        "print(\"Ready to finalize your project!\")"
    ]),
    md("cell-004", [
        "---\n",
        "## Section 1: Finalizing Analysis\n",
        "\n",
        "Complete any remaining analysis from Lesson 15. Add new findings."
    ]),
    code("cell-005", [
        "# Section 1: Complete your analysis\n",
        "\n",
        "# TODO: Any remaining groupby, correlation, or filtering analysis\n",
        "# Build on what you started in Lesson 15\n",
        "\n",
        "\n",
        "# TODO: What new patterns did you discover?\n"
    ]),
    md("cell-006", [
        "---\n",
        "## Section 2: Publication-Quality Charts\n",
        "\n",
        "Professional charts have:\n",
        "- `plt.figure(figsize=(12, 6))` — large enough to read\n",
        "- Clear title with `fontsize=14` or larger\n",
        "- Axis labels with `fontsize=12`\n",
        "- `plt.tight_layout()` — no cut-off labels\n",
        "- `plt.savefig('chart.png', dpi=300)` — high resolution for presentations"
    ]),
    code("cell-007", [
        "# Section 2: Create your best charts\n",
        "\n",
        "# Chart 1: Your primary finding\n",
        "plt.figure(figsize=(12, 6))\n",
        "# TODO: Create a polished chart for your most important finding\n",
        "\n",
        "plt.title('Your Primary Finding Title', fontsize=16, fontweight='bold')\n",
        "plt.xlabel('X Label', fontsize=12)\n",
        "plt.ylabel('Y Label', fontsize=12)\n",
        "plt.tight_layout()\n",
        "plt.savefig('chart_1.png', dpi=300, bbox_inches='tight')\n",
        "plt.show()\n",
        "print(\"Chart 1 saved as chart_1.png\")"
    ]),
    code("cell-008", [
        "# Chart 2: Supporting evidence\n",
        "plt.figure(figsize=(12, 6))\n",
        "# TODO: Create a second polished chart\n",
        "\n",
        "plt.title('Supporting Evidence Title', fontsize=16, fontweight='bold')\n",
        "plt.xlabel('X Label', fontsize=12)\n",
        "plt.ylabel('Y Label', fontsize=12)\n",
        "plt.tight_layout()\n",
        "plt.savefig('chart_2.png', dpi=300, bbox_inches='tight')\n",
        "plt.show()\n",
        "print(\"Chart 2 saved as chart_2.png\")"
    ]),
    code("cell-009", [
        "# Chart 3: Additional insight\n",
        "plt.figure(figsize=(12, 6))\n",
        "# TODO: Create a third polished chart\n",
        "\n",
        "plt.title('Additional Insight Title', fontsize=16, fontweight='bold')\n",
        "plt.xlabel('X Label', fontsize=12)\n",
        "plt.ylabel('Y Label', fontsize=12)\n",
        "plt.tight_layout()\n",
        "plt.savefig('chart_3.png', dpi=300, bbox_inches='tight')\n",
        "plt.show()\n",
        "print(\"Chart 3 saved as chart_3.png\")"
    ]),
    md("cell-010", [
        "---\n",
        "## Section 3: Report Narrative\n",
        "\n",
        "Write your final analysis report in the markdown cells below. This is the written component of your capstone."
    ]),
    md("cell-011", [
        "### Introduction\n",
        "\n",
        "*TODO: What is your research question? Why is it important? What dataset did you use?*\n",
        "\n",
        "(Replace this text with your introduction — aim for 3-5 sentences)"
    ]),
    md("cell-012", [
        "### Data & Methods\n",
        "\n",
        "*TODO: Describe your dataset (source, size, key columns). What cleaning did you perform? What analysis techniques did you use?*\n",
        "\n",
        "(Replace this text — aim for 4-6 sentences)"
    ]),
    md("cell-013", [
        "### Key Findings\n",
        "\n",
        "*TODO: Present your 3-4 most important findings. Reference your charts by name (Chart 1, Chart 2, etc.). Use specific numbers and percentages.*\n",
        "\n",
        "**Finding 1:** \n",
        "\n",
        "**Finding 2:** \n",
        "\n",
        "**Finding 3:** "
    ]),
    md("cell-014", [
        "### Conclusions & Recommendations\n",
        "\n",
        "*TODO: What did you learn? Answer your original research question. What would you recommend based on the data? What are the limitations?*\n",
        "\n",
        "(Replace this text — aim for 4-6 sentences)"
    ]),
    md("cell-015", [
        "### What I Learned\n",
        "\n",
        "*TODO: Reflect on the skills you used. What was challenging? What would you do differently with more time?*\n",
        "\n",
        "(Replace this text — aim for 3-4 sentences)"
    ]),
    md("cell-016", [
        "---\n",
        "## Section 4: Peer Review Notes\n",
        "\n",
        "After sharing your work with a classmate, record their feedback here."
    ]),
    md("cell-017", [
        "### Peer Feedback\n",
        "\n",
        "*TODO: After peer review, record:*\n",
        "\n",
        "**Reviewer name:** \n",
        "\n",
        "**What they liked:** \n",
        "\n",
        "**What they suggested improving:** \n",
        "\n",
        "**Changes I made based on feedback:** "
    ]),
    md("cell-018", [
        "## Submission\n",
        "\n",
        "Congratulations on completing your capstone analysis! To get credit:\n",
        "\n",
        "1. Complete all sections above (charts saved, report written)\n",
        "2. Save this notebook (File > Save a copy in Drive)\n",
        "3. Return to **HireWheel** and complete the UCASE submission:\n",
        "   - **Understand:** Restated research question\n",
        "   - **Clues:** Data cleaning and transformations performed\n",
        "   - **Assemble:** Code for your 2-3 best visualizations\n",
        "   - **Solve:** Full analysis report text\n",
        "   - **Examine:** Limitations and future analysis ideas\n",
        "4. Paste your **presentation URL** (Google Slides or similar)\n",
        "\n",
        "In **Lesson 17**, you'll present your findings to the class!"
    ])
]

os.makedirs("/tmp/dam-build/notebooks/phase_4", exist_ok=True)
with open("/tmp/dam-build/notebooks/phase_4/DAM_Lesson_15_Final_Project_Starter.ipynb", "w") as f:
    json.dump(make_nb(cells_15), f, indent=1)
with open("/tmp/dam-build/notebooks/phase_4/DAM_Lesson_16_Final_Project_Work.ipynb", "w") as f:
    json.dump(make_nb(cells_16), f, indent=1)
print("L15 and L16 written.")
