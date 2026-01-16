# Streamlit Crash Course Projects

## Description
This repository contains a structured learning path to master **Streamlit** through hands-on projects and exercises. It covers fundamental concepts and builds up to interactive, professional-level applications using Python core libraries such as **Streamlit**, **pandas**, and **numpy**.

You will learn how to create interactive apps, build dashboards, work with real data, and deploy your applications — all from a single Python file per app. This project is based on tutorials from a YouTube Streamlit crash course.

---

## Learning Objectives
By completing this project, you will be able to:  

- **Set up and run Streamlit projects locally.**  
- **Build interactive user interfaces** with forms, sliders, buttons, and dropdowns.  
- **Structure apps** with layouts like columns, sidebars, and expanders.  
- **Load, filter, and display real data** using pandas.  
- **Create dashboards** with KPI cards and charts using only built-in Streamlit features.  
- **Deploy Streamlit apps** to Streamlit Cloud.  

---

## Prerequisites
- Basic knowledge of Python programming.  
- Familiarity with HTML, CSS, and JavaScript is helpful but not required.  

---

## Project Structure / Table of Contents

| File | Description |
|------|-------------|
| `lecture1.py` | Introduction to Streamlit and basic components |
| `lecture2.py` | Widgets and input elements (checkbox, radio, selectbox, slider, etc.) |
| `lecture3.py` | Layouts, styling, and columns |
| `lecture4.py` | Working with real datasets using pandas |
| `lecture5.py` | API integration and dynamic content |
| `demo-dashboard.py` | Dashboards with KPI cards and charts |

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/streamlit-crash-course.git
cd streamlit-crash-course
Create and activate a virtual environment

bash
Copy code
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Install dependencies

bash
Copy code
pip install -r requirements.txt
Ensure requirements.txt contains at least:

txt
Copy code
streamlit
pandas
numpy
Usage
Run any of the apps locally using Streamlit:

bash
Copy code
streamlit run lecture1.py
Replace lecture1.py with the file you want to open.

The terminal will provide a local URL (usually http://localhost:8501) to view the app in your browser.


Credits
This repository and learning path are based on the Streamlit Crash Course with Showcase Projects by Chai aur Code. Special thanks to the creator for the structured tutorials that guided the development of this project.

License
This project is licensed under the MIT License. See LICENSE for details.
