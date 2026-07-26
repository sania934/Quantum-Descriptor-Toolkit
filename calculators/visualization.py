"""
=========================================================
Quantum Descriptor Toolkit (QDT)

Visualization Module
Publication-quality Plotly Figures

Author: Sania Ismaeel
=========================================================
"""

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

# =========================================================
# AVAILABLE FONTS
# =========================================================

FONT_OPTIONS = [

    "Times New Roman",
    "Arial",
    "Calibri",
    "Cambria",
    "Helvetica",
    "Georgia"

]

# =========================================================
# JOURNAL PRESETS
# =========================================================

JOURNAL_PRESETS = {

    "Custom": {
        "font": "Times New Roman",
        "template": "simple_white"
    },

    "Elsevier": {
        "font": "Times New Roman",
        "template": "simple_white"
    },

    "Springer Nature": {
        "font": "Times New Roman",
        "template": "simple_white"
    },

    "ACS": {
        "font": "Arial",
        "template": "simple_white"
    },

    "RSC": {
        "font": "Arial",
        "template": "simple_white"
    },

    "Wiley": {
        "font": "Helvetica",
        "template": "simple_white"
    }

}

# =========================================================
# PLOTLY THEMES
# =========================================================

THEMES = {

    "Default": "plotly",

    "Simple White": "simple_white",

    "Presentation": "presentation",

    "ggplot2": "ggplot2",

    "Seaborn": "seaborn"

}

# =========================================================
# PUBLICATION LAYOUT
# =========================================================

def publication_layout(

    fig,

    font="Times New Roman",

    template="simple_white",

    width=900,

    height=600,

    font_size=18,

    title_size=22

):

    fig.update_layout(

        template=template,

        width=width,

        height=height,

        font=dict(

            family=font,

            size=font_size,

            color="black"

        ),

        title=dict(

            x=0.5,

            font=dict(

                family=font,

                size=title_size

            )

        ),

        plot_bgcolor="white",

        paper_bgcolor="white",

        legend=dict(

            borderwidth=1

        )

    )

    fig.update_xaxes(

        showline=True,

        linewidth=2,

        linecolor="black",

        mirror=True,

        ticks="outside",

        showgrid=False

    )

    fig.update_yaxes(

        showline=True,

        linewidth=2,

        linecolor="black",

        mirror=True,

        ticks="outside",

        showgrid=False

    )

    return fig

# =========================================================
# EXPORT FIGURE
# =========================================================

def export_figure(

    fig,

    filename="publication_figure",

    width=1800,

    height=1200,

    scale=2

):

    fig.write_image(

        f"{filename}.png",

        width=width,

        height=height,

        scale=scale

    )

    fig.write_image(

        f"{filename}.svg"

    )

    fig.write_image(

        f"{filename}.pdf"

    )
    # =========================================================
# SCATTER PLOT
# =========================================================

def scatter_plot(

    dataframe,

    x,

    y,

    title="Scatter Plot",

    font="Times New Roman",

    template="simple_white",

    width=900,

    height=600,

    marker_size=10

):

    fig = px.scatter(

        dataframe,

        x=x,

        y=y,

        title=title

    )

    fig.update_traces(

        marker=dict(

            size=marker_size,

            line=dict(

                color="black",

                width=1

            )

        )

    )

    fig = publication_layout(

        fig,

        font=font,

        template=template,

        width=width,

        height=height

    )

    return fig


# =========================================================
# HISTOGRAM
# =========================================================

def histogram(

    dataframe,

    column,

    title="Histogram",

    bins=20,

    font="Times New Roman",

    template="simple_white",

    width=900,

    height=600

):

    fig = px.histogram(

        dataframe,

        x=column,

        nbins=bins,

        title=title

    )

    fig = publication_layout(

        fig,

        font=font,

        template=template,

        width=width,

        height=height

    )

    return fig


# =========================================================
# BAR PLOT
# =========================================================

def bar_plot(

    dataframe,

    x,

    y,

    title="Bar Plot",

    font="Times New Roman",

    template="simple_white",

    width=900,

    height=600

):

    fig = px.bar(

        dataframe,

        x=x,

        y=y,

        title=title

    )

    fig = publication_layout(

        fig,

        font=font,

        template=template,

        width=width,

        height=height

    )

    return fig


# =========================================================
# BOX PLOT
# =========================================================

def box_plot(

    dataframe,

    y,

    title="Box Plot",

    font="Times New Roman",

    template="simple_white",

    width=900,

    height=600

):

    fig = px.box(

        dataframe,

        y=y,

        title=title,

        points="outliers"

    )

    fig = publication_layout(

        fig,

        font=font,

        template=template,

        width=width,

        height=height

    )

    return fig
# =========================================================
# LINE PLOT
# =========================================================

def line_plot(

    dataframe,

    x,

    y,

    title="Line Plot",

    font="Times New Roman",

    template="simple_white",

    width=900,

    height=600

):

    fig = px.line(

        dataframe,

        x=x,

        y=y,

        title=title,

        markers=True

    )

    fig = publication_layout(

        fig,

        font=font,

        template=template,

        width=width,

        height=height

    )

    return fig


# =========================================================
# VIOLIN PLOT
# =========================================================

def violin_plot(

    dataframe,

    y,

    title="Violin Plot",

    font="Times New Roman",

    template="simple_white",

    width=900,

    height=600

):

    fig = px.violin(

        dataframe,

        y=y,

        box=True,

        points="all",

        title=title

    )

    fig = publication_layout(

        fig,

        font=font,

        template=template,

        width=width,

        height=height

    )

    return fig


# =========================================================
# BUBBLE PLOT
# =========================================================

def bubble_plot(

    dataframe,

    x,

    y,

    size,

    color,

    title="Bubble Plot",

    font="Times New Roman",

    template="simple_white",

    width=900,

    height=600

):

    fig = px.scatter(

        dataframe,

        x=x,

        y=y,

        size=size,

        color=color,

        title=title

    )

    fig = publication_layout(

        fig,

        font=font,

        template=template,

        width=width,

        height=height

    )

    return fig


# =========================================================
# CORRELATION HEATMAP
# =========================================================

def correlation_heatmap(

    dataframe,

    font="Times New Roman",

    template="simple_white",

    width=900,

    height=700

):

    correlation = dataframe.corr(numeric_only=True)

    fig = px.imshow(

        correlation,

        text_auto=".2f",

        color_continuous_scale="RdBu_r",

        aspect="auto",

        title="Correlation Matrix"

    )

    fig = publication_layout(

        fig,

        font=font,

        template=template,

        width=width,

        height=height

    )

    return fig