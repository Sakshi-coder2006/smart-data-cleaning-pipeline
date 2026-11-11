# Smart Data Cleaning Pipeline for Machine Learning

## Project Description
The Smart Data Cleaning Pipeline is a Python-based project that cleans raw and messy datasets and prepares them for Machine Learning applications.

It identifies missing values, removes duplicate records, performs text normalization, and generates a clean dataset.

## Features
- Detects missing values.
- Handles missing values.
- Removes duplicate records.
- Performs text normalization.
- Generates a cleaned CSV dataset.

## Technologies Used
- Python
- Pandas
- NumPy

## Project Structure

```text
Data-Cleaning-Pipeline/
│
├── dataset/
│   └── messy_data.csv
│
├── output/
│   └── cleaned_data.csv
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone this repository.
2. Install the required libraries:

```bash
pip install -r requirements.txt
```

## How to Run

Run the following command:

```bash
python main.py
```

The cleaned dataset will be saved in the `output` folder as `cleaned_data.csv`.

## Expected Output

A cleaned CSV file with:
- Missing values handled.
- Duplicate records removed.
- Text values standardized.

## Author
Sakshi C.H.
