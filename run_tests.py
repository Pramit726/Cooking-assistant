from tests.test_comment_classifier import test_classifier_accuracy
from tests.test_llm_routing_decision import test_routing_accuracy

if __name__ == "__main__":
    print("Running all tests...\n")
    
    routing_results = test_routing_accuracy()
    classifier_results = test_classifier_accuracy()
    
    print("\nAll tests completed successfully!")
    
    print("\nRouting Decision Test Results:")
    print(routing_results)
    print("\n" + "-"*40 + "\n")
    
    print("\nComment Classifier Test Results:")
    print(classifier_results)