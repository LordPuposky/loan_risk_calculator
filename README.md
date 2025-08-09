**Loan Risk Calculator**

A Python-based tool that simulates the credit risk evaluation process for personal loans.  
The program calculates key financial indicators such as **Debt-to-Income Ratio (DTI)** and estimates an **approval probability** based on a simplified model used in FinTech.

---

**Features**
- Calculates **Debt-to-Income Ratio (DTI)**.
- Categorizes **credit score** into standard rating ranges.
- Computes **loan approval probability** using a weighted model.
- Loads applicant data from CSV files.
- Unit tests with **pytest** to ensure reliability.

---

**Project Structure**

<img width="365" height="276" alt="imagen" src="https://github.com/user-attachments/assets/ca919a12-9e50-4d74-bef5-d6d15c0efdf5" />

---

**Requirements**
- Python 3.8+
- pandas (optional, for future data handling)
- matplotlib (optional, for visualization)
- pytest

Install dependencies (if any) with:

pip install -r requirements.txt

**How to Run**

1. Clone the repository

git clone https://github.com/LordPuposky/loan_risk_calculator.git
cd loan_risk_calculator

2. Run the main program

python main.py

3. Run the tests

pytest -q

 **Example Output**

 Applicant: Alice
  Credit Score: 720 (Good)
  DTI: 0.15
  Approval Probability: 78.6%
------------------------------
Applicant: Bob
  Credit Score: 580 (Fair)
  DTI: 0.4
  Approval Probability: 52.3%
------------------------------

**Testing**

The project includes unit tests to verify:

calculate_dti() returns correct ratios or None for invalid data.

evaluate_credit_score_range() returns correct credit categories.

loan_approval_probability() returns a value between 0 and 1.

Run tests with:

pytest -q

**Future Improvements**

Add visualization of risk distribution with matplotlib.

Integrate with external financial APIs.

Implement a more advanced credit scoring algorithm.

**License**

This project is for educational purposes as part of the CSE111 Programming with Functions course at BYU.
