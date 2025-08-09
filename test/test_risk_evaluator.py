import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from risk_evaluator import calculate_dti, evaluate_credit_score_range, loan_approval_probability

def test_calculate_dti_normal():
    assert calculate_dti(2000, 500) == 0.25

def test_calculate_dti_zero_income():
    assert calculate_dti(0, 500) is None

def test_calculate_dti_invalid_input():
    assert calculate_dti("abc", 500) is None

def test_evaluate_credit_score_range_values():
    assert evaluate_credit_score_range(550) == "Poor"
    assert evaluate_credit_score_range(600) == "Fair"
    assert evaluate_credit_score_range(700) == "Good"
    assert evaluate_credit_score_range(750) == "Very Good"
    assert evaluate_credit_score_range(820) == "Excellent"
    assert evaluate_credit_score_range(None) == "Unknown"

def test_loan_approval_probability_basic():
    applicant = {
        "credit_score": 750,
        "income": 4000,
        "debt": 1000,
        "employment_years": 5
    }
    prob = loan_approval_probability(applicant)
    assert 0 <= prob <= 1
