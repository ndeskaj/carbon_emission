import json

# Load the notebook
with open('carbon_emission_analysis.ipynb', 'r') as f:
    notebook = json.load(f)

# Find the cell with grangercausalitytests
for i, cell in enumerate(notebook['cells']):
    if cell['cell_type'] == 'code' and any('grangercausalitytests' in line for line in cell.get('source', [])):
        # Add warning filter at the beginning of the cell
        warning_filter = [
            "# Suppress FutureWarning about verbose parameter in statsmodels\n",
            "import warnings\n",
            "warnings.filterwarnings('ignore', category=FutureWarning, message='verbose is deprecated')\n",
            "\n"
        ]
        cell['source'] = warning_filter + cell['source']
        notebook['cells'][i] = cell
        print(f"Added warning filter to cell {i}")
        break

# Save the modified notebook
with open('carbon_emission_analysis.ipynb', 'w') as f:
    json.dump(notebook, f, indent=1)

print("Notebook updated successfully!") 