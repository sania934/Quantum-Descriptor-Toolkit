# ==========================================================
# Quantum Descriptor Toolkit (QDT)
# app.py
#
# Author: Sania Ismaeel
# Version: 2.0
# ==========================================================

import streamlit as st
import pandas as pd

from calculators.descriptors import (
    calculate_descriptors,
    hartree_to_ev
)

from calculators.descriptor_info import (
    DESCRIPTOR_INFO
)

from calculators.bibliography import (
    BIBLIOGRAPHY
)

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Quantum Descriptor Toolkit",
    page_icon="assets/logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# SESSION STATE
# ==========================================================

if "descriptors" not in st.session_state:
    st.session_state.descriptors = None

if "summary" not in st.session_state:
    st.session_state.summary = None

if "result_df" not in st.session_state:
    st.session_state.result_df = None

if "compound" not in st.session_state:
    st.session_state.compound = ""

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

.footer{
    text-align:center;
    color:gray;
    font-size:13px;
}

</style>
""",
    unsafe_allow_html=True
)

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.image(
    "assets/logo.png",
    width=180
)

st.sidebar.title("Quantum Descriptor Toolkit")

st.sidebar.markdown("---")

page = st.sidebar.radio(

    "Navigation",

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

st.sidebar.success("Version 2.0")

st.sidebar.info(
"""
Developer

**Sania Ismaeel**

Computational Chemistry

Conceptual Density Functional Theory

Organic Electronics
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

        st.subheader("Features")

        st.markdown("""

- HOMO/LUMO Calculator
- eV & Hartree Support
- 14 Conceptual DFT Descriptors
- Scientific Interpretation
- Batch Processing
- Interactive Visualization
- CSV Export

""")

    with col2:

        st.subheader("Included Descriptors")

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
- Electron Accepting Power
- Electron Donating Power
- Net Electrophilicity

""")

    st.divider()

    st.success(
"""
Welcome to the Quantum Descriptor Toolkit.

Use the navigation panel to calculate descriptors,
process multiple molecules, visualize results,
and explore the scientific meaning of each descriptor.
"""
    )

# ==========================================================
# SINGLE MOLECULE
# ==========================================================

elif page == "🧪 Single Molecule":

    st.title("🧪 Single Molecule Calculator")

    st.write(
        "Calculate Conceptual DFT descriptors from HOMO and LUMO energies."
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

        value=st.session_state.compound,

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
        # ======================================================
    # CALCULATE
    # ======================================================

    if calculate:

        if unit == "Hartree":

            homo = hartree_to_ev(homo)
            lumo = hartree_to_ev(lumo)

        if homo >= lumo:

            st.error(
                "HOMO energy must be lower than LUMO energy."
            )

        else:

            output = calculate_descriptors(
                homo,
                lumo
            )

            st.session_state.descriptors = output["descriptors"]
            st.session_state.summary = output["summary"]
            st.session_state.compound = compound

            st.success("Descriptors calculated successfully.")

    # ======================================================
    # DISPLAY RESULTS
    # ======================================================

    if st.session_state.descriptors is not None:

        descriptors = st.session_state.descriptors
        summary = st.session_state.summary
        compound = st.session_state.compound

        st.divider()

        # ==================================================
        # METRIC CARDS
        # ==================================================

        homo_value = None
        lumo_value = None
        gap_value = None

        for item in descriptors:

            if item["Symbol"] == "HOMO":
                homo_value = item["Value"]

            elif item["Symbol"] == "LUMO":
                lumo_value = item["Value"]

            elif item["Symbol"] == "Eg":
                gap_value = item["Value"]

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "HOMO",
                f"{float(homo_value):.4f} eV"
            )

        with c2:

            st.metric(
                "LUMO",
                f"{float(lumo_value):.4f} eV"
            )

        with c3:

            st.metric(
                "Energy Gap",
                f"{float(gap_value):.4f} eV"
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

        st.subheader("📚 Scientific Interpretation")

        descriptor_names = {
            item["Descriptor"]: item["Symbol"]
            for item in descriptors
        }

        selected = st.selectbox(
            "Select a Descriptor",
            list(descriptor_names.keys()),
            key="descriptor_select"
        )

        symbol = descriptor_names[selected]

        info = DESCRIPTOR_INFO[symbol]

        reference = BIBLIOGRAPHY[
            info["reference_id"]
        ]

        st.markdown(f"## {info['name']}")

        st.markdown(
            f"**Symbol:** {info['symbol']}"
        )

        st.markdown(
            f"**Equation:** `{info['equation']}`"
        )

        st.markdown(
            f"**Unit:** {info['unit']}"
        )

        st.divider()

        with st.expander(
            "📖 Definition",
            expanded=True
        ):

            st.write(
                info["definition"]
            )

        with st.expander(
            "💡 General Interpretation"
        ):

            st.write(
                info["interpretation"]
            )

        with st.expander(
            "📝 Remarks"
        ):

            st.write(
                info["remarks"]
            )

        with st.expander(
            "📚 Primary Reference"
        ):

            st.write(
                reference["authors"]
            )

            st.write(
                reference["title"]
            )

            if reference["volume"]:

                st.write(
                    f"{reference['journal']}, "
                    f"{reference['volume']}, "
                    f"{reference['pages']} "
                    f"({reference['year']})"
                )

            else:

                st.write(
                    f"{reference['journal']} "
                    f"({reference['year']})"
                )

            if reference["doi"]:

                st.code(
                    reference["doi"]
                )

        st.divider()

# ==========================================================
# BATCH CALCULATOR
# ==========================================================

elif page == "📂 Batch Calculator":

    st.title("📂 Batch Descriptor Calculator")

    st.write(
        "Upload a CSV or Excel file containing HOMO and LUMO energies."
    )

    uploaded_file = st.file_uploader(

        "Upload CSV or Excel File",

        type=[
            "csv",
            "xlsx"
        ]

    )

    if uploaded_file is not None:

        if uploaded_file.name.endswith(".csv"):

            data = pd.read_csv(
                uploaded_file
            )

        else:

            data = pd.read_excel(
                uploaded_file
            )

        st.subheader("Input Data")

        st.dataframe(

            data,

            use_container_width=True,

            hide_index=True

        )

        required = {
            "HOMO",
            "LUMO"
        }

        if required.issubset(
            data.columns
        ):

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

                result.update(
                    descriptor_values
                )

                results.append(
                    result
                )

            result_df = pd.DataFrame(
                results
            )

            st.session_state.result_df = result_df

            st.subheader(
                "Calculated Results"
            )

            st.dataframe(

                result_df,

                use_container_width=True,

                hide_index=True

            )

            csv = result_df.to_csv(
                index=False
            )

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

    st.title("📊 Publication Figure Studio")

    if st.session_state.result_df is None:

        st.warning(
            """
No batch calculation results found.

Please go to **Batch Calculator**, upload a dataset,
and calculate descriptors first.
"""
        )

    else:

        from calculators.figure_studio import publication_figure_studio

        publication_figure_studio(
            st.session_state.result_df
        )

# ==========================================================
# DESCRIPTOR GUIDE
# ==========================================================

elif page == "📘 Descriptor Guide":

    st.title("📘 Descriptor Guide")

    st.write(
        """
This guide summarizes all Conceptual DFT descriptors
implemented in the Quantum Descriptor Toolkit.
"""
    )

    descriptor_table = []

    for symbol, info in DESCRIPTOR_INFO.items():

        descriptor_table.append({

            "Descriptor": info["name"],

            "Symbol": info["symbol"],

            "Equation": info["equation"],

            "Unit": info["unit"]

        })

    guide_df = pd.DataFrame(
        descriptor_table
    )

    st.dataframe(

        guide_df,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    st.subheader("Scientific Definitions")

    for symbol, info in DESCRIPTOR_INFO.items():

        with st.expander(

            f"{info['name']} ({info['symbol']})"

        ):

            st.markdown(
                f"**Equation:** `{info['equation']}`"
            )

            st.markdown(
                f"**Unit:** {info['unit']}"
            )

            st.markdown("**Definition**")

            st.write(
                info["definition"]
            )

            st.markdown("**Interpretation**")

            st.write(
                info["interpretation"]
            )

            st.markdown("**Remarks**")

            st.write(
                info["remarks"]
            )

            reference = BIBLIOGRAPHY[
                info["reference_id"]
            ]

            st.markdown(
                "**Primary Reference**"
            )

            st.write(
                reference["authors"]
            )

            st.write(
                reference["title"]
            )

            if reference["volume"]:

                st.write(

                    f"{reference['journal']}, "

                    f"{reference['volume']}, "

                    f"{reference['pages']} "

                    f"({reference['year']})"

                )

            else:

                st.write(

                    f"{reference['journal']} "

                    f"({reference['year']})"

                )

            if reference["doi"]:

                st.code(
                    reference["doi"]
                )
                # ==========================================================
# ABOUT
# ==========================================================

elif page == "ℹ️ About":

    st.title("ℹ️ About")

    st.markdown("""

# Quantum Descriptor Toolkit (QDT)

The **Quantum Descriptor Toolkit (QDT)** is an open-source
Python application developed for calculating
Conceptual Density Functional Theory (CDFT)
descriptors directly from HOMO and LUMO energies.

The toolkit is intended for researchers working in

- Computational Chemistry
- Organic Electronics
- Materials Science
- Medicinal Chemistry
- Molecular Electronics
- Catalysis
- Machine Learning for Chemistry

---

## Current Features

✅ HOMO/LUMO Calculator

✅ Hartree ↔ eV Conversion

✅ 14 Conceptual DFT Descriptors

✅ Scientific Interpretation

✅ Descriptor Encyclopedia

✅ Batch Calculator

✅ Publication Figure Studio

✅ CSV Export

✅ Interactive Tables

---

## Figure Studio

The Publication Figure Studio allows users to create
publication-quality figures with

- Multiple journal fonts
- Adjustable figure size
- Editable Plotly figures
- Scatter plots
- Histograms
- Bar plots
- Box plots
- PNG export
- HTML export

---

## Developed By

**Sania Ismaeel**

PhD (Computational Chemistry)

---

## Built With

- Python
- Streamlit
- Pandas
- Plotly

---

## License

MIT License

---

## Version

Version **2.0**

""")

# ==========================================================
# FOOTER
# ==========================================================

st.divider()

c1, c2, c3 = st.columns(3)

with c1:

    st.caption("Quantum Descriptor Toolkit")

with c2:

    st.caption("Version 2.0")

with c3:

    st.caption("© 2026 Sania Ismaeel")