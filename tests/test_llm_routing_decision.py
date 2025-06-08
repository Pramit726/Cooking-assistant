import datetime

from tabulate import tabulate

from retriever.router import get_llm_routing_decision


def test_routing_accuracy():
    test_queries = [
        {"query": "What are the ingredients used in Chicken Biryani?", "recipe": "chickenbiryani", "expected": "pdf"},
        {"query": "Who invented Gulab Jamun?", "recipe": "gulabjamun", "expected": "wikipedia"},
        {"query": "How much protein is in a serving of Masala Dosa?", "recipe": "masaladosa", "expected": "pdf"},
        {"query": "Is Baingan Bharta vegan?", "recipe": "bainganbharta", "expected": "pdf"},
        {"query": "How to prepare Upma in a restaurant style?", "recipe": "upma", "expected": "pdf"},
        {"query": "What is the nutritional value of Kheer?", "recipe": "kheer", "expected": "pdf"},
        {"query": "When was the samosa first made?", "recipe": "samosa", "expected": "wikipedia"},
        {"query": "Can I substitute butter with ghee in Chicken Butter Masala?", "recipe": "chickenbuttermasala", "expected": "pdf"},
        {"query": "Which Indian state is known for Samosa?", "recipe": "samosa", "expected": "wikipedia"},
    ]

    report_rows = []
    correct = 0

    print("\n🧪 Running LLM Routing Decision Tests...\n")

    for i, test in enumerate(test_queries, 1):
        actual = get_llm_routing_decision(test["query"], test["recipe"])
        passed = actual == test["expected"]
        if passed:
            correct += 1

        report_rows.append([
            i,
            test["query"],
            test["recipe"],
            test["expected"],
            actual,
            "✅" if passed else "❌"
        ])

    accuracy = (correct / len(test_queries)) * 100

    # Print report table
    print(tabulate(
        report_rows,
        headers=["#", "Query", "Recipe", "Expected", "Actual", "Result"],
        tablefmt="grid"
    ))

    # Summary
    print("\n📊 Test Summary")
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total Tests: {len(test_queries)}")
    print(f"Passed: {correct}")
    print(f"Failed: {len(test_queries) - correct}")
    print(f"Accuracy: {accuracy:.2f}%")

    return {
        "total": len(test_queries),
        "passed": correct,
        "failed": len(test_queries) - correct,
        "accuracy": accuracy
    }
