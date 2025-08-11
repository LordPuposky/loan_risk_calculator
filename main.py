from risk_evaluator import load_applicant_data, loan_approval_probability
from visualization import plot_approval_probabilities

def main():
    # Load applicant data from CSV
    file_path = "data/applicants.csv"
    applicants = load_applicant_data(file_path)

    results = []
    for applicant in applicants:
        probability = loan_approval_probability(applicant)
        results.append({
            "name": applicant["name"],
            "approval_probability": probability
        })

    # Display results in the console
    for r in results:
        print(f"{r['name']}: Approval Probability = {r['approval_probability']*100:.1f}%")

    # Prepare data for visualization
    applicant_names = [{"name": r["name"]} for r in results]
    probabilities = [r["approval_probability"] for r in results]

    # Plot the probabilities
    plot_approval_probabilities(applicant_names, probabilities)

if __name__ == "__main__":
    main()
