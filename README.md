# CSV Data Analyzer

The project is being developed incrementally, beginning with basic CSV file handling and progressing toward data inspection, validation, duplicate detection, analysis, and report generation.

## Project Purpose

To learn practical Python and CSV/data-handling concepts,
by progressively building a program capable of inspecting and eventually analysing CSV data.

## Project Goals

- Load CSV files
- Inspect their structure
- Identify data-quality problems
- Detect duplicate records
- Perform basic analysis
- Generate useful summaries/reports

## Current Progress

### Stage 1 — Load the CSV

The program opens the sample CSV file, reads its contents as text, and displays the data in the terminal.

### Stage 2 — Understand and Search the Data

The program now:

- Identifies the header and records
- Separates records into individual fields
- Represents each record as a dictionary
- Stores all 20 records in a list of dictionaries
- Allows the user to search for a record by Load ID
- Handles differences in user input such as lowercase letters and extra spaces
- Displays matching records in a more readable format
- Gives the user a message when a Load ID cannot be found

### Stage 3 — Data Validation and Interactive Application

The program can now perform several data-quality checks:

Check for missing values
Check for unexpected status values
Check for duplicate Load IDs
Validate numeric fields
Validate dates
Identify different types of data-quality problems in a deliberately messy dataset

The validation system has been integrated into an interactive command-line application.

The current menu allows the user to:

Look up a Load ID
Run a Validation Quick Check
Quit the program

The program uses functions and a while loop to allow the user to perform multiple operations during the same session.

Stage 4 — Data Cleaning

Planned next:

Identify which problems can be safely corrected automatically
Standardise inconsistent values
Handle missing and invalid data appropriately
Investigate duplicate records
Preserve the original dataset
Create and verify a cleaned dataset
Future Stages

The project will eventually include:

Basic data analysis
Functions and modular code
pandas
Data cleaning
Simple reporting
Improved user interaction
Potentially generating reports from the analysed data

## License

This project is licensed under the MIT License.