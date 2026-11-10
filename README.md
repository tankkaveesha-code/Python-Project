# Electricity Consumption Analyzer

**Name:** Kaveesha Tank
**ERP:** RU-26-00345
**Class:** 1L
**Project:** PS 18 - Electricity Consumption Analyzer

## About the Project
This Python program reads monthly electricity usage from a CSV file and analyses it. It finds the total and average usage, the highest and lowest months, the standard deviation, and the months above average. It also shows the trend using charts.

## Technologies Used
- Python 3
- NumPy
- Pandas
- Matplotlib

## Files in this Repository
- `one.py` - the main Python program
- `usage.csv` - sample input data
- `README.md` - project description
- `Summary.md` - implementation details and test case screenshots

## How to Run
1. Install the libraries:
   `pip install numpy pandas matplotlib`
2. Keep `one.py` and `usage.csv` in the same folder.
3. Run the program:
   `python one.py`
4. Press Enter to use `usage.csv`, then choose an option.

## Menu Options
1. **Summary** - total, average, highest, lowest and standard deviation
2. **Above-average months and chart** - shows months above average, a bar chart and a line chart
3. **Exit**

## Input Format
The CSV file has two columns, Month and Units:
Jan,200
Feb,250
Mar,300

## Sample Output
Total: 750 units | Average: 250.00
Highest: Mar (300) | Lowest: Jan (200)
Std Dev: 40.82

## Error Handling
- Rows with invalid units (like `abc`) are skipped
- Rows with negative units are skipped
- A message is shown if the file is not found