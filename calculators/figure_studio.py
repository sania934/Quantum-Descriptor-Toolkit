"""
=========================================================
Quantum Descriptor Toolkit (QDT)

Publication Figure Studio

Author: Sania Ismaeel
=========================================================
"""

import streamlit as st
import pandas as pd

from calculators.visualization import (

    scatter_plot,

    histogram,

    bar_plot,

    box_plot,

    line_plot,

    violin_plot,

    bubble_plot,

    correlation_heatmap,

    FONT_OPTIONS,

    THEMES,

    JOURNAL_PRESETS,

    export_figure

)


# ==========================================================
# PUBLICATION FIGURE STUDIO
# ==========================================================

def publication_figure_studio(dataframe):

    """
    Interactive publication-quality figure generator.
    """

    st.title("📊 Publication Figure Studio")

    st.write(
        """
Create publication-quality figures from calculated
Conceptual DFT descriptors.
"""
    )

    st.divider()

    # ======================================================
    # CHECK DATA
    # ======================================================

    if dataframe is None:

        st.warning(
            "No dataset available."
        )

        return

    if dataframe.empty:

        st.warning(
            "Dataset is empty."
        )

        return

    numeric_columns = dataframe.select_dtypes(
        include="number"
    ).columns.tolist()

    if len(numeric_columns) == 0:

        st.error(
            "No numeric columns were found."
        )

        return

    # ======================================================
    # SIDEBAR SETTINGS
    # ======================================================

    st.sidebar.header("Figure Settings")

    graph_type = st.sidebar.selectbox(

        "Graph Type",

        [

            "Scatter Plot",

            "Histogram",

            "Bar Plot",

            "Box Plot",

            "Line Plot",

            "Violin Plot",

            "Bubble Plot",

            "Correlation Heatmap"

        ]

    )

    journal = st.sidebar.selectbox(

        "Journal Style",

        list(JOURNAL_PRESETS.keys())

    )

    default_font = JOURNAL_PRESETS[journal]["font"]

    default_template = JOURNAL_PRESETS[journal]["template"]

    font = st.sidebar.selectbox(

        "Font",

        FONT_OPTIONS,

        index=FONT_OPTIONS.index(default_font)

    )

    theme = st.sidebar.selectbox(

        "Theme",

        list(THEMES.keys()),

        index=1

    )

    template = THEMES[theme]
        # ======================================================
    # FIGURE SETTINGS
    # ======================================================

    width = st.sidebar.slider(

        "Figure Width",

        min_value=500,

        max_value=2000,

        value=900,

        step=50

    )

    height = st.sidebar.slider(

        "Figure Height",

        min_value=400,

        max_value=1500,

        value=600,

        step=50

    )

    font_size = st.sidebar.slider(

        "Font Size",

        min_value=10,

        max_value=30,

        value=18

    )

    marker_size = st.sidebar.slider(

        "Marker Size",

        min_value=4,

        max_value=20,

        value=10

    )

    export_scale = st.sidebar.selectbox(

        "Export Quality",

        [

            "Standard",

            "High",

            "Very High"

        ],

        index=1

    )

    if export_scale == "Standard":

        scale = 1

    elif export_scale == "High":

        scale = 2

    else:

        scale = 4

    st.divider()

    # ======================================================
    # FIGURE TITLE
    # ======================================================

    title = st.text_input(

        "Figure Title",

        value=graph_type

    )

    # ======================================================
    # AXIS SELECTION
    # ======================================================

    if graph_type != "Correlation Heatmap":

        col1, col2 = st.columns(2)

        with col1:

            x = st.selectbox(

                "X-axis",

                dataframe.columns.tolist()

            )

        with col2:

            if graph_type in [

                "Histogram",

                "Box Plot",

                "Violin Plot"

            ]:

                y = None

                st.info(
                    "Only one variable is required."
                )

            else:

                y = st.selectbox(

                    "Y-axis",

                    numeric_columns,

                    index=1 if len(numeric_columns) > 1 else 0

                )

    # ======================================================
    # BUBBLE SETTINGS
    # ======================================================

    if graph_type == "Bubble Plot":

        bubble_size = st.selectbox(

            "Bubble Size",

            numeric_columns

        )

        bubble_color = st.selectbox(

            "Bubble Color",

            dataframe.columns.tolist()

        )

    st.divider()

    generate = st.button(

        "📈 Generate Figure",

        use_container_width=True

    )
        # ======================================================
    # GENERATE FIGURE
    # ======================================================

    if generate:

        fig = None

        # ---------------------------------------------
        # Scatter Plot
        # ---------------------------------------------

        if graph_type == "Scatter Plot":

            fig = scatter_plot(

                dataframe=dataframe,

                x=x,

                y=y,

                title=title,

                font=font,

                template=template,

                width=width,

                height=height,

                marker_size=marker_size

            )

        # ---------------------------------------------
        # Histogram
        # ---------------------------------------------

        elif graph_type == "Histogram":

            fig = histogram(

                dataframe=dataframe,

                column=x,

                title=title,

                font=font,

                template=template,

                width=width,

                height=height

            )

        # ---------------------------------------------
        # Bar Plot
        # ---------------------------------------------

        elif graph_type == "Bar Plot":

            fig = bar_plot(

                dataframe=dataframe,

                x=x,

                y=y,

                title=title,

                font=font,

                template=template,

                width=width,

                height=height

            )

        # ---------------------------------------------
        # Box Plot
        # ---------------------------------------------

        elif graph_type == "Box Plot":

            fig = box_plot(

                dataframe=dataframe,

                y=x,

                title=title,

                font=font,

                template=template,

                width=width,

                height=height

            )

        # ---------------------------------------------
        # Line Plot
        # ---------------------------------------------

        elif graph_type == "Line Plot":

            fig = line_plot(

                dataframe=dataframe,

                x=x,

                y=y,

                title=title,

                font=font,

                template=template,

                width=width,

                height=height

            )

        # ---------------------------------------------
        # Violin Plot
        # ---------------------------------------------

        elif graph_type == "Violin Plot":

            fig = violin_plot(

                dataframe=dataframe,

                y=x,

                title=title,

                font=font,

                template=template,

                width=width,

                height=height

            )

        # ---------------------------------------------
        # Bubble Plot
        # ---------------------------------------------

        elif graph_type == "Bubble Plot":

            fig = bubble_plot(

                dataframe=dataframe,

                x=x,

                y=y,

                size=bubble_size,

                color=bubble_color,

                title=title,

                font=font,

                template=template,

                width=width,

                height=height

            )

        # ---------------------------------------------
        # Correlation Heatmap
        # ---------------------------------------------

        elif graph_type == "Correlation Heatmap":

            fig = correlation_heatmap(

                dataframe=dataframe,

                font=font,

                template=template,

                width=width,

                height=height

            )

        # ======================================================
        # DISPLAY FIGURE
        # ======================================================

        if fig is not None:

            st.success("Figure generated successfully!")

            st.plotly_chart(

                fig,

                use_container_width=True
            )
                        # ======================================================
            # DOWNLOAD OPTIONS
            # ======================================================

            st.divider()

            st.subheader("📥 Export Figure")

            transparent = st.checkbox(
                "Transparent Background",
                value=False
            )

            if transparent:

                fig.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)"
                )

            file_name = st.text_input(
                "Filename",
                value="publication_figure"
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                if st.button("Save PNG"):

                    fig.write_image(
                        f"{file_name}.png",
                        scale=scale
                    )

                    st.success("PNG saved successfully.")

            with col2:

                if st.button("Save SVG"):

                    fig.write_image(
                        f"{file_name}.svg"
                    )

                    st.success("SVG saved successfully.")

            with col3:

                if st.button("Save PDF"):

                    fig.write_image(
                        f"{file_name}.pdf"
                    )

                    st.success("PDF saved successfully.")

            st.divider()

            st.subheader("Figure Information")

            st.write(f"**Journal Style:** {journal}")

            st.write(f"**Font:** {font}")

            st.write(f"**Theme:** {theme}")

            st.write(f"**Dimensions:** {width} × {height}")

            st.write(f"**Export Quality Scale:** {scale}")