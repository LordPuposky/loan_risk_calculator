from typing import Optional, Dict, List
import csv

def calculate_dti(income: float, debt: float) -> Optional[float]:
    """
    Return debt-to-income ratio as a decimal (e.g., 0.35).
    If income <= 0 returns None to indicate invalid/undefined DTI.
    """
    try:
        income = float(income)
        debt = float(debt)
    except (TypeError, ValueError):
        return None
    if income <= 0:
        return None
    return debt / income

def evaluate_credit_score_range(score: int) -> str:
    """
    Categorize credit score:
    <580 Poor, 580-669 Fair, 670-739 Good, 740-799 Very Good, >=800 Excellent
    """
    if score is None:
        return "Unknown"
    try:
        s = int(score)
    except (TypeError, ValueError):
        return "Unknown"
    if s < 580:
        return "Poor"
    if s < 670:
        return "Fair"
    if s < 740:
        return "Good"
    if s < 800:
        return "Very Good"
    return "Excellent"

def loan_approval_probability(applicant: Dict) -> float:
    """
    Compute a simple approval probability in [0.0, 1.0].
    Factors:
        - credit score normalized between 300 and 850
        - DTI transformed so lower DTI => higher factor
        - employment_years capped at 10 for the factor

    Weights: score 0.5, dti 0.3, employment 0.2
    """
    score = applicant.get("credit_score", 0)
    income = applicant.get("income", 0)
    debt = applicant.get("debt", 0)
    emp_years = applicant.get("employment_years", 0)

    dti = calculate_dti(income, debt)
    if dti is None:
        return 0.0  # invalid income

    # normalize score to [0,1] from [300,850]
    score_norm = (max(300, min(850, int(score))) - 300) / 550
    dti_factor = max(0.0, min(1.0, 1.0 - dti))
    emp_factor = min(max(0.0, float(emp_years)), 10.0) / 10.0

    prob = 0.5 * score_norm + 0.3 * dti_factor + 0.2 * emp_factor
    return round(max(0.0, min(1.0, prob)), 3)

def load_applicant_data(file_path: str) -> List[dict]:
    """Load applicants from CSV and cast numeric fields where appropriate."""
    applicants = []
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row_parsed = {
                "name": row.get("name"),
                "credit_score": int(row.get("credit_score", 0)),
                "income": float(row.get("income", 0) or 0),
                "debt": float(row.get("debt", 0) or 0),
                "employment_years": float(row.get("employment_years", 0) or 0)
            }
            applicants.append(row_parsed)
    return applicants
