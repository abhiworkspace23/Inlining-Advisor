from data.dataset import generate_dataset
from features.feature_engineering import create_features
from models.train_model import train
from evaluation.evaluate import evaluate
from utils.heuristic import gcc_heuristic
from utils.plot_results import plot_comparison

def main():
    df = generate_dataset()

    X, y, FEATURES = create_features(df)

    model, scaler, X_test_s, y_test, X_test_raw = train(X, y)

    ml_acc = evaluate(model, X_test_s, y_test)

    # Heuristic
    heuristic_preds = X_test_raw.apply(gcc_heuristic, axis=1)
    heuristic_acc = (heuristic_preds == y_test).mean()

    print(f"\nHeuristic Accuracy: {heuristic_acc:.4f}")

    # Plot comparison
    plot_comparison(ml_acc, heuristic_acc)

if __name__ == "__main__":
    main()