from sklearn.metrics import classification_report, accuracy_score

def evaluate(model, X_test, y_test):
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    print(f"\nModel Accuracy: {acc:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, preds))

    return acc