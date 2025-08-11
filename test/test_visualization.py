import visualization

def test_plot_approval_probabilities_runs_without_error():
    sample_results = [
        {"name": "Alice", "approval_probability": 0.85},
        {"name": "Bob", "approval_probability": 0.45},
        {"name": "Charlie", "approval_probability": 0.60}
    ]
    
    applicants = [{"name": r["name"]} for r in sample_results]
    probabilities = [r["approval_probability"] for r in sample_results]

    try:
        visualization.plot_approval_probabilities(applicants, probabilities)
    except Exception as e:
        assert False, f"Visualization function raised an error: {e}"
