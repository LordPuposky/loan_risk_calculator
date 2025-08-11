from typing import Optional, Dict, List
import csv

# ----- Configuration constants -----
SCORE_MIN, SCORE_MAX = 300, 850
WEIGHT_SCORE, WEIGHT_DTI, WEIGHT_EMP = 0.5, 0.3, 0.2


def calculate_dti(income: float, debt: float) -> Optional[float]:
    """
    Calculate the debt-to-income (DTI) ratio as a decimal (e.g., 0.35).
    Returns None if income is less than or equal to 0 or if inputs are invalid.
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
    elif s < 670:
        return "Fair"
    elif s < 740:
        return "Good"
    elif s < 800:
        return "Very Good"
    return "Excellent"


def loan_approval_probability(applicant: Dict[str, float]) -> float:
    """
    Calculate a simple loan approval probability in the range [0.0, 1.0].
    Factors:
        - Credit score normalized between SCORE_MIN and SCORE_MAX
        - DTI (lower DTI => higher factor)
        - Employment years capped at 10 years for factor

    Weights: score 0.5, DTI 0.3, employment 0.2
    """
    score = applicant.get("credit_score", 0)
    income = applicant.get("income", 0)
    debt = applicant.get("debt", 0)
    emp_years = applicant.get("employment_years", 0)

    dti = calculate_dti(income, debt)
    if dti is None:
        return 0.0  # Invalid income

    # Normalize credit score to [0,1]
    score_norm = (max(SCORE_MIN, min(SCORE_MAX, int(score))) - SCORE_MIN) / (SCORE_MAX - SCORE_MIN)
    dti_factor = max(0.0, min(1.0, 1.0 - dti))
    emp_factor = min(max(0.0, float(emp_years)), 10.0) / 10.0

    prob = WEIGHT_SCORE * score_norm + WEIGHT_DTI * dti_factor + WEIGHT_EMP * emp_factor
    return round(max(0.0, min(1.0, prob)), 3)


def load_applicant_data(file_path: str) -> List[Dict[str, float]]:
    """
    Load applicants from a CSV file and cast numeric fields where appropriate.
    """
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
