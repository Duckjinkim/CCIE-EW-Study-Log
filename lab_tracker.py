import tkinter as tk
from datetime import datetime
import os
import subprocess

# 전역 변수
start_time = None
log_file = r"Z:\CCIE EW\CCIE-EW-Study-Log\CCIE-EW-Study-log.txt"  # 파일 경로 지정

def start_lab():
    global start_time
    start_time = datetime.now()
    status_label.config(text="랩 시작: " + start_time.strftime("%Y-%m-%d %H:%M:%S"))

def stop_lab():
    global start_time
    if start_time is None:
        status_label.config(text="먼저 랩을 시작하세요!")
        return
    
    end_time = datetime.now()
    duration = end_time - start_time
    hours = duration.total_seconds() / 3600  # 시간을 시간 단위로 변환
    
    # 기록 파일에 추가
    log_entry = f"{start_time.strftime('%Y-%m-%d')}: {hours:.2f}시간 - CCIE EW 랩\n"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry)
    
    # Git 커밋 및 푸시
    commit_and_push(log_entry)
    
    status_label.config(text=f"랩 종료: {hours:.2f}시간 기록됨")
    start_time = None

def commit_and_push(log_entry):
    # 작업 디렉토리를 지정된 경로로 변경
    os.chdir(r"Z:\CCIE EW\CCIE-EW-Study-Log")
    subprocess.run(["git", "add", "CCIE-EW-Study-log.txt"], check=True)
    subprocess.run(["git", "commit", "-m", f"랩 기록: {log_entry.strip()}"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)

# GUI 생성
window = tk.Tk()
window.title("CCIE EW 랩 트래커")
window.geometry("300x150")

status_label = tk.Label(window, text="랩을 시작하세요!", font=("Arial", 12))
status_label.pack(pady=20)

start_button = tk.Button(window, text="랩 시작", command=start_lab, font=("Arial", 10))
start_button.pack(pady=5)

stop_button = tk.Button(window, text="랩 중지", command=stop_lab, font=("Arial", 10))
stop_button.pack(pady=5)

window.mainloop()