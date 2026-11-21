from pathlib import Path

import joblib
import pandas as pd

# Load the project’s saved decision tree.
project_root = Path(__file__).resolve().parents[1]
model_path = project_root / "artifacts" / "p2_decision_tree.joblib"
loaded_tree = joblib.load(model_path)

# Predict for the same fictional listing using the saved feature order.
demo_listing = pd.DataFrame(
    [{"Type": 1, "Age": 6, "Fee": 0, "PhotoAmt": 3}],
    columns=loaded_tree.feature_names_in_,
)
loaded_prediction = loaded_tree.predict(demo_listing)[0]

print("Model features:", loaded_tree.feature_names_in_.tolist())
print(f"Reloaded model prediction: {loaded_prediction}")