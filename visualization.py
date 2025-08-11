import matplotlib.pyplot as plt

def plot_approval_probabilities(applicants, probabilities):
    """
    Plot approval probabilities for each applicant.
    :param applicants: list of dicts with at least a "name" key.
    :param probabilities: list of float probabilities between 0.0 and 1.0.
    """
    names = [a["name"] for a in applicants]
    
    plt.figure(figsize=(8, 5))
    plt.bar(names, probabilities, color="skyblue")
    plt.xlabel("Applicants")
    plt.ylabel("Approval Probability")
    plt.ylim(0, 1)
    plt.title("Loan Approval Probabilities")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()
