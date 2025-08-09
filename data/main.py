from risk_evaluator import (
    load_applicant_data,
    loan_approval_probability,
    calculate_dti,
    evaluate_credit_score_range)

def display_applicant_report(applicant):
    prob = loan_approval_probability(applicant)
    dti = calculate_dti(applicant.get('income', 0), applicant.get('debt', 0))
    print(f"Applicant: {applicant.get('name', 'Unknown')}")
    print(f"  Credit Score: {applicant.get('credit_score')} ({evaluate_credit_score_range(applicant.get('credit_score'))})")
    print(f"  DTI: {round(dti, 3) if dti is not None else 'N/A'}")
    print(f"  Approval Probability: {prob*100:.1f}%")
    print("-" * 30)

if __name__ == "__main__":
    applicants = load_applicant_data("data/applicants.csv")
    for a in applicants:
        display_applicant_report(a)
