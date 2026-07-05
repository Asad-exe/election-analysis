import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load data
df = pd.read_csv('../data/cleaned_data.csv')

# Main window
root = tk.Tk()
root.title("Pakistan 2018 Election Dashboard")
root.geometry("900x650")

# --- Top frame: controls ---
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

tk.Label(control_frame, text="Select Province:", font=("Arial", 12)).grid(row=0, column=0, padx=5)

province_options = ["All"] + sorted(df['province'].unique().tolist())
province_var = tk.StringVar(value="All")
province_dropdown = ttk.Combobox(control_frame, textvariable=province_var, values=province_options, state="readonly")
province_dropdown.grid(row=0, column=1, padx=5)

tk.Label(control_frame, text="Select Chart:", font=("Arial", 12)).grid(row=0, column=2, padx=5)

chart_options = ["Turnout by Province", "Seats by Party", "Turnout vs Margin"]
chart_var = tk.StringVar(value="Turnout by Province")
chart_dropdown = ttk.Combobox(control_frame, textvariable=chart_var, values=chart_options, state="readonly")
chart_dropdown.grid(row=0, column=3, padx=5)

# --- Chart area ---
chart_frame = tk.Frame(root)
chart_frame.pack(fill="both", expand=True)

canvas = None

def draw_chart():
    global canvas
    if canvas:
        canvas.get_tk_widget().destroy()

    selected_province = province_var.get()
    selected_chart = chart_var.get()

    if selected_province == "All":
        data = df
    else:
        data = df[df['province'] == selected_province]

    fig, ax = plt.subplots(figsize=(8, 5))

    if selected_chart == "Turnout by Province":
        grouped = df.groupby('province')['turnout'].mean().sort_values(ascending=False)
        ax.bar(grouped.index, grouped.values, color='steelblue')
        ax.set_title("Average Turnout by Province")
        ax.set_ylabel("Turnout")
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

    elif selected_chart == "Seats by Party":
        party_counts = data['win_party'].value_counts().head(6)
        ax.barh(party_counts.index, party_counts.values, color='seagreen')
        ax.set_title(f"Seats by Party ({selected_province})")
        ax.set_xlabel("Seats")
        ax.invert_yaxis()

    elif selected_chart == "Turnout vs Margin":
        data = data.copy()
        data['margin'] = data['win_pct'] - data['second_pct']
        ax.scatter(data['turnout'], data['margin'], alpha=0.6, color='darkorange')
        ax.set_title(f"Turnout vs Margin ({selected_province})")
        ax.set_xlabel("Turnout")
        ax.set_ylabel("Winning Margin")

    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)
    plt.close(fig)

update_btn = tk.Button(control_frame, text="Update Chart", command=draw_chart, bg="#4CAF50", fg="white")
update_btn.grid(row=0, column=4, padx=10)

# Draw initial chart
draw_chart()

root.mainloop()