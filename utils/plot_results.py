import matplotlib.pyplot as plt

def plot_comparison(ml_acc, heuristic_acc):
    names = ["ML Model", "Heuristic"]
    values = [ml_acc, heuristic_acc]

    plt.bar(names, values)
    plt.ylabel("Accuracy")
    plt.title("Inlining Decision Comparison")

    for i, v in enumerate(values):
        plt.text(i, v + 0.01, f"{v:.3f}", ha='center')

    plt.ylim(0,1)
    plt.savefig("inlining_results.png")
    plt.show()