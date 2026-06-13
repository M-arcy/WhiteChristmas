# Beyond the Waiting Room — Data-Driven Appointment Predictions

## Table of Contents

- [Description](#description)
- [Key Results](#key-results)
- [Visuals](#visuals)
- [Installation](#installation)
- [Usage](#usage)
- [Author](#author)

<hr style="border: none; height: 10px; background-color: #003057;" />

## Name

Predicting Patient No-Shows Using Machine Learning — Healthcare Appointment Analysis

## Description

Patient no-shows are a significant operational problem for healthcare providers: missed appointments waste clinical capacity, delay care for other patients, and increase costs. This project analyzes __110,527 medical appointments__ from Brazil in 2016 to build a model that predicts whether a patient will show up — giving providers the opportunity to intervene in advance.

The project follows the __CRISP-DM methodology__ across the full data science workflow: understanding the business problem, exploring data distributions, engineering features, training and comparing multiple classifiers, and evaluating real-world performance.

**Project hypothesis:** Patients who face socioeconomic challenges, chronic conditions, or limited access to healthcare resources are more likely to miss their appointments. SMS reminders may help, but their effectiveness varies by circumstance.

This project has these files:
- `main.py` — entry point that coordinates data loading, model training, and evaluation
- `data.py` — data loading, cleaning, and feature engineering (including `waiting_time` calculation)
- `model.py` — model definitions and training logic for all three classifiers
- `model_tuning.py` — hyperparameter optimization for the gradient boosting model
- `demo.py` — demonstration script showing the model in use
- `tests/` — unit and integration test suite with GitHub Actions CI
- `models/` — saved model files (persisted with joblib)
- `data/` — dataset files
- `screenshots/` — project visualizations
- `requirements.txt` — lists all packages and dependencies required to run the project
- `README.md` — provides an overview of the project

[Back to Top](#table-of-contents)

## Key Results

**Dataset:** 110,527 appointment records, including patient demographics, health conditions (hypertension, diabetes, alcoholism), socioeconomic indicators (scholarship status), appointment timing, and SMS reminder receipt.

**Models compared:**
| Model | Notes |
|---|---|
| Logistic Regression | Baseline classifier |
| Random Forest | Ensemble method — handles nonlinear relationships |
| Gradient Boosting | Best performer after hyperparameter tuning |

**Best model — tuned Gradient Boosting Classifier:**
- __Accuracy: ~71.5%__
- __Precision: ~63%__
- Recall was initially low at 2%, indicating class imbalance — a known challenge with no-show datasets where the majority class (patients who show up) dominates

**Key engineered feature:**
- `waiting_time` — the number of days between when an appointment was scheduled and when it was due. Longer waits are associated with higher no-show rates, making this one of the most predictive features in the dataset.

**Why gradient boosting outperformed the alternatives:**
Gradient boosting builds models sequentially, with each new model correcting the errors of the previous one. For a dataset with class imbalance and complex nonlinear interactions between socioeconomic and health variables, this iterative error-correction approach captures patterns that logistic regression (which assumes linear relationships) cannot.

[Back to Top](#table-of-contents)

## Visuals

Performance visualizations are saved in the `screenshots/` folder and include:
- Feature importance charts showing which variables most strongly predict no-shows
- Model comparison charts across accuracy, precision, recall, and F1-score
- Distribution plots from the exploratory analysis phase

## Installation

Clone the repository:

```bash
git clone https://github.com/M-arcy/Beyond-the-Waiting-Room-Data-Driven-Appointment-Predictions.git
cd Beyond-the-Waiting-Room-Data-Driven-Appointment-Predictions
```

Create and activate a virtual environment (recommended):

```bash
python -m venv venv
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

[Back to Top](#table-of-contents)

## Usage

Run the full pipeline — data loading, model training, and evaluation:

```bash
python main.py
```

To see the model in action on sample inputs:

```bash
python demo.py
```

To run the test suite:

```bash
python -m pytest tests/
```

The dataset is publicly available on [Kaggle](https://www.kaggle.com/joniarroba/noshowappointments).

[Back to Top](#table-of-contents)

## Support

For questions, open an issue on the [GitHub repository](https://github.com/M-arcy/Beyond-the-Waiting-Room-Data-Driven-Appointment-Predictions/issues) or reach out via [LinkedIn](https://www.linkedin.com/in/marcy-misner/).

## Author

Developed by __Marcy Misner__.

For more of my work: [GitHub](https://github.com/M-arcy) | [LinkedIn](https://www.linkedin.com/in/marcy-misner/)

## License

This project is licensed under the MIT License.

[Back to Top](#table-of-contents)
