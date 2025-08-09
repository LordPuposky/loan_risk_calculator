from typing import Optional, Dict

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
