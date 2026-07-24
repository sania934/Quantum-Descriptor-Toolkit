# ==========================================================
# Quantum Descriptor Toolkit
# app.py
# Part 1 of 3
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px

from calculators.descriptors import (
    calculate_descriptors,
    hartree_to_ev
)

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Quantum Descriptor Toolkit",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown(
    """
<style>

.main-title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#0066cc;
}

.subtitle{
    text-align:center;
    font-size:18px;
    color:gray;
}

.card{
    background-color:#f8f9fa;
    padding:18px;
    border-radius:10px;
    border:1px solid #dddddd;
}

.footer{
    text-align:center;
    color:gray;
    font-size:13px;
}

</style>
""",
    unsafe_allow_html=True,
)

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("⚛️ Quantum Descriptor Toolkit")

st.sidebar.markdown("---")

st.sidebar.markdown("### Navigation")

page = st.sidebar.radio(

    "",

    [

        "🏠 Home",

        "🧪 Single Molecule",

        "📂 Batch Calculator",

        "📊 Visualization",

        "📘 Descriptor Guide",

        "ℹ️ About"

    ]

)

st.sidebar.markdown("---")

st.sidebar.info(

"""
Developer

**Sania Ismaeel**

Computational Chemistry

Conceptual Density Functional Theory

Organic Electronics

Version 1.0
"""

)

# ==========================================================
# HOME PAGE
# ==========================================================

if page == "🏠 Home":

    st.markdown(
        "<h1 class='main-title'>⚛️ Quantum Descriptor Toolkit</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p class='subtitle'>A Python toolkit for Conceptual Density Functional Theory (CDFT) descriptors</p>",
        unsafe_allow_html=True
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("## Features")

        st.markdown("""

✅ HOMO/LUMO Calculator

✅ eV & Hartree Support

✅ Conceptual DFT Descriptors

✅ Interactive Tables

✅ Batch Processing

✅ Plotly Visualization

✅ Excel Export

✅ CSV Export

""")

    with col2:

        st.markdown("## Included Descriptors")

        st.markdown("""

- HOMO

- LUMO

- Energy Gap

- Ionization Potential

- Electron Affinity

- Chemical Potential

- Electronegativity

- Global Hardness

- Global Softness

- Electrophilicity

- Maximum Charge Transfer

- Electron Donating Power

- Electron Accepting Power

""")

    st.divider()

    st.success(

"""
Welcome!

Use the navigation panel on the left to access the calculator,
visualization tools, descriptor guide, and batch processing.
"""

)

# ==========================================================
# SINGLE MOLECULE
# ==========================================================

elif page == "🧪 Single Molecule":

    st.title("🧪 Single Molecule Calculator")

    st.write(
        "Calculate conceptual DFT descriptors directly from HOMO and LUMO energies."
    )

    st.divider()

    unit = st.radio(

        "Energy Unit",

        [

            "eV",

            "Hartree"

        ],

        horizontal=True

    )

    compound = st.text_input(

        "Compound Name",

        placeholder="Example: D1"

    )

    col1, col2 = st.columns(2)

    with col1:

        homo = st.number_input(

            f"HOMO ({unit})",

            format="%.6f"

        )

    with col2:

        lumo = st.number_input(

            f"LUMO ({unit})",

            format="%.6f"

        )

    calculate = st.button(

        "⚛️ Calculate Descriptors",

        use_container_width=True

    )

    # ---------- PART 2 CONTINUES HERE ----------
        # ======================================================
    # CALCULATE
    # ======================================================

    if calculate:

        # ------------------------------------------
        # Convert Hartree to eV
        # ------------------------------------------

        if unit == "Hartree":

            homo = hartree_to_ev(homo)
            lumo = hartree_to_ev(lumo)

        # ------------------------------------------
        # Validation
        # ------------------------------------------

        if homo >= lumo:

            st.error(
                "❌ HOMO must be lower than LUMO.\n\n"
                "Example:\n"
                "HOMO = -5.20 eV\n"
                "LUMO = -2.60 eV"
            )

        else:

            output = calculate_descriptors(homo, lumo)

            descriptors = output["descriptors"]

            summary = output["summary"]

            st.success("Descriptors calculated successfully.")

            st.divider()

            # ==================================================
            # METRIC CARDS
            # ==================================================

            c1, c2, c3 = st.columns(3)

            gap = lumo - homo

            with c1:

                st.metric(

                    label="HOMO",

                    value=f"{homo:.4f} eV"

                )

            with c2:

                st.metric(

                    label="LUMO",

                    value=f"{lumo:.4f} eV"

                )

            with c3:

                st.metric(

                    label="Band Gap",

                    value=f"{gap:.4f} eV"

                )

            st.divider()

            # ==================================================
            # RESULTS TABLE
            # ==================================================

            if compound.strip():

                st.subheader(f"Results : {compound}")

            else:

                st.subheader("Calculated Descriptors")

            df = pd.DataFrame(descriptors)

            st.dataframe(

                df,

                use_container_width=True,

                hide_index=True

            )

            st.divider()

            # ==================================================
            # SCIENTIFIC INTERPRETATION
            # ==================================================

            st.subheader("Scientific Interpretation")

            col1, col2 = st.columns(2)

            with col1:

                st.info(

f"""
### Band Gap

**{summary['Band Gap Interpretation']}**

Energy Gap = **{gap:.4f} eV**

The band gap determines the electronic excitation energy of the molecule.
"""

                )

                st.info(

f"""
### Global Hardness

**{summary['Hardness Interpretation']}**

Hardness reflects molecular stability and resistance toward charge transfer.
"""

                )

            with col2:

                st.info(

f"""
### Electrophilicity

**{summary['Electrophilicity Interpretation']}**

Electrophilicity measures the tendency of a molecule to accept electrons.
"""

                )

                st.info(

"""
### Notes

All descriptors are calculated using
Conceptual Density Functional Theory (CDFT)
based on Koopmans' approximation.
"""

                )

            st.divider()

            # ==================================================
            # BAR CHART
            # ==================================================

            st.subheader("Descriptor Visualization")

            chart_df = df.copy()

            chart_df = chart_df.dropna()

            fig = px.bar(

                chart_df,

                x="Symbol",

                y="Value",

                color="Descriptor",

                text="Value",

                height=500

            )

            fig.update_layout(

                xaxis_title="Descriptor",

                yaxis_title="Value",

                showlegend=False

            )

            st.plotly_chart(

                fig,

                use_container_width=True

            )

            st.divider()

            # ==================================================
            # DOWNLOAD CSV
            # ==================================================

            csv = df.to_csv(index=False)

            st.download_button(

                label="⬇ Download Results (CSV)",

                data=csv,

                file_name="Quantum_Descriptors.csv",

                mime="text/csv",

                use_container_width=True

            )

# ==========================================================
# ---------- PART 3 CONTINUES BELOW ------------------------
# ==========================================================
# ==========================================================
# BATCH CALCULATOR
# ==========================================================

elif page == "📂 Batch Calculator":

    st.title("📂 Batch Descriptor Calculator")

    st.write(
        """
        Upload a CSV or Excel file containing HOMO and LUMO energies.
        The application will calculate all conceptual DFT descriptors.
        """
    )

    uploaded_file = st.file_uploader(
        "Upload CSV or Excel File",
        type=["csv", "xlsx"]
    )

    if uploaded_file is not None:

        if uploaded_file.name.endswith(".csv"):
            data = pd.read_csv(uploaded_file)
        else:
            data = pd.read_excel(uploaded_file)

        st.subheader("Input Data")

        st.dataframe(
            data,
            use_container_width=True,
            hide_index=True
        )

        required = {"HOMO", "LUMO"}

        if required.issubset(data.columns):

            results = []

            for _, row in data.iterrows():

                output = calculate_descriptors(
                    row["HOMO"],
                    row["LUMO"]
                )

                descriptor_values = {
                    item["Symbol"]: item["Value"]
                    for item in output["descriptors"]
                }

                result = row.to_dict()

                result.update(descriptor_values)

                results.append(result)

            result_df = pd.DataFrame(results)

            st.subheader("Calculated Results")

            st.dataframe(
                result_df,
                use_container_width=True,
                hide_index=True
            )

            csv = result_df.to_csv(index=False)

            st.download_button(
                "⬇ Download Results (CSV)",
                csv,
                file_name="Batch_Quantum_Descriptors.csv",
                mime="text/csv",
                use_container_width=True
            )

        else:

            st.error(
                "Input file must contain HOMO and LUMO columns."
            )

# ==========================================================
# VISUALIZATION
# ==========================================================

elif page == "📊 Visualization":

    st.title("📊 Visualization")

    st.info(
        """
        Visualization of batch data will be available
        after uploading a dataset.

        Planned plots:

        • HOMO vs LUMO

        • Band Gap Distribution

        • Hardness Distribution

        • Electrophilicity Distribution

        • Correlation Heatmap
        """
    )

# ==========================================================
# DESCRIPTOR GUIDE
# ==========================================================

elif page == "📘 Descriptor Guide":

    st.title("📘 Descriptor Guide")

    guide = pd.DataFrame({

        "Descriptor":[

            "Energy Gap",

            "Ionization Potential",

            "Electron Affinity",

            "Chemical Potential",

            "Electronegativity",

            "Global Hardness",

            "Global Softness",

            "Electrophilicity",

            "Maximum Charge Transfer",

            "Electron Accepting Power",

            "Electron Donating Power"

        ],

        "Formula":[

            "LUMO − HOMO",

            "−HOMO",

            "−LUMO",

            "(HOMO+LUMO)/2",

            "−μ",

            "(LUMO−HOMO)/2",

            "1/(2η)",

            "μ²/(2η)",

            "−μ/η",

            "(IP+3EA)² / 16(IP−EA)",

            "(3IP+EA)² / 16(IP−EA)"

        ],

        "Units":[

            "eV",

            "eV",

            "eV",

            "eV",

            "eV",

            "eV",

            "eV⁻¹",

            "eV",

            "-",

            "eV",

            "eV"

        ]

    })

    st.dataframe(

        guide,

        use_container_width=True,

        hide_index=True

    )

# ==========================================================
# ABOUT
# ==========================================================

elif page == "ℹ️ About":

    st.title("ℹ️ About")

    st.markdown("""

## Quantum Descriptor Toolkit

A Python application developed for calculating
Conceptual Density Functional Theory (CDFT)
descriptors from HOMO and LUMO energies.

---

### Features

- HOMO/LUMO Calculator
- eV and Hartree Conversion
- Conceptual DFT Descriptors
- Batch Processing
- Interactive Visualization
- CSV Export

---

### Developed By

**Sania Ismaeel**

Computational Chemistry

---

### Built With

- Python
- Streamlit
- Pandas
- Plotly

""")

# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.caption(
    "Quantum Descriptor Toolkit (QDT) | Version 1.0 | © 2026 Sania Ismaeel"
)