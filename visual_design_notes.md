# Visual Design Notes -- Pass 2B

## Summary
Added diagrams, inline SVGs, and HTML visuals to 12 of 17 DAM lesson files.
Lessons L1, L3, L12, L16, L17 were skipped (no visuals specified in brief).

## Visuals Added Per Lesson

### L2: NumPy Arrays (light theme)
- **1D array visual**: 5 boxes with index labels, arr[2] highlighted in red
- **Slicing visual**: arr[1:4] with orange highlighted included elements, grey excluded
- **2D array grid**: 3x4 table with arr[1][2]=7 highlighted in red

### L4: Arrays vs DataFrames (light theme)
- **Mermaid CDN** added to `<head>` with `theme:'default'`
- **Mermaid flowchart**: Decision tree "When to use Array vs DataFrame"
- **Side-by-side comparison**: NumPy array (green border) vs DataFrame (blue border)

### L5: Working with DataFrames (light theme)
- **Annotated .describe() table**: 8 stat rows with blue labels, plain English explanations, 50% row highlighted yellow

### L6: Intro to Databases & SQL (dark theme)
- **Mermaid CDN** added to `<head>` with `theme:'dark'`
- **Mermaid ER diagram**: employees table entity-relationship diagram
- **Table/Rows/Columns hierarchy**: 3-card layout showing Columns, Rows, Primary Key
- **Annotated CREATE TABLE**: Line-by-line breakdown with inline comments

### L7: SQL SELECT Mastery (dark theme)
- **WHERE before/after visual**: Side-by-side tables showing filtering effect, matching rows highlighted green, excluded rows crossed out
- **ORDER BY ASC vs DESC**: Two-column layout showing same data sorted both ways with directional labels

### L8: Data Cleaning (dark theme)
- **Mermaid CDN** added to `<head>` with `theme:'dark'`
- **Mermaid data cleaning flowchart**: Linear flow from Raw Data through each cleaning step (duplicates, NULLs, bad values, wrong types) to Clean Data
- **Before/after comparison**: Red-bordered messy table vs green-bordered clean table showing specific fixes

### L9: SQL Mini-Project (dark theme)
- **Pokemon type color chips**: Flex-wrapped color-coded badges for all 15 Pokemon types using classic game colors

### L10: JOINs & Exporting (dark theme) -- MOST CRITICAL
- **4 SVG Venn diagrams**: INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN -- each embedded in its respective join-card with proper color coding (green/blue/orange/red)
- **INNER vs LEFT JOIN result tables**: Side-by-side comparison showing matched rows vs NULL-filled unmatched rows

### L11: Data Retrieval & Analysis (light theme)
- **Mermaid CDN** added to `<head>` with `theme:'default'`
- **Mermaid data pipeline flowchart**: CSV/Database -> DataFrame -> Clean DataFrame -> Analysis Results -> Visualizations

### L13: Matplotlib & Seaborn (light theme)
- **Side-by-side code comparison**: Matplotlib bar chart code (more lines) vs Seaborn countplot (fewer lines) -- same visual result

### L14: Data Project (light theme)
- **Correlation coefficient scale**: Gradient bar from -1.0 (blue) to +1.0 (red) with labeled markers
- **Regression line SVG diagrams**: Three mini scatter plots showing positive slope, negative slope, and flat (no relationship)

### L15: Final Project Planning (light theme)
- **Mermaid CDN** added to `<head>` with `theme:'default'`
- **Mermaid capstone flowchart**: L15 (Plan) -> L16 (Analyze) -> L17 (Present) with color-coded stages

## Technical Notes
- Mermaid.js CDN v10 used: `https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js`
- Dark theme lessons (L6-L10): `mermaid.initialize({startOnLoad:true,theme:'dark'})`
- Light theme lessons (L4, L11, L15): `mermaid.initialize({startOnLoad:true,theme:'default'})`
- All SVGs are inline (no external image files)
- All diagrams use existing CSS variables from each lesson's theme
- Caption pattern: `<p class="diagram-caption" style="text-align:center;font-size:0.85em;color:#97a3b6;margin-top:4px">...</p>` (dark), `color:#64748b` (light)
- No question IDs, data-question-id attributes, form JS, or script src paths were modified
- No Bootstrap or external CSS was added

## Files Modified (12 total)
1. `dam_lesson_02_numpy_arrays.html`
2. `dam_lesson_04_arrays_vs_dataframes.html`
3. `dam_lesson_05_working_with_dataframes.html`
4. `dam_lesson_06_intro_databases_sql.html`
5. `dam_lesson_07_sql_select_mastery.html`
6. `dam_lesson_08_data_cleaning.html`
7. `dam_lesson_09_sql_mini_project.html`
8. `dam_lesson_10_joins_and_exporting.html`
9. `dam_lesson_11_data_retrieval_analysis.html`
10. `dam_lesson_13_matplotlib_seaborn.html`
11. `dam_lesson_14_data_project.html`
12. `dam_lesson_15_final_project_planning.html`
