import datetime

from tabulate import tabulate

from llm.groq_qa import is_comment_question

test_comments = [
    ("How long should I cook the biryani on low heat?", True),
    ("Thanks for the recipe, it turned out great!", False),
    ("Can I replace yogurt with coconut milk?", True),
    ("Loved it ❤️", False),
    ("Is there a vegan version of this recipe?", True),
    ("I make this every weekend!", False),
    ("Why do you add garam masala at the end?", True),
    ("Yummy 😋", False),
]

def test_classifier_accuracy():
    print("\n Running Comment Classification Tests...\n")

    results = []
    correct = 0

    for i, (comment, expected) in enumerate(test_comments, 1):
        predicted = is_comment_question(comment)
        result = "✅" if predicted == expected else "❌"
        if result == "✅":
            correct += 1
        results.append([
            i, comment, expected, predicted, result
        ])

    # Generate tabular report
    print(tabulate(
        results,
        headers=["#", "Comment", "Expected", "Predicted", "Result"],
        tablefmt="grid"
    ))

    total = len(test_comments)
    accuracy = correct / total * 100

    print("\n📊 Test Summary")
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total Tests: {total}")
    print(f"Passed: {correct}")
    print(f"Failed: {total - correct}")
    print(f"Accuracy: {accuracy:.2f}%")

    return {
        "total": total,
        "passed": correct,
        "failed": total - correct,
        "accuracy": accuracy
    }