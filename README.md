# ⚛️ Quantum Descriptor Toolkit (QDT)

A web-based Python application for calculating **Conceptual Density Functional Theory (CDFT)** descriptors directly from HOMO and LUMO energies.

The toolkit supports both **electron volts (eV)** and **Hartree** units, making it useful for researchers performing quantum chemical calculations using software such as Gaussian, ORCA, and other electronic structure packages.

---

🌐 Live Demo

**Application**

https://quantum-descriptor-toolkit.streamlit.app/ 

---

# GitHub Repository

https://github.com/sania934/Quantum-Descriptor-Toolkit

---

# Features

- Calculate Conceptual DFT descriptors
- Supports HOMO/LUMO values in eV and Hartree
- Automatic unit conversion
- Batch calculations using CSV and Excel
- Interactive visualization
- Download calculated descriptors
- Scientific descriptor guide


# Calculated Descriptors

The toolkit calculates:

- HOMO Energy
- LUMO Energy
- Energy Gap (Eg)
- Ionization Potential (IP)
- Electron Affinity (EA)
- Chemical Potential (μ)
- Electronegativity (χ)
- Global Hardness (η)
- Global Softness (S)
- Electrophilicity Index (ω)
- Maximum Charge Transfer (ΔNmax)
- Electron Accepting Power (ω⁺)
- Electron Donating Power (ω⁻)
- Net Electrophilicity (Δω)


# Input

Example

| Compound | HOMO | LUMO |
|-----------|------|------|
| D1 | -4.25 | -2.25 |
| D2 | -4.70 | -2.59 |

---

#  Packages Used

- Python
- Streamlit
- Pandas
- Plotly
- OpenPyXL


# Installation

Clone the repository

```bash
git clone https://github.com/sania934/Quantum-Descriptor-Toolkit.git
```

Install packages

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

# Scientific Background

The descriptors implemented in this application are based on **Conceptual Density Functional Theory (CDFT)** using Koopmans' approximation.

---

# Future Development

- Gaussian log parser
- ORCA output parser
- PDF report generation
- Additional quantum chemical descriptors
- Improved visualization

---

# Author

**Sania Ismaeel**

PhD Computational Chemistry

University of Agriculture Faisalabad

GitHub

https://github.com/sania934

---

# License

MIT License
