# Electricity Consumption Analyzer - simple version

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------- Step 1: Read the CSV file ----------
file_name = input("Enter CSV file name (default usage.csv): ")
if file_name == "":
    file_name = "usage.csv"

try:
    data = pd.read_csv(file_name, header=None, names=["Month", "Units"], dtype=str)
except FileNotFoundError:
    print("File not found!")
    exit()

# If the file has a header row (Month,Units), remove it
if data.iloc[0]["Month"] == "Month":
    data = data.iloc[1:]

# ---------- Step 2: Clean the data ----------
months = []   # valid months
units = []    # valid units

row_no = 1
for m, u in zip(data["Month"], data["Units"]):
    try:
        u = float(u)               # try to convert to number
        if u < 0:
            print("Row", row_no, "skipped: Units cannot be negative.")
        else:
            months.append(m)
            units.append(u)
    except (ValueError, TypeError):
        print("Row", row_no, "skipped: invalid Units '" + str(u) + "'.")
    row_no = row_no + 1

# Make a clean table with only valid rows
df = pd.DataFrame({"Month": months, "Units": units})

if len(df) == 0:
    print("No valid data found.")
    exit()

# Show valid row count only if some rows were skipped
if len(df) != len(data):
    print("Valid rows:", len(df), "| Total:", int(df["Units"].sum()), "units")

# ---------- Step 3: Calculations using NumPy ----------
arr = np.array(df["Units"])
total = np.sum(arr)
average = np.mean(arr)
highest = np.max(arr)
lowest = np.min(arr)
std_dev = np.std(arr)    # population standard deviation

# Find which month is highest / lowest
high_month = df["Month"][df["Units"] == highest].iloc[0]
low_month = df["Month"][df["Units"] == lowest].iloc[0]

# ---------- Step 4: Menu ----------
while True:
    print()
    print("1. Summary")
    print("2. Above-average months and chart")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Total:", int(total), "units | Average:", f"{average:.2f}")
        print("Highest:", high_month, "(" + str(int(highest)) + ") | Lowest:",
              low_month, "(" + str(int(lowest)) + ")")
        print("Std Dev:", f"{std_dev:.2f}")

    elif choice == "2":
        # Boolean filtering: keep only rows where Units > average
        above = df[df["Units"] > average]
        text = ""
        for m, u in zip(above["Month"], above["Units"]):
            text = text + m + " (" + str(int(u)) + "), "
        print("Months above average (" + f"{average:.2f}" + "):", text.rstrip(", "))

        # Bar chart
        plt.figure()
        plt.bar(df["Month"], df["Units"], color="skyblue")
        plt.title("Monthly Consumption")
        plt.xlabel("Month")
        plt.ylabel("Units")
        print("Bar chart 'Monthly Consumption' displayed")

        # Line chart
        plt.figure()
        plt.plot(df["Month"], df["Units"], marker="o")
        plt.title("Consumption Trend")
        plt.xlabel("Month")
        plt.ylabel("Units")

        plt.show()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Enter 1, 2 or 3.")