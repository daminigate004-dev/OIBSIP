# Advanced BMI Calculator

## Project Overview

This project is an Advanced BMI Calculator developed using Python.

The application provides a graphical user interface (GUI) that allows users to enter their name, weight, and height. It calculates the user's Body Mass Index (BMI) and displays the corresponding BMI category.

The application also stores BMI records in an SQLite database and provides features to view BMI history and display BMI trends using a graph.

## Features

- User-friendly graphical interface using Tkinter
- Multiple-user BMI records
- BMI calculation
- BMI category classification
- Input validation and error handling
- SQLite database for storing BMI records
- BMI history display
- BMI trend graph using Matplotlib

## BMI Categories

| BMI Range | Category |
|---|---|
| Below 18.5 | Underweight |
| 18.5 – 24.9 | Normal |
| 25 – 29.9 | Overweight |
| 30 and above | Obese |

## Technologies Used

- Python 3
- Tkinter
- SQLite
- Matplotlib

## Project Structure

```text
Python-Task2-BMICalculator/
│
├── main.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
    ├── main-window.png
    ├── bmi-result.png
    ├── validation-error.png
    ├── bmi-history.png
    └── bmi-trend.png