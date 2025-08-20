import customtkinter as ctk
from tkinter import messagebox
import time
import threading

# Set theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# App window
app = ctk.CTk()
app.title("FocusFlow - ToDo + Timer")
app.geometry("500x600")

# ---------- Task Manager ----------
tasks = []

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert("end", task)
        tasks.append(task)
        task_entry.delete(0, "end")
    else:
        messagebox.showwarning("Input Error", "Enter a task.")

def remove_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected[0])
        del tasks[selected[0]]

# ---------- Timer ----------
timer_running = False
def start_timer():
    global timer_running
    if not timer_running:
        timer_running = True
        threading.Thread(target=run_timer).start()

def stop_timer():
    global timer_running
    timer_running = False
    timer_label.configure(text="25:00")

def run_timer():
    total_seconds = 25 * 60
    while total_seconds > 0 and timer_running:
        mins, secs = divmod(total_seconds, 60)
        timer_label.configure(text=f"{mins:02d}:{secs:02d}")
        time.sleep(1)
        total_seconds -= 1
    if timer_running:
        messagebox.showinfo("Time's up!", "Focus session complete!")
    stop_timer()

# ---------- Layout ----------

title = ctk.CTkLabel(app, text="🧠 FocusFlow", font=("Segoe UI", 30, "bold"))
title.pack(pady=20)

# To-do section
task_entry = ctk.CTkEntry(app, placeholder_text="Enter a task...", width=300)
task_entry.pack(pady=10)

btn_frame = ctk.CTkFrame(app, fg_color="transparent")
btn_frame.pack()

add_btn = ctk.CTkButton(btn_frame, text="Add Task", command=add_task)
add_btn.grid(row=0, column=0, padx=5)

remove_btn = ctk.CTkButton(btn_frame, text="Remove Selected", command=remove_task)
remove_btn.grid(row=0, column=1, padx=5)

task_listbox = ctk.CTkScrollableFrame(app, height=200)
task_listbox.pack(pady=10, padx=20, fill="both", expand=True)

def insert_tasks():
    for task in tasks:
        task_listbox.insert("end", task)

# Timer section
timer_label = ctk.CTkLabel(app, text="25:00", font=("Segoe UI", 40, "bold"))
timer_label.pack(pady=30)

timer_buttons = ctk.CTkFrame(app, fg_color="transparent")
timer_buttons.pack()

start_btn = ctk.CTkButton(timer_buttons, text="Start Timer", command=start_timer)
start_btn.grid(row=0, column=0, padx=10)

stop_btn = ctk.CTkButton(timer_buttons, text="Stop", command=stop_timer)
stop_btn.grid(row=0, column=1, padx=10)

app.mainloop()
