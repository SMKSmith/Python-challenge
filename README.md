# Python-challenge

* PyBank: Analysis of monthly profit and loss data
* PyPoll: Analysis of election results

## PyBank

In this project I created a Python script for analyzing the financial profit and loss records of PyBank. 

![revenue-per-lead](https://user-images.githubusercontent.com/117343047/212153647-cf28bfc3-5b6e-4692-9578-8e2f0e6f4120.png)

The analyzed dataset [budget_data.csv](PyBank/Resources/budget_data.csv) is composed of two columns: "Date" and "Profit/Losses".

 * The Python script is to analyze the records to calculate the following:

  - [x] The total number of months included in the dataset

  - [x] The net total amount of "Profit/Losses" over the entire period

  - [x] The changes in "Profit/Losses" over the entire period, and then the average of those changes

  - [x] The greatest increase in profits (date and amount) over the entire period

  - [x] The greatest decrease in profits (date and amount) over the entire period

```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $22564198
  Average Change: $-8311.11
  Greatest Increase in Profits: Aug-16 ($1862002)
  Greatest Decrease in Profits: Feb-14 ($-1825558)
  ```


  ## PyPoll
  In this project I helped a small, rural town modernize its vote counting process.

  ![Vote_counting](https://user-images.githubusercontent.com/117343047/212500741-fb255598-793b-4c30-87c6-cb6e21302100.png)

The dataset given was a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: "Voter ID", "County", and "Candidate".

* Python script that analyzes the votes and calculates each of the following:

  - [x] The total number of votes cast

  - [x]A complete list of candidates who received votes

  - [x] The percentage of votes each candidate won

  - [x] The total number of votes each candidate won

  - [x] The winner of the election based on popular vote.


 ```text
  Election Results
  -------------------------
  Total Votes: 369711
  -------------------------
  Charles Casper Stockham: 23.049% (85213)
  Diana DeGette: 73.812% (272892)
  Raymon Anthony Doane: 3.139% (11606)
  -------------------------
  Winner: Diana DeGette
  -------------------------
  ```