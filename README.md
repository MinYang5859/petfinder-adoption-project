# PetFinder Adoption Prediction — P1 Initial EDA

This repository contains the initial exploratory data analysis for the PetFinder.my Adoption Prediction project in MSBA 265.

The project examines how pet characteristics and listing information are associated with `AdoptionSpeed`. The P1 analysis focuses on the target distribution, pet type, age, adoption fee, and number of photos.

## Project Question

How are pet characteristics and listing features related to adoption speed, and which features may be useful for a future classification model?

## Dataset

The data comes from the Kaggle competition:

[PetFinder.my Adoption Prediction](https://www.kaggle.com/competitions/petfinder-adoption-prediction/data)

The original dataset is not included in this repository because of its size. A Kaggle account may be required to access and download the competition data.

Download the competition data and place the following files inside `data/raw/`:

```text
train.csv
breed_labels.csv
color_labels.csv
state_labels.csv
```

Only `train.csv` and the three label files are required for the P1 notebook.

Expected folder structure:

```text
petfinder-adoption-project/
├── data/
│   └── raw/
│       ├── train.csv
│       ├── breed_labels.csv
│       ├── color_labels.csv
│       └── state_labels.csv
├── figures/
├── notebooks/
│   └── 01_p1_initial_eda.ipynb
├── P1/
│   ├── 01_p1_initial_eda.html
│   └── 01_p1_initial_eda.pdf
├── .gitignore
├── README.md
└── requirements.txt
```

## Development Environment

The project was developed with:

- Windows 11
- Python 3.11
- VS Code
- Jupyter Notebook

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

You should see files such as `README.md` and `requirements.txt`.

### 2. Create a Python environment

Choose **one** of the following methods.

### Option A: Python venv — Recommended

This option does not require Anaconda or Miniconda.

First, check which Python command is available:

```powershell
py --version
python --version
```

The project was developed with Python 3.11.

If the `py` command is available, create the environment with:

```powershell
py -3.11 -m venv .venv
```

If `py` is unavailable but `python` reports Python 3.11, use:

```powershell
python -m venv .venv
```

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, the PowerShell prompt should begin with:

```text
(.venv)
```

If PowerShell blocks the activation script, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

The execution-policy change applies only to the current PowerShell session.

### Option B: Conda

Use this option only if Anaconda or Miniconda is installed.

Check whether `conda` is available:

```powershell
conda --version
```

Create and activate the environment:

```powershell
conda create -n petfinder-p1 python=3.11 -y
conda activate petfinder-p1
```

If PowerShell reports that `conda` is not recognized, use **Anaconda Prompt** or follow **Option A: Python venv** instead.

### 3. Install the required packages

After activating the selected environment, upgrade `pip`:

```powershell
python -m pip install --upgrade pip
```

Install the project dependencies:

```powershell
python -m pip install -r requirements.txt
```

Confirm that the packages are installed:

```powershell
python -m pip list
```

### 4. Register the Jupyter kernel

Register the active environment as a Jupyter kernel:

```powershell
python -m ipykernel install --user --name petfinder-p1 --display-name "Python (petfinder-p1)"
```

Confirm which Python executable is being used:

```powershell
python -c "import sys; print(sys.executable)"
```

For a `venv` setup, the path should point to:

```text
petfinder-adoption-project\.venv\Scripts\python.exe
```

For a conda setup, the path should point to the `petfinder-p1` conda environment.

### 5. Download and prepare the dataset

1. Open the [Kaggle competition data page](https://www.kaggle.com/competitions/petfinder-adoption-prediction/data).
2. Sign in to Kaggle if required.
3. Download the competition files.
4. Extract the downloaded ZIP file.
5. Copy the following files into `data/raw/`:

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

The filenames must remain unchanged.

### 6. Run the notebook

Open the following notebook in VS Code or Jupyter:

```text
notebooks/01_p1_initial_eda.ipynb
```

In VS Code:

1. Open the notebook.
2. Click the kernel name in the upper-right corner.
3. Select `Python (petfinder-p1)`.
4. Choose **Restart Kernel and Run All Cells**.
5. Wait until every cell finishes.

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

Check the generated figures with:

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

### `conda` is not recognized

Example error:

```text
conda : The term 'conda' is not recognized as the name of a cmdlet
```

Possible causes:

- Anaconda or Miniconda is not installed.
- `conda` is not available in the system `PATH`.
- PowerShell has not been initialized for conda.

Recommended solution: follow **Option A: Python venv**.

If Anaconda is installed, open **Anaconda Prompt** and check:

```powershell
conda --version
```

### `python` is not recognized

Check whether the Windows Python Launcher is available:

```powershell
py --version
```

If `py` works, use:

```powershell
py -3.11 -m venv .venv
```

If neither `python` nor `py` works, install Python 3.11 before continuing.

After installation, close and reopen PowerShell or VS Code.

### PowerShell cannot activate `.venv`

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

### The virtual environment is not active

Run:

```powershell
.\.venv\Scripts\Activate.ps1
```

The prompt should begin with:

```text
(.venv)
```

Verify the Python location:

```powershell
python -c "import sys; print(sys.executable)"
```

### Package installation fails

Confirm that the environment is active, and then run:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Using `python -m pip` helps ensure that packages are installed into the active environment.

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

Do not rename the CSV files or place them inside another subfolder.

### Jupyter kernel is missing

Activate the project environment and run:

```powershell
python -m ipykernel install --user --name petfinder-p1 --display-name "Python (petfinder-p1)"
```

Then reopen the notebook and select `Python (petfinder-p1)`.

### VS Code uses the wrong Python environment

In the notebook:

1. Click the kernel selector in the upper-right corner.
2. Choose **Select Another Kernel** if necessary.
3. Select `Python (petfinder-p1)`.
4. Restart the kernel.
5. Run all cells again.

Verify the active Python path in a notebook cell:

```python
import sys
print(sys.executable)
```

For a `venv` setup, the result should include:

```text
petfinder-adoption-project\.venv\Scripts\python.exe
```

### Figures are not generated

Confirm that the notebook completed all cells without errors.

Then check:

```powershell
Get-ChildItem .\figures
```

If the folder is empty, restart the notebook kernel and select **Run All** again.

## Validation Checklist

The peer validator should independently complete the following steps:

- [ ] Clone the GitHub repository.
- [ ] Create and activate a new Python environment.
- [ ] Install packages from `requirements.txt`.
- [ ] Download and place the four CSV files in `data/raw/`.
- [ ] Open `notebooks/01_p1_initial_eda.ipynb`.
- [ ] Select the correct Jupyter kernel.
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