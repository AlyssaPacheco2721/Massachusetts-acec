# 🌿 Massachusetts Areas of Critical Environmental Concern (ACEC) Analysis

An exploratory environmental data analysis using **QGIS and Python** to examine the distribution, acreage, and designation history of Massachusetts Areas of Critical Environmental Concern (ACECs).

## Project Overview

This project analyzes the **MassGIS Areas of Critical Environmental Concern (ACEC) dataset** to explore spatial and quantitative patterns among protected environmental areas across Massachusetts.

Spatial data preparation and inspection were completed in **QGIS**, while **Python** was used for data cleaning, analysis, and visualization.

The project demonstrates how GIS and Python can be combined to investigate environmental conservation datasets through **spatial data preparation, quantitative analysis, and scientific visualization**.

---

## Research Questions

- How is ACEC acreage distributed across Massachusetts?
- How does designated acreage compare with GIS polygon acreage?
- How have ACEC designations changed over time?
- How can GIS and Python be combined to explore statewide conservation data?

---

## Tools & Skills

**QGIS • Python • pandas • matplotlib • seaborn • GIS • Spatial Data • Data Aggregation • Exploratory Data Analysis • Environmental Data Visualization**

- **QGIS** — spatial data preparation, projection verification, attribute inspection, and map development.
- **Python / pandas** — data loading, aggregation, date processing, and preparation of environmental data for analysis.
- **matplotlib / seaborn** — creation and formatting of bar, scatter, and time-series visualizations.
- **GIS analysis** — integration of spatial and quantitative approaches to examine Massachusetts conservation areas.
- **GitHub** — source code documentation and project version control.

---

## Data Source

**MassGIS — Areas of Critical Environmental Concern (ACEC), April 2009**

The dataset contains spatial and attribute information describing Massachusetts Areas of Critical Environmental Concern.

ACECs provide the geographic framework for examining protected environmental areas, acreage, and designation patterns across the state.

---

## Methodology

### 1. Spatial Data Preparation

The MassGIS ACEC dataset was imported into **QGIS** for spatial preparation and inspection.

- Reviewed spatial features and associated attributes.
- Verified spatial consistency and projection.
- Prepared the dataset for further analysis.

### 2. Data Cleaning & Inspection

Attribute data were examined and cleaned using **Python and pandas**.

The workflow included:

- Inspecting dataset structure and variables.
- Identifying and handling missing values.
- Preparing relevant fields for quantitative analysis.
- Checking data prior to visualization.

### 3. Exploratory Analysis

The cleaned data were analyzed to examine several characteristics of Massachusetts ACECs, including:

- Acreage by region.
- Differences between designated acreage and GIS polygon acreage.
- ACEC designation patterns over time.

### 4. Data Visualization

Visualizations were created programmatically in **Python using matplotlib and seaborn** to examine:

- Total ACEC acreage by region.
- Designated ACEC acreage compared with GIS polygon acreage.
- The number of ACEC designations over time.

The Python analysis and visualization workflow is available in [`acec_analysis.py`](acec_analysis.py).

---

## Results

### ACEC Acreage by Region

<img width="700" alt="ACEC acreage by region bar chart" src="https://github.com/user-attachments/assets/bc9e0041-5ff5-41a8-ada9-871e499cb873">

The bar chart compares ACEC acreage across geographic regions, providing a visual overview of how designated environmental areas are distributed across Massachusetts.

---

### Designated vs. GIS Polygon Acres

<img width="800" alt="Designated acreage versus GIS polygon acreage scatter plot" src="https://github.com/user-attachments/assets/40cff8bc-4777-4a6c-9c0a-d796e4527d76">

The scatter plot compares designated ACEC acreage with acreage represented by GIS polygons, allowing differences between the two measurements to be visually examined.

---

### ACEC Designations Over Time

<img width="800" alt="ACEC designations over time line chart" src="https://github.com/user-attachments/assets/f55604e9-39ed-4e64-be4a-d0f1e5232091">

The time-series visualization examines the historical pattern of ACEC designations represented in the dataset.

---

## GIS Visualization

🗺️ [View Exported ACEC Map](https://github.com/user-attachments/assets/bccf8704-1f15-4138-8c5e-47bae6da8357)

The GIS map provides spatial context for the quantitative analysis and illustrates the geographic distribution of Areas of Critical Environmental Concern across Massachusetts.

---

## Project Outputs

- 🐍 [`acec_analysis.py`](acec_analysis.py) — Python analysis and visualization script using pandas, matplotlib, and seaborn
- 📊 [ACEC Acreage Bar Chart](https://github.com/user-attachments/assets/8f3ea8b7-c90c-4084-9fc2-7d17b365825c)
- 📈 [Designated vs. GIS Polygon Acreage Scatter Plot](https://github.com/user-attachments/assets/40cff8bc-4777-4a6c-9c0a-d796e4527d76)
- 📉 [ACEC Designations Over Time](https://github.com/user-attachments/assets/f55604e9-39ed-4e64-be4a-d0f1e5232091)
- 🗺️ [Exported GIS Map](https://github.com/user-attachments/assets/bccf8704-1f15-4138-8c5e-47bae6da8357)
- 📁 [`Areas_CritENVConcern.csv`](Areas_CritENVConcern.csv) — ACEC dataset used in the Python analysis
- 📄 [Full Project Report](https://github.com/user-attachments/files/22048981/Areas.of.Critical.Environmental.Concern.pdf)

---

## Key Takeaways

This project demonstrates a workflow that combines **GIS and programmatic environmental data analysis**.

Rather than using GIS only for map creation, spatial information was prepared in QGIS and then analyzed quantitatively using Python. The resulting visualizations provide multiple ways to examine acreage, spatial representation, and designation history within the Massachusetts ACEC dataset.

---

## Future Development

Future versions of this project could extend the analysis through:

- Additional spatial analysis of ACEC distribution.
- Comparison with land use, habitat, or conservation-priority datasets.
- Statistical analysis of regional differences.
- Automated geospatial processing using Python.
- Development of an interactive GIS visualization or dashboard.

---

## Data & Citation

**Data Source:** MassGIS. *Areas of Critical Environmental Concern (ACEC), April 2009.*

**Project Citation**

Pacheco, A. *Massachusetts Areas of Critical Environmental Concern (ACEC) Analysis.*

---

## Author

**Alyssa Pacheco**

Environmental Scientist | Coastal & Marine Science | GIS & Environmental Data Analysis
