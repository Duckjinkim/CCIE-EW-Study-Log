import tkinter as tk
from datetime import datetime, timedelta
import os
import subprocess
import threading

# Global variables
start_time = None
timer_running = False
paused = False
elapsed_time = timedelta(0)  # Accumulated time
last_start_time = None
timer_thread = None
section_times = {f"Section {i}": None for i in range(1, 7)}  # Completion time for each section
section_labels = {}  # Labels for section times

# Log file path
log_file = r"Z:\CCIE EW\CCIE-EW-Study-Log\CCIE-EW-Study-log.txt"

def update_timer():
    """Update elapsed time in real-time"""
    global elapsed_time, last_start_time, timer_running
    while timer_running:
        if last_start_time:
            current_elapsed = datetime.now() - last_start_time
            total_elapsed = elapsed_time + current_elapsed
            hours, remainder = divmod(total_elapsed.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            elapsed_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            elapsed_time_label.config(text=f"Current Elapsed Time: {elapsed_str}")
        window.update()
        window.after(1000)  # Update every second

def start_lab():
    """Start or resume the lab"""
    global start_time, last_start_time, timer_running, paused, timer_thread
    if not timer_running:
        if paused:
            # Resume from paused state
            last_start_time = datetime.now()
        else:
            # Start fresh
            start_time = datetime.now()
            last_start_time = start_time
        status_label.config(text=f"Lab Started: {start_time.strftime('%Y-%m-%d %H:%M:%S')}", fg="#00ff00")
        timer_running = True
        paused = False
        # Start timer thread
        timer_thread = threading.Thread(target=update_timer)
        timer_thread.daemon = True
        timer_thread.start()

def stop_lab():
    """Pause the lab"""
    global elapsed_time, last_start_time, timer_running, paused
    if not last_start_time:
        status_label.config(text="Please start the lab first!", fg="#ff0000")
        return
    
    # Accumulate elapsed time
    current_elapsed = datetime.now() - last_start_time
    elapsed_time += current_elapsed
    last_start_time = None
    timer_running = False
    paused = True
    status_label.config(text="Lab Paused", fg="#ffcc00")

def section_checked(section):
    """Record time for the selected section"""
    global elapsed_time, last_start_time
    if not last_start_time and not paused:
        status_label.config(text="Please start the lab first!", fg="#ff0000")
        return
    
    # Calculate elapsed time
    if last_start_time:
        current_elapsed = datetime.now() - last_start_time
        total_elapsed = elapsed_time + current_elapsed
    else:
        total_elapsed = elapsed_time
    
    # Record section time
    hours, remainder = divmod(total_elapsed.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    elapsed_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    section_times[section] = elapsed_str
    section_labels[section].config(text=f"{section}: {elapsed_str}")

def exit_app():
    """Exit the app and save records to GitHub"""
    global elapsed_time, last_start_time, timer_running, start_time
    timer_running = False
    
    # If start_time is None, set it to current time
    if start_time is None:
        start_time = datetime.now()
    
    # Calculate final elapsed time
    if last_start_time:
        current_elapsed = datetime.now() - last_start_time
        elapsed_time += current_elapsed
    
    # Ensure at least 1 minute is recorded
    if elapsed_time.total_seconds() < 60:  # Less than 1 minute
        elapsed_time = timedelta(seconds=60)  # Set to 1 minute
    
    # Calculate total hours
    hours = elapsed_time.total_seconds() / 3600
    
    # Save to log file
    log_entry = f"{start_time.strftime('%Y-%m-%d')}: {hours:.2f} hours - CCIE EW Lab\n"
    log_entry += "Section Times:\n"
    for section, time in section_times.items():
        if time:
            log_entry += f"  {section}: {time}\n"
    
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry)
    
    # Commit and push to GitHub
    commit_and_push(log_entry)
    
    # Exit the app
    window.destroy()

def commit_and_push(log_entry):
    """Commit and push to GitHub"""
    os.chdir(r"Z:\CCIE EW\CCIE-EW-Study-Log")
    subprocess.run(["git", "add", "CCIE-EW-Study-log.txt"], check=True)
    subprocess.run(["git", "commit", "-m", f"Lab Record: {log_entry.splitlines()[0]}"], check=True)
    subprocess.run(["git", "push", "origin", "master"], check=True)  # Branch is master

# GUI creation
window = tk.Tk()
window.title("CCIE EW Study LAB Time")
window.geometry("800x600")  # Window size
window.configure(bg="#1e1e2f")  # Dark theme background
window.resizable(True, True)  # Allow window resizing

# Main frame (for centering)
main_frame = tk.Frame(window, bg="#1e1e2f")
main_frame.pack(fill="both", expand=True)

# Elapsed time label (centered, now at the top)
elapsed_time_label = tk.Label(main_frame, text="Current Elapsed Time: 00:00:00", font=("Arial", 40, "bold"), fg="#ff0000", bg="#1e1e2f", highlightbackground="#ff0000", highlightthickness=2)
elapsed_time_label.pack(pady=5)  # Reduced padding

# Title label (centered, now below elapsed time)
title_label = tk.Label(main_frame, text="CCIE EW Study LAB Time", font=("Arial", 30, "bold"), fg="#00b7eb", bg="#1e1e2f")
title_label.pack(pady=5)  # Reduced padding

# Status label (centered)
status_label = tk.Label(main_frame, text="Start the Lab!", font=("Arial", 16), fg="#ffffff", bg="#1e1e2f")
status_label.pack(pady=10)

# Section checkboxes frame (centered)
section_frame = tk.Frame(main_frame, bg="#1e1e2f")
section_frame.pack(pady=10)

# Section checkboxes (2 columns, centered)
for i in range(1, 7):
    section = f"Section {i}"
    var = tk.BooleanVar()
    col = 0 if i <= 3 else 1
    row = (i-1) % 3
    chk = tk.Checkbutton(section_frame, text=section, variable=var, command=lambda s=section: section_checked(s), font=("Arial", 14), fg="#ffffff", bg="#1e1e2f", selectcolor="#1e1e2f")
    chk.grid(row=row*2, column=col, padx=20, pady=5)
    # Section time label
    time_label = tk.Label(section_frame, text=f"{section}: --:--:--", font=("Arial", 12), fg="#ffcc00", bg="#1e1e2f")
    time_label.grid(row=row*2+1, column=col, padx=20, pady=5)
    section_labels[section] = time_label

# Button frame (centered)
button_frame = tk.Frame(main_frame, bg="#1e1e2f")
button_frame.pack(pady=20)

# Button style
button_style = {"font": ("Arial", 14, "bold"), "width": 10, "height": 3, "bd": 2, "relief": "raised", "borderwidth": 3}

# Start button
start_button = tk.Button(button_frame, text="Start", command=start_lab, bg="#4caf50", fg="white", **button_style)
start_button.grid(row=0, column=0, padx=20)

# Stop button
stop_button = tk.Button(button_frame, text="Stop", command=stop_lab, bg="#f44336", fg="white", **button_style)
stop_button.grid(row=0, column=1, padx=20)

# Exit button
exit_button = tk.Button(button_frame, text="Exit", command=exit_app, bg="#607d8b", fg="white", **button_style)
exit_button.grid(row=0, column=2, padx=20)

# Run the window
window.mainloop()