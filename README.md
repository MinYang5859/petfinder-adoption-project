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

## Setup and Reproduction

You will need Git and Python. The reference run used Windows and Python 3.13.5. You can start with another installed Python version and use the dependency and import checks below to see whether it works for your platform. If installation fails for your version, try Python 3.13 in a fresh environment. Record the OS and Python version you actually test.

### 1. Clone the repository

Open a terminal in the folder where you want to put the validation copy.

```text
git clone https://github.com/MinYang5859/petfinder-adoption-project.git petfinder-p2-validation
cd petfinder-p2-validation
git log -1 --oneline
```

If you were given a specific commit, run `git checkout COMMIT_ID` with that ID, then run `git log -1 --oneline` again. A detached HEAD message is normal for this checkout. Run the remaining commands from the repository root.

### 2. Create the project environment

**Windows (PowerShell or Command Prompt)**

```text
py -m venv .venv
```

If Windows cannot find the launcher, check that `python --version` works and run `python -m venv .venv` instead.

**macOS or Linux**

```sh
python3 -m venv .venv
```

A virtual environment created successfully may produce no terminal output. Keep running commands from the repository root.

### 3. Activate the environment and verify it

Open the terminal in the repository root. Run only the block matching your shell. In VS Code, use the dropdown beside the terminal **+** button to choose a shell.

**Windows PowerShell** (the prompt usually starts with PS)

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell says script execution is disabled, open a **Command Prompt** terminal using the VS Code dropdown and run the cmd block below. From PowerShell, you can also run the following command to open an activated cmd session in the same folder. Continue in that session. Type exit to return to PowerShell.

```text
cmd /k ".venv\Scripts\activate.bat"
```

**Windows Command Prompt (cmd)**

```cmd
.venv\Scripts\activate.bat
```

**macOS or Linux (Bash or Zsh)**

```sh
source .venv/bin/activate
```

After activation, the prompt usually starts with (.venv). Prompt appearance can vary. Run this check in the same terminal:

```text
python -c "import sys; print(sys.executable); print('Virtual environment:', sys.prefix != sys.base_prefix)"
```

The executable should be inside this clone's .venv and the last line should be Virtual environment: True. If the command points elsewhere, check that you used the activation block for your actual shell. PowerShell and cmd use different activation scripts. If the activation file is missing, confirm that you are in the repository root and repeat Step 2.

Activation applies to the current terminal. Repeat this step after opening a new terminal. If your shell cannot activate the environment, the explicit interpreter commands in the following sections can still run the project.

### 4. Install and verify dependencies

The commands below call the project's Python directly. Start with the first command for your platform and continue only when it succeeds and shows an executable inside this clone's `.venv`. The prompt can stay unchanged throughout setup.

**Windows (PowerShell or Command Prompt)**

```text
.\.venv\Scripts\python.exe -c "import sys; print(sys.version); print(sys.executable); assert sys.prefix != sys.base_prefix"
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -c "import numpy, pandas, matplotlib, seaborn, sklearn, joblib, ipykernel; print('scikit-learn', sklearn.__version__); print('joblib', joblib.__version__); print('Imports OK')"
```

**macOS or Linux**

```sh
./.venv/bin/python -c "import sys; print(sys.version); print(sys.executable); assert sys.prefix != sys.base_prefix"
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python -c "import numpy, pandas, matplotlib, seaborn, sklearn, joblib, ipykernel; print('scikit-learn', sklearn.__version__); print('joblib', joblib.__version__); print('Imports OK')"
```

Expect `Imports OK`, scikit-learn 1.9.1, and joblib 1.6.0. If the executable is missing, check that `requirements.txt` is visible in your current folder and rerun Step 2. If pip fails, use the troubleshooting table below before continuing.

## Get the Data

Start with **Reload the saved model** in the P2 section below. It can run before downloading the dataset.

To retrain or run P1, open the [Kaggle competition data page](https://www.kaggle.com/competitions/petfinder-adoption-prediction/data). Sign in, join or accept the rules if prompted, and download and extract the competition data. If extraction creates nested folders, locate the CSVs inside them and copy the files directly into your clone's `data/raw/` directory.

| Task | Required files |
|---|---|
| Reload the model supplied with the repository | `artifacts/p2_decision_tree.joblib` |
| Train and evaluate P2 | `data/raw/train.csv` |
| Run the P1 notebook | `train.csv`, `breed_labels.csv`, `color_labels.csv`, and `state_labels.csv` in `data/raw/` |

Use the labeled `train.csv`. The script splits this file into training and test sets. Check the file names in your file browser. Keep the Kaggle CSVs local.

## P1 — Exploratory Data Analysis

### Run the notebook

1. Open `notebooks/01_p1_initial_eda.ipynb` in VS Code.
2. Open the kernel picker in the upper-right corner.
3. Choose **Python Environments** and select the project's `.venv`. Match the kernel path to the executable printed in Step 4.
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

**Windows (PowerShell or Command Prompt)**

```text
.\.venv\Scripts\python.exe notebooks/P2/p2_load_model.py
```

**macOS or Linux**

```sh
./.venv/bin/python notebooks/P2/p2_load_model.py
```

The script reads the saved model and predicts one fictional listing with `Type=1`, `Age=6`, `Fee=0`, and `PhotoAmt=3`. It runs without the raw CSV. Load only a model file you trust.

Expected output:

```text
Model features: ['Type', 'Age', 'Fee', 'PhotoAmt']
Reloaded model prediction: 4
```

### Train and evaluate

Place the labeled Kaggle `train.csv` at `data/raw/train.csv`. From the project root, run:

**Windows (PowerShell or Command Prompt)**

```text
.\.venv\Scripts\python.exe notebooks/P2/p2_baseline.py
```

**macOS or Linux**

```sh
./.venv/bin/python notebooks/P2/p2_baseline.py
```

The script prints the split counts, evaluation metrics, and class 4 results. It writes the following files:

- `figures/p2_decision_tree_confusion_matrix.png`
- `artifacts/p2_decision_tree.joblib`

The training script prints `Original model prediction: 4` for the same fictional listing. Repeat the **Reload the saved model** command for your platform to verify that the locally trained and saved model returns the same prediction.

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
- [ ] Create and activate the project `.venv`, install dependencies using its Python executable, and verify `Imports OK`.
- [ ] Run **Reload the saved model** before retraining. Confirm that the supplied model returns class 4 for the fictional listing.
- [ ] Download the labeled Kaggle CSV and place it at `data/raw/train.csv`.
- [ ] Run **Train and evaluate**. Confirm 12,464 training listings, 2,529 test listings, and zero shared rescuer IDs.
- [ ] Compare the actual metrics with the P2 results table. Record any differences.
- [ ] Open the generated confusion matrix. Confirm that the cell for actual class 4 and predicted class 4 shows 454.
- [ ] Repeat the **Reload the saved model** command for your platform. Confirm that the reloaded prediction matches the training script's prediction for the same fictional listing.
- [ ] Record the Python version, actual outputs, and any reproduction issues in the Assignment Validation form. Complete and sign the form after testing.

To validate P1 as well, add the three label CSVs, run the notebook using the project `.venv`, and compare the output with the P1 expected results.

## Troubleshooting

| What you see | How to proceed |
|---|---|
| Git or Python is missing | Run `git --version` and the Python version command for your platform. Install the missing tool from [Git](https://git-scm.com/downloads) or [Python](https://www.python.org/downloads/), or use your OS package manager. Reopen the terminal afterward. |
| Linux cannot create the venv or reports missing `ensurepip` | Install your distribution's venv package for the Python version you chose, then retry in a fresh environment. |
| The interpreter points outside the project or a package is missing | Repeat Step 4 using the commands for your platform. For P1, select the same executable in the notebook kernel picker. |
| pip cannot install a dependency | Record the package, error, OS, and Python version. If you tried a different Python version, retry in a fresh Python 3.13 environment. |
| The notebook kernel is missing | Enable the VS Code Python and Jupyter extensions, then reopen the notebook. If the environment is still missing from the picker, register it using the commands below. |
| The saved model is missing or fails to load | Check the commit, the artifact path, and the package versions from Step 4. Record the original artifact check before retraining. Reload the newly trained artifact separately. |
| Kaggle access or a CSV path fails | Sign in and accept the competition rules if prompted. Check that the labeled file is named `train.csv` and is directly inside `data/raw/`. If access remains blocked, record the blocker and complete the saved-model check. |
| Results differ from the expected table | Verify the commit, Python and dependency versions, and input file. Report your actual results and any discrepancies in the validation form. |

### Register the P1 kernel if it is missing

Run the command for your platform from the repository root after Step 4 succeeds.

**Windows (PowerShell or Command Prompt)**

```text
.\.venv\Scripts\python.exe -m ipykernel install --user --name petfinder-validation --display-name "Python (PetFinder validation)"
```

**macOS or Linux**

```sh
./.venv/bin/python -m ipykernel install --user --name petfinder-validation --display-name "Python (PetFinder validation)"
```

Select **Python (PetFinder validation)** in VS Code and rerun the kernel path check in the P1 section.

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
