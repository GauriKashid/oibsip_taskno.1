import tkinter as tk
from tkinter import messagebox

class BMI_Calculator:
    def __init__(self):
        self.history = []

    def calculate_bmi(self, weight, height):
        return weight / (height ** 2)

    def category(self, bmi):
        if bmi < 18.5:
            return 'Underweight'
        elif bmi < 24.9:
            return 'Normal weight'
        elif bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'

    def add_to_history(self, weight, height, bmi, category):
        self.history.append({"Weight": weight, "Height": height, "BMI": bmi, "Category": category})

    def display_history(self):
        if not self.history:
            return "There is no history available."
        else:
            history_text = "Historical data\n"
            for record in self.history:
                history_text += f"{record['Weight']}\t\t{record['Height']}\t\t{record['BMI']:.2f}\t\t{record['Category']}\n"
            return history_text

def calculate_bmi_command():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter valid input")
        return

    bmi = bmi_calculator.calculate_bmi(weight, height)
    category = bmi_calculator.category(bmi)
    
    result_obtained.config(text=f"BMI report is: {bmi:.2f}")
    bmi_calculator.add_to_history(weight, height, bmi, category)
    clear_fields()

def display_history_command():
    history_text = bmi_calculator.display_history()
    history_label.config(text=history_text)

def clear_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)

def create_boxes(root):
    weight_label = tk.Label(root, text="Weight (kg):")
    weight_label.grid(row=2, column=0)

    global weight_entry
    weight_entry = tk.Entry(root)
    weight_entry.grid(row=2, column=1)

    height_label = tk.Label(root, text="Height (m):")
    height_label.grid(row=5, column=0)

    global height_entry
    height_entry = tk.Entry(root)
    height_entry.grid(row=5, column=1)

    calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi_command)
    calculate_button.grid(row=7, column=0, columnspan=2)

    global result_obtained
    result_obtained= tk.Label(root, text="")
    result_obtained.grid(row=8, column=0, columnspan=2)

    view_history_button = tk.Button(root, text="View History", command=display_history_command)
    view_history_button.grid(row=15, column=0, columnspan=2)

    global history_label
    history_label = tk.Label(root, text="")
    history_label.grid(row=10, column=0, columnspan=2)

if __name__ == "__main__":
    bmi_calculator = BMI_Calculator()
    root = tk.Tk()
    root.title("BMI Calculator")
    create_boxes(root)
    root.mainloop()
