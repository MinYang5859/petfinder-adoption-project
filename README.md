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
│       ├── p2_baseline.py
│       ├── p2_load_model.py
│       ├── p2_report.md
│       └── p2_stakeholder_presentation.pptx
├── P1/
│   └── 01_p1_initial_eda.html
├── .gitignore
├── README.md
└── requirements.txt
```

The P1 HTML export provides a browser-readable copy of the exploratory analysis. The P2 report explains the model, evaluation, and proposed staff review process.

## Windows Setup

The author reproduced P1 and P2 on Windows with Python 3.13.5. Python 3.14.3 is an alternate environment to try. Record the version you actually use and whether each check passes.

1. Open Windows PowerShell or Command Prompt (cmd). Start in a folder where you want to create a fresh clone.
2. Run the following commands. If your assignment specifies a commit, run `git checkout COMMIT_ID` with the assigned ID before continuing. A detached HEAD message is normal for that checkout.

```text
git clone https://github.com/MinYang5859/petfinder-adoption-project.git petfinder-p2-validation
cd petfinder-p2-validation
git log -1 --oneline
py --version
```

3. Create the environment. Use the first command if Python 3.13 is available. If that command reports that no suitable runtime was found and `py --version` shows 3.14, use the second command instead.

```text
py -3.13 -m venv .venv
```

If only Python 3.14 is available, run this instead:

```text
py -3.14 -m venv .venv
```

If `py` is unavailable, run `python --version`. If it reports 3.13 or 3.14, use `python -m venv .venv`. If neither command works, install Windows Python from [python.org](https://www.python.org/downloads/windows/) and reopen the terminal. If reusing a previously created `.venv`, check its version using the next block.

4. From the project root, run all three commands below. They work in PowerShell and cmd without activating the environment.

```text
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -c "import sys, numpy, pandas, matplotlib, seaborn, sklearn, joblib, ipykernel; print(sys.executable); print('scikit-learn:', sklearn.__version__); print('joblib:', joblib.__version__); print('Imports OK')"
```

Verify that the path ends in `.venv\Scripts\python.exe` and the last line is `Imports OK`. The expected pinned versions are scikit-learn 1.9.1 and joblib 1.6.0. Prompt color and the presence of a `(.venv)` prefix do not affect these commands.

## Get the Data

Start with **Reload the saved model** in the P2 section below. It can run before downloading the dataset.

To retrain or run P1, open the [Kaggle competition data page](https://www.kaggle.com/competitions/petfinder-adoption-prediction/data). Sign in, join or accept the rules if prompted, and download and extract the competition data. If extraction creates nested folders, locate the CSVs inside them and copy the files directly into your clone's `data/raw/` directory.

| Task | Required files |
|---|---|
| Reload the model supplied with the repository | `artifacts/p2_decision_tree.joblib` |
| Train and evaluate P2 | `data/raw/train.csv` |
| Run the P1 notebook | `train.csv`, `breed_labels.csv`, `color_labels.csv`, and `state_labels.csv` in `data/raw/` |

Use the labeled `train.csv`. The script splits this file into training and test sets. Run `dir data\raw` from the project root to verify the file names. Keep the Kaggle CSVs local.

## P1 — Exploratory Data Analysis

### Run the notebook

1. Open `notebooks/01_p1_initial_eda.ipynb` in VS Code.
2. Open the kernel picker in the upper-right corner.
3. Choose **Python Environments** and select the project's `.venv`. The interpreter path should end in `.venv\Scripts\python.exe`.
4. Run `import sys; print(sys.executable)` in a notebook cell to verify the kernel path. Restart the kernel and select **Run All**.

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

To verify the model supplied in the repository, run this step **before retraining**. From the repository root, run:

```cmd
.\.venv\Scripts\python.exe notebooks\P2\p2_load_model.py
```

The script reads the saved model and predicts one fictional listing with `Type=1`, `Age=6`, `Fee=0`, and `PhotoAmt=3`. It runs without the raw CSV. Load only a model file you trust.

Expected output:

```text
Model features: ['Type', 'Age', 'Fee', 'PhotoAmt']
Reloaded model prediction: 4
```

### Train and evaluate

Place the labeled Kaggle `train.csv` at `data/raw/train.csv`. From the project root, run:

```cmd
.\.venv\Scripts\python.exe notebooks\P2\p2_baseline.py
```

The script prints the split counts, evaluation metrics, and class 4 results. It writes the following files:

- `figures/p2_decision_tree_confusion_matrix.png`
- `artifacts/p2_decision_tree.joblib`

The training script prints `Original model prediction: 4` for the same fictional listing. Run `.\.venv\Scripts\python.exe notebooks\P2\p2_load_model.py` again to verify that the locally trained and saved model returns the same prediction.

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
- [ ] Create the project `.venv`, install dependencies using its Python executable, and verify `Imports OK`.
- [ ] Run `.\.venv\Scripts\python.exe notebooks\P2\p2_load_model.py` before retraining. Confirm that the supplied model returns class 4 for the fictional listing.
- [ ] Download the labeled Kaggle CSV and place it at `data/raw/train.csv`.
- [ ] Run `.\.venv\Scripts\python.exe notebooks\P2\p2_baseline.py`. Confirm 12,464 training listings, 2,529 test listings, and zero shared rescuer IDs.
- [ ] Compare the actual metrics with the P2 results table. Record any differences.
- [ ] Open the generated confusion matrix. Confirm that the cell for actual class 4 and predicted class 4 shows 454.
- [ ] Run `.\.venv\Scripts\python.exe notebooks\P2\p2_load_model.py` again. Confirm that the reloaded prediction matches the training script's prediction for the same fictional listing.
- [ ] Record the Python version, actual outputs, and any reproduction issues in the Assignment Validation form. Complete and sign the form after testing.

To validate P1 as well, add the three label CSVs, run the notebook using the project `.venv`, and compare the output with the P1 expected results.

## Troubleshooting

| What you see | How to proceed |
|---|---|
| `No suitable Python runtime found` with `py -3.13` | Run `py -0p` or `py --version`. If 3.14 is available, create the environment with `py -3.14 -m venv .venv`. |
| No `(.venv)` prefix, or pip reports packages under global Python | Run Step 4 using the full `.\.venv\Scripts\python.exe` prefix. A batch activation command launched from PowerShell does not activate its parent PowerShell session. |
| `pip` reports no matching distribution or fails to build a package | Check the failing package and your virtual environment's Python version. If this occurs under 3.14, install 3.13 and start with a fresh clone and environment using 3.13. Record the failed attempt in the validation form. |
| P1 reports `No module named numpy` or asks for `ipykernel` | Complete Step 4, then select the project's `.venv` in the VS Code kernel picker. With the Python and Jupyter extensions enabled, reopen the notebook if the environment is missing from the picker. For a persistent picker issue, run `.\.venv\Scripts\python.exe -m ipykernel install --user --name petfinder-validation --display-name "Python (PetFinder validation)"`, select that kernel, and verify `sys.executable`. |
| Kaggle denies the download or Python cannot find the CSV | Sign in and accept the competition rules if prompted. Run `dir data\raw` and verify that the file is named `train.csv` and is directly inside `data/raw/`. If Kaggle access remains blocked, record that and complete the saved-model check. |
| The saved model is missing or gives a version warning | Run `git log -1 --oneline` and `dir artifacts\p2_decision_tree.joblib`. Verify the pinned versions with `.\.venv\Scripts\python.exe -m pip show scikit-learn joblib`. If the supplied artifact still fails, record that result before retraining. Test the newly trained artifact separately. |
| Results differ from the expected table | Check the commit, Python and dependency versions, and that you used the labeled Kaggle `train.csv`. Record the actual outputs and the differences in the form. |

## P2 Submission Materials

- P2 report draft (`notebooks/P2/p2_report.md`)
- Stakeholder PowerPoint (`notebooks/P2/p2_stakeholder_presentation.pptx`)
- Training and evaluation script, saved model, reload script, and confusion matrix
- README, requirements, and Kaggle data access instructions
- P1 feedback status and Assignment Validation form (completed by the peer after testing)

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
