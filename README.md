# CCIE EW Study LAB Time Tracker

## Overview
Welcome to the **CCIE EW Study LAB Time Tracker**! This project is a part of my journey as a network engineer preparing for the **CCIE Enterprise Wireless (EW)** certification. As a network engineer, I created this tool to track my study time, visualize my progress, and enhance my time management skills—crucial for the CCIE LAB exam. This repository serves as a portfolio piece to demonstrate my dedication to CCIE preparation, my ability to manage time effectively, and my skills in Python programming for automation.

### Why I Built This
The CCIE LAB exam is a rigorous 5-hour test that demands exceptional time management, troubleshooting, problem-solving, implementation, deployment, and design skills under pressure. To succeed, I needed a tool to:
- **Track Study Time**: Monitor how much time I spend on CCIE lab practice to ensure consistent progress.
- **Visualize Contributions**: Use GitHub Contributions to visually represent my study efforts over time.
- **Practice Time Management**: Simulate the time constraints of the CCIE LAB exam by tracking and optimizing my lab sessions.
- **Enhance Lab Skills**: Focus on troubleshooting, identifying issues, meeting requirements, implementing solutions, deploying configurations, and designing networks within a short timeframe.

In CCIE preparation, **lab practice is paramount**. The ability to efficiently manage time while solving complex network scenarios is a critical skill for the exam and real-world network engineering. This tool helps me practice these skills by providing a structured way to record my lab sessions, ensuring I am well-prepared for the CCIE LAB exam.

## How It Works
The **CCIE EW Study LAB Time Tracker** is a Python-based application built with  for the GUI. It tracks the time spent on lab practice sessions and automatically logs the data to a file (), which is then pushed to this GitHub repository. Here's how it operates:

- **Start/Stop Timer**: Use the "Start" button to begin a lab session and the "Stop" button to pause it. The timer tracks your elapsed time in real-time.
- **Section Tracking**: The app includes sections (Section 1 to Section 6) to mark the completion of specific lab tasks. When a section is checked, the elapsed time at that moment is recorded.
- **Automatic GitHub Updates**: Every action (Start, Stop, Section completion, Exit) triggers an update to the log file, which is then committed and pushed to GitHub. This ensures that my study progress is continuously reflected in my GitHub Contributions.
- **Minimum Time Logging**: Even if you exit immediately after starting, the app logs a minimum of 1 minute to ensure consistent tracking.

### Key Features
- **Real-Time Timer**: Displays the current elapsed time during lab sessions.
- **Section-Based Tracking**: Records the time taken to complete each section of the lab.
- **GitHub Integration**: Automatically commits and pushes updates to GitHub, visualizing study progress through Contributions.
- **Time Management Practice**: Helps simulate the time constraints of the CCIE LAB exam, improving efficiency in troubleshooting, implementation, and design.

## How to Use
This tool is designed to be user-friendly and accessible to anyone preparing for the CCIE or similar certifications. Follow these steps to use it:

### Prerequisites
- **Python 3.x**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **Git**: Install Git to interact with the GitHub repository. Download it from [git-scm.com](https://git-scm.com/).
- **GitHub Account**: You'll need a GitHub account to clone and push updates to your repository.

### Setup
1. **Clone the Repository**:
   

2. **Run the Application**:
   

3. **Usage**:
   - **Start a Session**: Click the "Start" button to begin tracking your lab time.
   - **Pause a Session**: Click the "Stop" button to pause the timer.
   - **Mark Sections**: Check the boxes (Section 1 to Section 6) to record the time taken for each section.
   - **Exit and Save**: Click the "Exit" button to save your session data and push it to GitHub.

### Customization
- **Log File Path**: Modify the  variable in  to change where the log is saved.
- **Sections**: Adjust the  dictionary to add or remove sections as needed.

## Why This Matters for CCIE Preparation
The CCIE LAB exam is a 5-hour test that requires candidates to troubleshoot, implement, deploy, and design network solutions under strict time constraints. Time management is a critical skill, as you must:
- **Troubleshoot Quickly**: Identify and resolve issues within minutes.
- **Implement Efficiently**: Configure networks to meet specific requirements.
- **Design and Deploy**: Create and deploy solutions that align with best practices.

This tool helps me practice these skills by simulating the time pressure of the exam. By tracking my lab sessions and visualizing my progress on GitHub, I can ensure I'm dedicating enough time to preparation and improving my efficiency.

## For Network Engineers
This project is not just for me—it's for any network engineer preparing for the CCIE or similar certifications. Whether you're studying for CCIE Enterprise Wireless, Enterprise Infrastructure, or another track, this tool can help you:
- Track your study time and ensure consistent practice.
- Visualize your progress through GitHub Contributions.
- Practice time management under simulated exam conditions.

Feel free to fork this repository, customize it for your needs, and use it as part of your own CCIE preparation journey. Contributions and feedback are welcome!

## My CCIE Journey
As of March 29, 2025, I have been diligently preparing for the CCIE Enterprise Wireless certification. This repository reflects my commitment to lab practice, with each commit representing a study session. By visualizing my contributions, I can see how much time I've invested and identify areas for improvement. My goal is to master the skills needed to pass the CCIE LAB exam and become a certified network expert.

## License
This project is open-source and available under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as needed.
## Contact
If you have questions, suggestions, or want to collaborate, feel free to reach out:
- GitHub: [DJ Kim](https://github.com/Duckjinkim)
- Email: [ccie68155@gmail.com](mailto:ccie68155@gmail.com)
- LinkedIn: https://www.linkedin.com/in/dj-duckjin-kim-55727827b/
- Blog: https://ccie68155.tistory.com/

Happy studying, and good luck on your CCIE journey!
