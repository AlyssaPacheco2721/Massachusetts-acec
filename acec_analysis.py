"""
Massachusetts Areas of Critical Environmental Concern (ACEC) Analysis

Exploratory analysis and visualization of Massachusetts ACEC data using
pandas, matplotlib, and seaborn.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------
# Load data
# ---------------------------------------------------------

# Load CSV
df = pd.read_csv(r"Areas_CritENVConcern.csv")

# ---------------------------------------------------------
# ACEC acreage by region
# ---------------------------------------------------------

region_acres = df.groupby("REGION")["ACEC_ACRES"].sum().reset_index()

plt.figure(figsize=(10,6))
sns.barplot(data=region_acres, x="REGION", y="ACEC_ACRES", palette="viridis")

plt.title("ACEC Acreage by Region", fontsize=16, fontweight='bold')
plt.xlabel("Region", fontsize=12)
plt.ylabel("Total ACEC Acres", fontsize=12)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# Designated ACEC acres vs. GIS polygon acres
# ---------------------------------------------------------

plt.figure(figsize=(8,6))
sns.scatterplot(
    data=df,
    x="ACEC_ACRES",
    y="POLY_ACRES",
    hue="REGION",
    palette="tab10",
    s=70,
    edgecolor="black"
)
plt.title("Designated ACEC Acres vs GIS Polygon Acres")
plt.xlabel("Designated ACEC Acres")
plt.ylabel("GIS Polygon Acres")
plt.legend(title="Region", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# ACEC designations over time
# ---------------------------------------------------------

df["DES_DATE"] = pd.to_datetime(df["DES_DATE"], errors="coerce")
df["Year"] = df["DES_DATE"].dt.year

designations_per_year = df.groupby("Year").size().reset_index(name="Count")

plt.figure(figsize=(10,6))
sns.lineplot(data=designations_per_year, x="Year", y="Count", marker="o")
plt.title("ACEC Designations Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Designations")
plt.tight_layout()

plt.show()