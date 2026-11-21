from pathlib import Path

import pandas as pd
from sklearn.model_selection import GroupShuffleSplit
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    cohen_kappa_score,
    confusion_matrix,
    f1_score,
)

import joblib

# Load the labeled PetFinder listings.
project_root = Path(__file__).resolve().parents[2]
data = pd.read_csv(project_root / "data" / "raw" / "train.csv")

# Split by rescuer so each rescuer appears in only one set.
splitter = GroupShuffleSplit(n_splits=1, test_size=0.20, random_state=42)
train_idx, test_idx = next(splitter.split(data, groups=data["RescuerID"]))

# Select the listings for each set using their row positions.
train = data.iloc[train_idx]
test = data.iloc[test_idx]

# Check the row counts and look for rescuers shared by both sets.
overlap = set(train["RescuerID"]) & set(test["RescuerID"])
print("Training rows:", len(train))
print("Test rows:", len(test))
print("Rescuers in both sets:", len(overlap))

# Find the most common adoption class in the training set.
train_class_counts = train["AdoptionSpeed"].value_counts()
majority_class = train_class_counts.idxmax()

print("\nTraining class counts:")
print(train_class_counts)
print("Baseline predicted class:", majority_class)

# Count how often the same prediction matches the test labels.
correct_count = (test["AdoptionSpeed"] == majority_class).sum()
baseline_accuracy = correct_count / len(test)

print(f"Correct predictions: {correct_count} / {len(test)}")
print(f"Baseline accuracy: {baseline_accuracy:.2%}")

# Start with the four features explored in P1.
feature_columns = ["Type", "Age", "Fee", "PhotoAmt"]
target_column = "AdoptionSpeed"

# Select the features and target from the same rows in each set.
X_train = train[feature_columns]
y_train = train[target_column]

X_test = test[feature_columns]
y_test = test[target_column]

# Check the shapes and missing feature values before training.
print("\nTraining features:", X_train.shape)
print("Training labels:", y_train.shape)
print("Test features:", X_test.shape)
print("Test labels:", y_test.shape)

print("\nMissing feature values in training:")
print(X_train.isna().sum())

# Check for missing values in the test features.
print("\nMissing feature values in test:")
print(X_test.isna().sum())

# Train a shallow tree using the training features and labels.
tree = DecisionTreeClassifier(max_depth=4, random_state=42)
tree.fit(X_train, y_train)

# Predict adoption classes for the held-out listings.
tree_predictions = tree.predict(X_test)

# Compare the tree and baseline on the same test set.
tree_correct_count = (tree_predictions == y_test.to_numpy()).sum()
tree_accuracy = tree_correct_count / len(y_test)
accuracy_gain = (tree_accuracy - baseline_accuracy) * 100

print(f"\nDecision Tree correct: {tree_correct_count} / {len(y_test)}")
print(f"Decision Tree accuracy: {tree_accuracy:.2%}")
print(f"Baseline accuracy: {baseline_accuracy:.2%}")
print(f"Accuracy difference: {accuracy_gain:+.2f} percentage points")

# Count actual and predicted adoption classes on the test set.
labels = [0, 1, 2, 3, 4]
tree_matrix = confusion_matrix(y_test, tree_predictions, labels=labels)

# Label the rows and columns so the matrix is easier to read.
tree_matrix_table = pd.DataFrame(
    tree_matrix,
    index=pd.Index(labels, name="Actual"),
    columns=pd.Index(labels, name="Predicted"),
)

print("\nDecision Tree confusion matrix:")
print(tree_matrix_table)
print("Total predictions in matrix:", tree_matrix.sum())
print("Correct predictions in matrix:", tree_matrix.trace())

# Find the row and column for AdoptionSpeed class 4.
class_4_index = labels.index(4)

# Count correct flags, actual class 4 listings, and all flags.
correct_flags = tree_matrix[class_4_index, class_4_index]
actual_class_4 = tree_matrix[class_4_index, :].sum()
predicted_class_4 = tree_matrix[:, class_4_index].sum()

class_4_recall = correct_flags / actual_class_4
class_4_precision = correct_flags / predicted_class_4

print(f"\nClass 4 recall: {correct_flags} / {actual_class_4} = {class_4_recall:.2%}")
print(f"Class 4 precision: {correct_flags} / {predicted_class_4} = {class_4_precision:.2%}")
print(f"Missed class 4 listings: {actual_class_4 - correct_flags}")
print(f"Flagged listings from other classes: {predicted_class_4 - correct_flags}")

# Create one baseline prediction for each test listing.
baseline_predictions = [majority_class] * len(y_test)

# Compare both models using the same test labels and class order.
for model_name, predictions in [
    ("Baseline", baseline_predictions),
    ("Decision Tree", tree_predictions),
]:
    macro_f1 = f1_score(
        y_test, predictions, labels=labels, average="macro", zero_division=0
    )
    qwk = cohen_kappa_score(
        y_test, predictions, labels=labels, weights="quadratic"
    )

    print(f"\n{model_name}")
    print(f"Macro F1: {macro_f1:.4f}")
    print(f"Quadratic Weighted Kappa: {qwk:.4f}")

    # Plot the confusion matrix calculated from the held-out test set.
fig, ax = plt.subplots(figsize=(7, 5))
display = ConfusionMatrixDisplay(
    confusion_matrix=tree_matrix,
    display_labels=labels,
)
display.plot(ax=ax, cmap="Blues", values_format="d", colorbar=False)

ax.set_title("Decision Tree Confusion Matrix")
ax.set_xlabel("Predicted AdoptionSpeed")
ax.set_ylabel("Actual AdoptionSpeed")
fig.tight_layout()

# Save the figure for the P2 report.
figure_dir = project_root / "figures"
figure_dir.mkdir(exist_ok=True)
figure_path = figure_dir / "p2_decision_tree_confusion_matrix.png"
fig.savefig(figure_path, dpi=200)
plt.close(fig)

print(f"\nSaved confusion matrix figure: {figure_path}")

# Save the fitted tree for use in a separate script.
model_dir = project_root / "artifacts"
model_dir.mkdir(exist_ok=True)

model_path = model_dir / "p2_decision_tree.joblib"
joblib.dump(tree, model_path)
print(f"\nSaved fitted model: {model_path}")

# Record a prediction for one fictional listing before reloading.
demo_listing = pd.DataFrame(
    [{"Type": 1, "Age": 6, "Fee": 0, "PhotoAmt": 3}],
    columns=feature_columns,
)
original_prediction = tree.predict(demo_listing)[0]
print(f"Original model prediction: {original_prediction}")