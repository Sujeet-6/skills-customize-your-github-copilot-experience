import os
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def ensure_results_dir():
    Path("results").mkdir(parents=True, exist_ok=True)


def load_data(path="data.csv"):
    df = pd.read_csv(path, parse_dates=["date"])
    return df


def basic_eda(df: pd.DataFrame):
    print("Data shape:", df.shape)
    print("Missing values:\n", df.isna().sum())
    print("Summary statistics:\n", df.describe())


def example_plots(df: pd.DataFrame):
    ensure_results_dir()

    # Time series: aggregate daily totals
    daily = df.groupby("date")["value"].sum().reset_index()
    plt.figure(figsize=(8, 4))
    sns.lineplot(data=daily, x="date", y="value")
    plt.title("Daily total value")
    plt.xlabel("Date")
    plt.ylabel("Total value")
    plt.tight_layout()
    plt.savefig("results/daily_total.png")
    plt.close()

    # Category distribution
    plt.figure(figsize=(6, 4))
    sns.barplot(data=df.groupby("category")["value"].sum().reset_index(), x="category", y="value")
    plt.title("Total value by category")
    plt.xlabel("Category")
    plt.ylabel("Total value")
    plt.tight_layout()
    plt.savefig("results/value_by_category.png")
    plt.close()

    # Scatter with regression
    plt.figure(figsize=(6, 4))
    sns.scatterplot(data=df, x="value", y="value2", hue="category")
    sns.regplot(data=df, x="value", y="value2", scatter=False, color="gray")
    plt.title("Value vs Value2")
    plt.tight_layout()
    plt.savefig("results/value_vs_value2.png")
    plt.close()


def main():
    df = load_data()
    basic_eda(df)
    example_plots(df)
    print("Example plots saved in ./results/")


if __name__ == "__main__":
    main()
