# PetFinder.my Adoption Prediction

This MSBA 265 project uses historical PetFinder.my listings to study pet adoption speed. P1 explores the relationship between adoption speed and listing characteristics. P2 compares a Decision Tree with a majority-class baseline and demonstrates how to save and reload the fitted model.

## Project Questions

- **P1:** How does adoption speed vary by pet type, age, adoption fee, and number of photos?
- **P2:** How well can a Decision Tree using those four features predict adoption speed for listings from rescuers held out of training? What would its predictions mean for staff who review listings at risk of remaining unadopted?

## Repository Structure

The tree below shows the main files used to run and review the analysis.

```text
petfinder-adoption-project/
├── artifacts/
│   └── p2_decision_tree.joblib
├── data/
│   └── raw/
│       └── .gitkeep
├── figures/
│   ├── adoption_speed_distribution.png
│   ├── adoption_speed_by_pet_type.png
│   ├── adoption_speed_by_age_group.png
│   ├── adoption_speed_by_fee_group.png
│   ├── adoption_speed_by_photo_group.png
│   └── p2_decision_tree_confusion_matrix.png
├── notebooks/
│   ├── 01_p1_initial_eda.ipynb
│   └── P2/
│       └── p2_report.md
├── P1/
│   └── 01_p1_initial_eda.html
├── src/
│   ├── p2_baseline.py
│   └── p2_load_model.py
├── .gitignore
├── README.md
└── requirements.txt
```

The P1 HTML export provides a browser-readable copy of the exploratory analysis. The P2 report explains the model, evaluation, and proposed staff review process.

## Setup and Reproduction

The P1 notebook and the P2 scripts were tested on Windows with Python 3.13.5 in a project-local virtual environment (`.venv`). P2 was tested with scikit-learn 1.9.1 and joblib 1.6.0. The commands below use Windows Command Prompt (`cmd`).

### 1. Clone the repository

```cmd
git clone https://github.com/MinYang5859/petfinder-adoption-project.git
cd petfinder-adoption-project
```

If you are validating a specific version for the assignment, confirm the commit before running the project:

```cmd
git log -1 --oneline
```

### 2. Create the virtual environment and install dependencies

From the repository root, run:

```cmd
py -3.13 --version
py -3.13 -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python -c "import sys; print(sys.executable)"
```

The last command should print a path ending in `petfinder-adoption-project\.venv\Scripts\python.exe`. If the project's `.venv` already exists, start with the activation command.

### 3. Download the data

Open the [PetFinder.my Adoption Prediction competition data page](https://www.kaggle.com/competitions/petfinder-adoption-prediction/data). Sign in and accept the competition rules if prompted. Download the competition data, extract the relevant files, and place them directly in `data/raw/`.

| Task | Required files in `data/raw/` |
|---|---|
| Run the P1 notebook | `train.csv`, `breed_labels.csv`, `color_labels.csv`, `state_labels.csv` |
| Train and evaluate the P2 model | `train.csv` |
| Reload the saved P2 model | No CSV is required. The script uses `artifacts/p2_decision_tree.joblib`. |

Use the labeled competition file named `train.csv`. The project creates its own training and test split from that file. The original Kaggle CSVs are stored locally and excluded from Git.

To check the file names and location, run:

```cmd
dir data\raw
```

## P1 — Exploratory Data Analysis

### Run the notebook

1. Open `notebooks/01_p1_initial_eda.ipynb` in VS Code.
2. Open the kernel picker in the upper-right corner.
3. Choose **Python Environments** and select the project's `.venv` for Python 3.13. The interpreter path should end in `.venv\Scripts\python.exe`.
4. Restart the kernel and select **Run All**.

### Expected results

| Verification | Expected result |
|---|---:|
| Labeled listings loaded | 14,993 |
| Missing `AgeGroup` values | 0 |
| Missing `FeeGroup` values | 0 |
| Missing `PhotoGroup` values | 0 |
| Expected figure checks | All five return `True` |

The notebook generates the five P1 charts listed under `figures/` in the repository structure.

### Main findings

- The five `AdoptionSpeed` classes have different numbers of listings.
- Cats had a slightly lower average `AdoptionSpeed` class value than dogs in this dataset.
- Pets aged 0–5 months tended to appear in faster adoption classes.
- Adoption fee showed no clear linear relationship with adoption speed.
- Listings without photos had the highest average `AdoptionSpeed` class value. The share of class 4 listings generally decreased across groups with more photos.

`AdoptionSpeed` is an ordered category. Its average class value summarizes the category codes rather than the number of days to adoption. These patterns describe associations in the historical data. The effect of changing a listing feature would require a separate evaluation.

## P2 — Decision Tree

The model uses `Type`, `Age`, `Fee`, and `PhotoAmt` to predict `AdoptionSpeed`. The data is split by `RescuerID`, so all listings from the same rescuer stay in one set. The split contains 12,464 training listings and 2,529 test listings, with zero shared rescuer IDs.

The majority-class baseline predicts class 4 for every listing because class 4 is the most frequent class in the training set. The Decision Tree has a maximum depth of 4. Both approaches are evaluated on the same test listings.

### Reload the saved model

To verify the model supplied in the repository, run this step **before retraining**. From the repository root, with `.venv` active, run:

```cmd
python src\p2_load_model.py
```

The script reads the saved model and predicts one fictional listing with `Type=1`, `Age=6`, `Fee=0`, and `PhotoAmt=3`. It runs without the raw CSV. Load only a model file you trust.

Expected output:

```text
Model features: ['Type', 'Age', 'Fee', 'PhotoAmt']
Reloaded model prediction: 4
```

### Train and evaluate

Place the labeled Kaggle `train.csv` at `data/raw/train.csv`. With `.venv` active, run:

```cmd
python src\p2_baseline.py
```

The script prints the split counts, evaluation metrics, and class 4 results. It writes the following files:

- `figures/p2_decision_tree_confusion_matrix.png`
- `artifacts/p2_decision_tree.joblib`

The training script prints `Original model prediction: 4` for the same fictional listing. Run `python src\p2_load_model.py` again to verify that the locally trained and saved model returns the same prediction.

### Expected test results

| Metric | Majority-class baseline | Decision Tree |
|---|---:|---:|
| Accuracy | 27.88% | 34.40% |
| Correct predictions | 705 of 2,529 | 870 of 2,529 |
| Macro F1 | 0.0872 | 0.2409 |
| Quadratic weighted kappa | 0.0000 | 0.2201 |

The tree identified 454 of the 705 actual class 4 listings, giving a recall of 64.40%. It missed the other 251. A rule that flags every class 4 prediction would flag 1,159 of the 2,529 historical test listings for manual review. Of those flagged listings, 454 actually belonged to class 4, giving a precision of 39.17%. The tree also missed all 61 actual class 0 listings.

The historical test results estimate review workload under this rule. Whether acting on the flags improves adoption outcomes remains to be tested in a staff-led pilot.

## P2 Peer Validation Checklist

- [ ] Clone the repository into a new folder and record the commit ID.
- [ ] Create and activate the Python 3.13 `.venv`. Install the packages from `requirements.txt`.
- [ ] Run `python src\p2_load_model.py` before retraining. Confirm that the supplied model returns class 4 for the fictional listing.
- [ ] Download the labeled Kaggle CSV and place it at `data/raw/train.csv`.
- [ ] Run `python src\p2_baseline.py`. Confirm 12,464 training listings, 2,529 test listings, and zero shared rescuer IDs.
- [ ] Compare the actual metrics with the P2 results table. Record any differences.
- [ ] Open the generated confusion matrix. Confirm that the cell for actual class 4 and predicted class 4 shows 454.
- [ ] Run `python src\p2_load_model.py` again. Confirm that the reloaded prediction matches the training script's prediction for the same fictional listing.
- [ ] Record the Python version, actual outputs, and any reproduction issues in the Assignment Validation form. Complete and sign the form after testing.

To validate P1 as well, add the three label CSVs, run the notebook using the project `.venv`, and compare the output with the P1 expected results.

## Troubleshooting

| Issue | What to check |
|---|---|
| `py -3.13` cannot find Python | Run `py -0p` to see which versions the launcher recognizes. If Python 3.13 is missing, install it, reopen `cmd`, and return to Step 2. |
| VS Code is using the wrong notebook kernel | Run `import sys` and `print(sys.executable)` in a notebook cell. If the path points to another environment, select the project's `.venv` in the kernel picker and restart the notebook kernel. |
| `ModuleNotFoundError` | Activate the project `.venv` and run `python -m pip install -r requirements.txt`. If the error is in the notebook, also check its kernel. |
| `FileNotFoundError` for a CSV | Run `dir data\raw` from the repository root and check that the files required for your task are in that folder. |
| P2 cannot find the saved model | Check `dir artifacts\p2_decision_tree.joblib`. If the file is missing from a fresh clone, record that in peer validation. You can still train a local copy with `python src\p2_baseline.py` and then test reloading it. |
| Model reload gives a version warning | Check the active environment with `python -m pip show scikit-learn joblib` and compare the versions with `requirements.txt`. |
| A figure is missing | For P1, review the first notebook cell that reports an error. For P2, check the output of `python src\p2_baseline.py` for the saved figure path. |

## P2 Submission Materials

- P2 report draft (`notebooks/P2/p2_report.md`)
- Stakeholder PowerPoint (`p2_stakeholder_presentation.pptx`)
- Training and evaluation script, saved model, reload script, and confusion matrix
- README, requirements, and Kaggle data access instructions
- P1 feedback status and completed Assignment Validation form

At the time of this P2 draft, P1 had not been graded and instructor feedback was not yet available. P2 extends the exploratory analysis with a held-out model evaluation, an explanation of the results for rescue staff, and a standalone model reload demonstration.

## References

PetFinder.my. (n.d.). *About PetFinder.my*.  
https://www.petfinder.my/about.htm

PetFinder.my. (2018). *PetFinder.my adoption prediction* [Data set]. Kaggle.  
https://www.kaggle.com/competitions/petfinder-adoption-prediction

## Author

Min Yang  
MSBA 265 — Special Analytics Topics  
University of the Pacific