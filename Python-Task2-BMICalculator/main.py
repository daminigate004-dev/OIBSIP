import tkinter as tk
from database import create_database, save_bmi_record, get_bmi_history
import matplotlib.pyplot as plt

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x550")

# Heading
title_label = tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=20)

# Name
name_label = tk.Label(
    root,
    text="Name:"
)
name_label.pack()

name_entry = tk.Entry(
    root,
    width=30
)
name_entry.pack(pady=5)

# Weight
weight_label = tk.Label(
    root,
    text="Weight (kg):"
)
weight_label.pack()

weight_entry = tk.Entry(
    root,
    width=30
)
weight_entry.pack(pady=5)

# Height
height_label = tk.Label(
    root,
    text="Height (m):"
)
height_label.pack()

height_entry = tk.Entry(
    root,
    width=30
)
height_entry.pack(pady=5)

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        # Check for invalid values
        if weight <= 0:
            result_label.config(
                text="Error: Weight must be greater than 0."
            )
            return

        if height <= 0:
            result_label.config(
                text="Error: Height must be greater than 0."
            )
            return

        # Calculate BMI
        bmi = weight / (height ** 2)

        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        # Display result
        result_label.config(
            text=f"BMI: {bmi:.2f}\nCategory: {category}"
        )
        # Save the BMI record
        name = name_entry.get().strip()

        if name:
            save_bmi_record(
                name,
                weight,
                height,
                bmi,
                category
            )
    
    except ValueError:
        result_label.config(
            text="Error: Please enter valid numbers."
        )

# Function to view BMI history
def view_history():
    records = get_bmi_history()

    history_window = tk.Toplevel(root)
    history_window.title("BMI History")
    history_window.geometry("700x400")

    history_label = tk.Label(
        history_window,
        text="BMI History",
        font=("Arial", 18, "bold")
    )
    history_label.pack(pady=10)

    if not records:
        empty_label = tk.Label(
            history_window,
            text="No BMI records found."
        )
        empty_label.pack(pady=20)
        return

    history_text = tk.Text(
        history_window,
        width=80,
        height=18
    )
    history_text.pack(padx=10, pady=10)

    for record in records:
        name, weight, height, bmi, category, date = record

        history_text.insert(
            tk.END,
            f"Name: {name}\n"
            f"Weight: {weight} kg | Height: {height} m\n"
            f"BMI: {bmi:.2f} | Category: {category}\n"
            f"Date: {date}\n"
            f"{'-' * 60}\n"
        )

    history_text.config(state="disabled")

# Function to show BMI trend graph
def show_bmi_trend():
    records = get_bmi_history()

    if not records:
        result_label.config(
            text="No BMI records available for graph."
        )
        return

    names = []
    bmi_values = []

    for record in records:
        name, weight, height, bmi, category, date = record

        names.append(date)
        bmi_values.append(bmi)

    plt.figure(figsize=(8, 5))
    plt.plot(names, bmi_values, marker="o")

    plt.title("BMI Trend")
    plt.xlabel("Date")
    plt.ylabel("BMI")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()

# Calculate BMI button
calculate_button = tk.Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi
)
calculate_button.pack(pady=20)

# View History button
history_button = tk.Button(
    root,
    text="View History",
    command=view_history
)
history_button.pack(pady=10)

# BMI Trend button
trend_button = tk.Button(
    root,
    text="BMI Trend",
    command=show_bmi_trend
)
trend_button.pack(pady=10)

# Result
result_label = tk.Label(
    root,
    text="BMI: "
)
result_label.pack(pady=10)

# Create the database
create_database()

# Keep the application running
root.mainloop()