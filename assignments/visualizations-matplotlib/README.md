# 📘 Assignment: Insightful Visualizations with Matplotlib & Seaborn

## 🎯 Objective

Students will clean a small dataset, perform exploratory data analysis, and create clear, informative visualizations using `pandas`, `matplotlib`, and `seaborn`. The emphasis is on transforming data into visual stories and choosing appropriate chart types.

## 📝 Tasks

### 🛠️ 1 — Data Cleaning & Preparation

#### Description
Load the provided dataset, handle missing values, and prepare aggregated views needed for plotting.

#### Requirements

- Load `data.csv` into a `pandas` DataFrame.
- Handle or document any missing values (drop or fill with an explanation).
- Create at least two aggregated views (e.g., group by category and date).

### 🛠️ 2 — Exploratory Data Analysis (EDA)

#### Description
Compute summary statistics and create visual checks to understand distributions and trends.

#### Requirements

- Show summary statistics for numeric columns.
- Create at least two exploratory plots (histogram, boxplot, or time series preview).
- Include brief comments on what each plot reveals.

### 🛠️ 3 — Final Visualizations and Storytelling

#### Description
Create a set of polished visualizations that communicate one or more insights from the data.

#### Requirements

- Produce at least three final plots using `matplotlib` and/or `seaborn` (examples: line chart, bar chart, heatmap, or scatter with regression).
- Each plot must have axis labels, a title, and a short caption (1–2 sentences) explaining the insight.
- Save the plots as PNG files in a `results/` directory.

## Starter Files

- `starter-code.py` — Example code to load the data and scaffold plotting functions.
- `data.csv` — Small sample dataset to use for the assignment.
- `requirements.txt` — Python dependencies.

## How to run

1. (Optional) Create and activate a virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the starter script (it will create a `results/` folder with example plots):

```bash
python starter-code.py
```

4. Open the generated images in the `results/` folder to review.

## Learning Resources

- Pandas documentation: https://pandas.pydata.org/
- Matplotlib gallery: https://matplotlib.org/stable/gallery/index.html
- Seaborn tutorial: https://seaborn.pydata.org/tutorial.html
