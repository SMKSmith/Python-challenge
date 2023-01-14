# Python-challenge

* PyBank: Analysis of monthly profit and loss data
* PyPoll: Analysis of election results

## PyBank


![revenue-per-lead](https://user-images.githubusercontent.com/117343047/212153647-cf28bfc3-5b6e-4692-9578-8e2f0e6f4120.png)

* In this project I created a Python script for analyzing the financial profit and loss records of PyBank. The analyzed dataset [budget_data.csv](PyBank/Resources/budget_data.csv) is composed of two columns: "Date" and "Profit/Losses".

* The Python script is to analyze the records to calculate the following:

** The total number of months included in the dataset

** The net total amount of "Profit/Losses" over the entire period

** The changes in "Profit/Losses" over the entire period, and then the average of those changes

** The greatest increase in profits (date and amount) over the entire period

** The greatest decrease in profits (date and amount) over the entire period

```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $22564198
  Average Change: $-8311.11
  Greatest Increase in Profits: Aug-16 ($1862002)
  Greatest Decrease in Profits: Feb-14 ($-1825558)
  ```