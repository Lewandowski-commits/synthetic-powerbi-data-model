# Synthetic Power BI data model

Quick script to generate 4 CSVs for a star schema to be used within PowerBI (or any data model). The generated files will contain:
- list of salesmen and their metadata
- list of pharmaceutical products
- list of manufacturing companies/sites
- fact/sales data

## Usage
1. Activate the virtual environment:
```
/.venv/Scripts/Activate.ps1
```
2. Run main.py to use default arguments:
```
python main.py
```
or import it as a module to call the main function and specify the number of rows to be produced for each DF, and how many years the fact data should go back from today.

3. The files will be generated in the directory where main.py was executed.
