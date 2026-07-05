## Project Structure
election-analysis/
- data/
  - raw_data.csv
  - cleaned_data.csv
- notebooks/
  - analysis.ipynb
- visualizations/
  - dashboard.py
- report.pdf
- README.md
- requirements.txt

## Key Findings
- Islamabad had the highest voter turnout (~58%); Khyber Pakhtunkhwa the lowest (~44%)
- Pakistan Tehreek-e-Insaf (PTI) won the most seats nationally (331)
- Punjab had the most competitive races; Islamabad the least competitive
- Turnout and winning margin show a weak negative correlation (-0.20)

## How to Run
1. Install dependencies: pip install -r requirements.txt
2. Open notebooks/analysis.ipynb in Jupyter/VS Code to view the analysis
3. Run the dashboard: python visualizations/dashboard.py

## Tools Used
Python, Pandas, Matplotlib, Seaborn, Tkinter, Jupyter Notebook