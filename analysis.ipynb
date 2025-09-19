# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Load the dataset
df = pd.read_csv("data/metadata.csv")

# Step 3: Explore the dataset
print("Shape of dataset:", df.shape)   # rows and columns
print(df.info())                       # column info
print(df.head())                       # first 5 rows

# Step 4: Clean data
# Convert publish_time to datetime
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")

# Create a new column called "year"
df["year"] = df["publish_time"].dt.year

# Remove rows where year is missing
df = df.dropna(subset=["year"])

# Step 5: Visualization 1 - Publications per year
year_counts = df["year"].value_counts().sort_index()
plt.bar(year_counts.index, year_counts.values)
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of Publications")
plt.show()

# Step 6: Visualization 2 - Top 10 Journals
top_journals = df["journal"].value_counts().head(10)
top_journals.plot(kind="barh")
plt.title("Top 10 Journals")
plt.xlabel("Number of Publications")
plt.ylabel("Journal")
plt.show()
