# PetFinder Adoption Prediction — P1 Initial EDA

This repository contains the initial exploratory data analysis for the PetFinder.my Adoption Prediction project in MSBA 265.

The project examines how pet characteristics and listing information are associated with `AdoptionSpeed`. The P1 analysis focuses on the target distribution, pet type, age, adoption fee, and number of photos.

## Project Question

How are pet characteristics and listing features related to adoption speed, and which features may be useful for a future classification model?

## Dataset

The data comes from the Kaggle competition:

[PetFinder.my Adoption Prediction](https://www.kaggle.com/competitions/petfinder-adoption-prediction/data)

The original dataset is not included in this repository because of its size and Kaggle access requirements. A Kaggle account may be required to download the competition data.

Download the competition data and place the following files inside `data/raw/`:

```text
train.csv
breed_labels.csv
color_labels.csv
state_labels.csv
```

Only `train.csv` and the three label files are required for the P1 notebook.

## Project Structure

After cloning the repository, the `data/raw/` folder contains only `.gitkeep`. The original dataset is not included in GitHub.

```text
petfinder-adoption-project/
├── data/
│   └── raw/
│       └── .gitkeep
├── figures/
├── notebooks/
│   └── 01_p1_initial_eda.ipynb
├── P1/
│   └── 01_p1_initial_eda.html
├── .gitignore
├── README.md
└── requirements.txt
```

After downloading the required data files, place them inside `data/raw/`. The local project structure should then look like this:

```text
petfinder-adoption-project/
├── data/
│   └── raw/
│       ├── .gitkeep
│       ├── train.csv
│       ├── breed_labels.csv
│       ├── color_labels.csv
│       └── state_labels.csv
├── figures/
├── notebooks/
│   └── 01_p1_initial_eda.ipynb
├── P1/
│   └── 01_p1_initial_eda.html
├── .gitignore
├── README.md
└── requirements.txt
```

The CSV files are stored locally and ignored by Git. They will not appear in the GitHub repository.

## Development Environment

The project was developed and tested with:

- Windows 11
- Python 3.11
- VS Code
- Jupyter Notebook

Python 3.11 is recommended for reproducibility.

A newer Python version, such as Python 3.12, 3.13, or 3.14, may work, but it has not been fully tested for this project. A higher version number does not automatically guarantee compatibility because some Python packages may not yet support the newest Python release.

Python 3.11 and Python 3.14 can be installed on the same Windows computer. They do not need to replace each other. The Windows Python Launcher, `py`, can be used to select the required version.

## Setup Instructions

### 1. Clone the repository

Open PowerShell or the VS Code terminal and run:

```powershell
git clone https://github.com/MinYang5859/petfinder-adoption-project.git
cd petfinder-adoption-project
```

Confirm that you are inside the project folder:

```powershell
Get-Location
Get-ChildItem
```

You should see files and folders such as:

```text
README.md
requirements.txt
notebooks
data
figures
P1
```

## 2. Check the Available Python Versions

Before creating an environment, check the installed Python versions.

Run:

```powershell
py -0p
```

This command displays all Python versions recognized by the Windows Python Launcher.

You can also run:

```powershell
py --version
python --version
```

Example output from `py -0p`:

```text
-V:3.14 * C:\Users\username\AppData\Local\Programs\Python\Python314\python.exe
-V:3.11   C:\Users\username\AppData\Local\Programs\Python\Python311\python.exe
```

This example means that both Python 3.14 and Python 3.11 are installed.

The `*` identifies the current default version. The project does not need to use the default version because a specific version can be selected with `py -3.11`.

## 3. Choose the Python Setup

Use the first option that matches your computer.

### Option A: Python 3.11 Is Already Installed — Recommended

Confirm that Python 3.11 is available:

```powershell
py -3.11 --version
```

Expected output:

```text
Python 3.11.x
```

Create the virtual environment with Python 3.11:

```powershell
py -3.11 -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, the PowerShell prompt should begin with:

```text
(.venv)
```

Verify the Python version inside the environment:

```powershell
python --version
```

Expected output:

```text
Python 3.11.x
```

Also verify the Python location:

```powershell
python -c "import sys; print(sys.executable)"
```

The result should point to a path similar to:

```text
petfinder-adoption-project\.venv\Scripts\python.exe
```

### Option B: Only Python 3.14 Is Installed — Install Python 3.11

If `py -0p` shows Python 3.14 but does not show Python 3.11, install Python 3.11 separately.

Python 3.14 does not need to be removed.

Install Python 3.11 with Windows Package Manager:

```powershell
winget install --id Python.Python.3.11 -e
```

After installation:

1. Close PowerShell.
2. Close VS Code.
3. Reopen VS Code.
4. Open the project folder again.
5. Open a new PowerShell terminal.

Confirm that Python 3.11 is now available:

```powershell
py -0p
py -3.11 --version
```

Then create the environment:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
```

The final command should show:

```text
Python 3.11.x
```

### Option C: Test Python 3.14 — Use Only If Python 3.11 Cannot Be Installed

Python 3.14 may work, but this project was not developed or fully tested with Python 3.14.

To test it, create a separate virtual environment:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
```

Expected output:

```text
Python 3.14.x
```

Continue with the package installation instructions below.

Python 3.14 can be considered usable for this project only if:

- All packages install successfully.
- The Jupyter kernel starts successfully.
- Every notebook cell runs without errors.
- All five expected figures are generated.
- The final verification checks match the expected results.

If package installation or notebook execution fails, delete or deactivate the test environment and use Python 3.11 instead.

To leave the active environment:

```powershell
deactivate
```

### Option D: Use Conda

Use this option only if Anaconda or Miniconda is already installed.

Check whether `conda` is available:

```powershell
conda --version
```

Create and activate the environment:

```powershell
conda create -n petfinder-p1 python=3.11 -y
conda activate petfinder-p1
```

Verify the version:

```powershell
python --version
```

Expected output:

```text
Python 3.11.x
```

If PowerShell reports that `conda` is not recognized, use Anaconda Prompt or follow Option A or Option B.

## 4. Activate the Virtual Environment

If you created `.venv`, activate it whenever you reopen the project:

```powershell
.\.venv\Scripts\Activate.ps1
```

The prompt should begin with:

```text
(.venv)
```

If PowerShell blocks the activation script, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

The policy change applies only to the current PowerShell session.

After activation, verify the environment:

```powershell
python --version
python -c "import sys; print(sys.executable)"
```

## 5. Install the Required Packages

Make sure the correct environment is active before installing packages.

Upgrade `pip`:

```powershell
python -m pip install --upgrade pip
```

Install the project dependencies:

```powershell
python -m pip install -r requirements.txt
```

Using `python -m pip` helps ensure that the packages are installed in the active environment.

Confirm that the packages are installed:

```powershell
python -m pip list
```

Check the main imports:

```powershell
python -c "import numpy, pandas, matplotlib, seaborn; print('Package import test passed.')"
```

Expected output:

```text
Package import test passed.
```

## 6. Register the Jupyter Kernel

Register the active environment as a Jupyter kernel:

```powershell
python -m ipykernel install --user --name petfinder-p1 --display-name "Python (petfinder-p1)"
```

The display name `Python (petfinder-p1)` should appear in the VS Code notebook kernel list.

## 7. Download and Prepare the Dataset

1. Open the [Kaggle competition data page](https://www.kaggle.com/competitions/petfinder-adoption-prediction/data).
2. Sign in to Kaggle if required.
3. Accept the competition rules if required.
4. Download the competition data.
5. Extract the downloaded ZIP file.
6. Copy the required files into `data/raw/`.

Required files:

```text
train.csv
breed_labels.csv
color_labels.csv
state_labels.csv
```

Confirm that the files are in the correct location:

```powershell
Get-ChildItem .\data\raw
```

Do not rename the files.

Do not place them inside another folder under `data/raw/`.

Correct:

```text
data/raw/train.csv
```

Incorrect:

```text
data/raw/train/train.csv
```

## 8. Run the Notebook

Open the following notebook in VS Code:

```text
notebooks/01_p1_initial_eda.ipynb
```

In VS Code:

1. Open the notebook.
2. Click the kernel name in the upper-right corner.
3. Select `Python (petfinder-p1)`.
4. If it is not visible, choose **Select Another Kernel**.
5. Select **Restart Kernel and Run All Cells**.
6. Wait until every cell finishes.

The notebook should complete without runtime errors.

## Expected Results

A successful run should:

- Load 14,993 training records.
- Report zero missing values in `AgeGroup`.
- Report zero missing values in `FeeGroup`.
- Report zero missing values in `PhotoGroup`.
- Generate five figures in the `figures/` folder.
- Complete all notebook cells without runtime errors.

Expected figure files:

```text
adoption_speed_distribution.png
adoption_speed_by_pet_type.png
adoption_speed_by_age_group.png
adoption_speed_by_fee_group.png
adoption_speed_by_photo_group.png
```

Check the generated figures:

```powershell
Get-ChildItem .\figures
```

## Main P1 Findings

- `AdoptionSpeed` is not evenly distributed across the five classes.
- Cats have a slightly lower average `AdoptionSpeed` than dogs.
- Pets aged 0–5 months generally appear in faster adoption classes.
- Adoption fee does not show a simple linear relationship with adoption speed.
- Listings without photos have the highest average `AdoptionSpeed`.
- The percentage of `AdoptionSpeed 4` generally decreases as the number of photos increases.

These findings show associations and do not prove causation.

## Repository Contents

- `notebooks/01_p1_initial_eda.ipynb`: complete P1 analysis
- `figures/`: figures generated by the notebook
- `P1/01_p1_initial_eda.html`: browser-readable notebook export
- `P1/01_p1_initial_eda.pdf`: PDF notebook export
- `requirements.txt`: required Python packages
- `.gitignore`: excludes the original Kaggle dataset, local environments, and temporary files
- `data/raw/.gitkeep`: preserves the required data folder structure

## Troubleshooting

### `conda` Is Not Recognized

Example error:

```text
conda : The term 'conda' is not recognized as the name of a cmdlet
```

Possible causes:

- Anaconda or Miniconda is not installed.
- `conda` is not available in the system `PATH`.
- PowerShell has not been initialized for conda.

Recommended solution: use the Python `venv` setup instead.

If Anaconda is installed, open Anaconda Prompt and run:

```powershell
conda --version
```

### Only Python 3.14 Is Available

Check the installed versions:

```powershell
py -0p
```

If Python 3.11 is missing, install it:

```powershell
winget install --id Python.Python.3.11 -e
```

Close and reopen VS Code after installation.

Then run:

```powershell
py -3.11 --version
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
```

Python 3.14 does not need to be uninstalled.

### `py -3.11` Reports That No Suitable Python Runtime Was Found

This means Python 3.11 is not installed or is not recognized by the Python Launcher.

Check:

```powershell
py -0p
```

Install Python 3.11:

```powershell
winget install --id Python.Python.3.11 -e
```

Then close and reopen PowerShell or VS Code.

### `py` Is Not Recognized

Try:

```powershell
python --version
```

If `python` reports Python 3.11, create the environment with:

```powershell
python -m venv .venv
```

If neither `py` nor `python` works, Python is not installed correctly or is not available in `PATH`.

Install Python 3.11 and reopen the terminal.

### PowerShell Cannot Activate `.venv`

Example error:

```text
running scripts is disabled on this system
```

Run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

This change affects only the current PowerShell session.

### The Environment Uses the Wrong Python Version

Activate the environment and check:

```powershell
python --version
python -c "import sys; print(sys.executable)"
```

If the environment was created with the wrong Python version, deactivate it:

```powershell
deactivate
```

Remove the `.venv` folder using File Explorer, or use PowerShell after confirming that you are in the project folder:

```powershell
Remove-Item -Recurse -Force .\.venv
```

Then recreate it with Python 3.11:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
```

Warning: run the removal command only from the project folder and only when `.venv` is the intended environment folder.

### Package Installation Fails on Python 3.14

Possible cause: one or more dependencies may not yet provide a compatible release for Python 3.14.

Verify the active version:

```powershell
python --version
```

If it shows Python 3.14, switch to Python 3.11:

```powershell
deactivate
```

Create a new Python 3.11 environment:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### The Virtual Environment Is Not Active

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

The prompt should begin with:

```text
(.venv)
```

Confirm the environment path:

```powershell
python -c "import sys; print(sys.executable)"
```

### `FileNotFoundError`

Confirm that the required CSV files are located directly inside:

```text
data/raw/
```

Check the folder:

```powershell
Get-ChildItem .\data\raw
```

The folder must contain:

```text
train.csv
breed_labels.csv
color_labels.csv
state_labels.csv
```

Do not rename the CSV files.

### Jupyter Kernel Is Missing

Activate the project environment and register it again:

```powershell
python -m ipykernel install --user --name petfinder-p1 --display-name "Python (petfinder-p1)"
```

Then reopen the notebook and select `Python (petfinder-p1)`.

### VS Code Uses the Wrong Python Environment

In the notebook:

1. Click the kernel selector in the upper-right corner.
2. Choose **Select Another Kernel**.
3. Select `Python (petfinder-p1)`.
4. Restart the kernel.
5. Run all cells again.

Verify the active environment in a notebook cell:

```python
import sys

print(sys.version)
print(sys.executable)
```

The executable should point to the project `.venv` or the `petfinder-p1` conda environment.

### Figures Are Not Generated

Confirm that the notebook completed all cells without errors.

Check the output folder:

```powershell
Get-ChildItem .\figures
```

If the figure files are missing:

1. Confirm that the correct kernel is selected.
2. Confirm that the CSV files are in `data/raw/`.
3. Restart the notebook kernel.
4. Run all cells again.
5. Review the first cell that reports an error.

## Final Environment Verification

Before validation, run:

```powershell
python --version
python -c "import sys; print(sys.executable)"
python -c "import numpy, pandas, matplotlib, seaborn; print('Package import test passed.')"
Get-ChildItem .\data\raw
Get-ChildItem .\figures
```

Recommended Python result:

```text
Python 3.11.x
```

The final notebook verification should report:

```text
Training rows: 14993
Missing AgeGroup values: 0
Missing FeeGroup values: 0
Missing PhotoGroup values: 0
```

All five expected figure checks should return `True`.

## Validation Checklist

The peer validator should independently complete the following steps:

- [ ] Clone the GitHub repository.
- [ ] Check the installed Python versions with `py -0p`.
- [ ] Use Python 3.11 when available.
- [ ] Install Python 3.11 separately if the computer has only Python 3.14.
- [ ] Create and activate a new environment.
- [ ] Confirm the active Python version.
- [ ] Install packages from `requirements.txt`.
- [ ] Download and place the four CSV files in `data/raw/`.
- [ ] Open `notebooks/01_p1_initial_eda.ipynb`.
- [ ] Select `Python (petfinder-p1)` as the kernel.
- [ ] Restart the kernel and run all cells.
- [ ] Confirm that all cells finish without runtime errors.
- [ ] Confirm that all five figure files are generated.
- [ ] Record any error and the steps used to resolve it.
- [ ] Complete and sign the Assignment Validation form.

## References

PetFinder.my. (n.d.). *About PetFinder.my*.  
https://www.petfinder.my/about.htm

PetFinder.my. (2018). *PetFinder.my adoption prediction* [Data set]. Kaggle.  
https://www.kaggle.com/competitions/petfinder-adoption-prediction

## Author

Min Yang  
MSBA 265 — Special Analytics Topics  
University of the Pacific