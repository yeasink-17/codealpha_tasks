# Stock Portfolio Tracker 📈

A simple console stock tracker built in Python as part of the **CodeAlpha Python Programming Internship** (Task 2).

## What It Does
- Shows a list of stocks with hardcoded prices (e.g. `{"AAPL": 180, "TSLA": 250}`).
- You type stock names and how many shares you own.
- It calculates the value of each stock and your total investment.
- Optionally saves the result to `portfolio.csv`.

## Features
- Case-insensitive stock names (`aapl` works the same as `AAPL`)
- Rejects unknown stocks and invalid quantities
- Adds up quantities if you enter the same stock twice
- Saves a clean CSV summary with a total row

## How to Run
1. Install Python 3
2. Run: `python stock_portfolio.py`
3. Type `done` when you have finished entering stocks.

## Concepts Used
Dictionary, input/output, basic arithmetic, file handling (`csv`)

## Author
Yeasin Khan
