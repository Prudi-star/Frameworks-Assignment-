import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load dataset
df = pd.read_csv("data/metadata.csv")

# Step 2: Clean dataset
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
df["year"] = df["publish_time"].dt.year

# Step 3: Title and description
st.title("CORD-19 Data Explorer")
st.write("A simple app to explore COVID-19 research papers")

# Step 4: Year filter
year_range = st.slider("Select year range", 2015, 2022, (2019, 2021))
filtered = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

# Step 5: Show data sample
st.write("Here are some rows from the dataset:")
st.write(filtered[["title", "authors", "journal", "year"]].head(10))

# Step 6: Publications per Year
st.write("### Publications by Year")
year_counts = filtered["year"].value_counts().sort_index()

fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_title("Publications by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Count")
st.pyplot(fig)

# Step 7: Top Journals
st.write("### Top Journals")
top_journals = filtered["journal"].value_counts().head(10)
st.bar_chart(top_journals)
