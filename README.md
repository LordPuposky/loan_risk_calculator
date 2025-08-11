**Loan Risk Simulator**

**Overview**

This Python project simulates a credit risk evaluation process for loan applicants.
It calculates the Debt-to-Income Ratio (DTI), evaluates credit score ranges, and estimates the probability of loan approval using a weighted scoring system.
The project includes data visualization with Matplotlib to better understand applicant risk profiles.

**Features**

DTI Calculation – Computes the debt-to-income ratio for each applicant.

Credit Score Categorization – Classifies credit scores into standard ranges.

Loan Approval Probability – Uses credit score, DTI, and employment history to estimate approval chances.

CSV Data Loading – Reads applicant data from a CSV file.

Visualization – Generates bar charts comparing approval probabilities.

Unit Testing – Includes pytest tests for core functions.

**Technologies Used**

Python 3

Matplotlib – Data visualization

Pytest – Unit testing

CSV Module – Data handling

**Project Structure**

<img width="373" height="243" alt="image" src="https://github.com/user-attachments/assets/6df0e077-76cb-4865-b0af-3660be64ba30" />

**Installation & Usage**

Clone the repository

git clone https://github.com/yourusername/credit_risk_project.git

cd credit_risk_project
Create a virtual environment
python -m venv venv
Activate the virtual environment

**Windows:**

venv\Scripts\activate

**Mac/Linux:**

source venv/bin/activate
Install dependencies
pip install -r requirements.txt
Run the program
python main.py

Run tests
pytest

**Example Output**

The program generates:

A console report with DTI, credit score category, and approval probability for each applicant.

A bar chart comparing approval probabilities.

**Testing**

The project includes unit tests for:

calculate_dti()

evaluate_credit_score_range()

loan_approval_probability()

Run:

pytest

**Future Improvements**

Add a GUI for easier data entry.

Integrate with a real credit scoring API.

Implement risk thresholds for automated decision-making.

**License**

This project is for educational purposes as part of the CSE111 Programming with Functions course at BYU Pathway.
