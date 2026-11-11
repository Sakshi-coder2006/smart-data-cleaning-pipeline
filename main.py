
import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv("dataset/messy_data.csv")

print("========== ORIGINAL DATASET ==========")
print(df)

# Step 2: Detect missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Step 3: Handle missing values
df["Course"] = df["Course"].fillna("Unknown")
df["Marks"] = df["Marks"].fillna(0)

print("\n========== AFTER HANDLING MISSING VALUES ==========")
print(df)

# Step 4: Remove duplicate records
df = df.drop_duplicates()

print("\n========== AFTER REMOVING DUPLICATES ==========")
print(df)

# Step 5: Text normalization
df["Course"] = df["Course"].str.strip().str.upper()

print("\n========== AFTER TEXT NORMALIZATION ==========")
print(df)

# Step 6: Save the cleaned dataset
df.to_csv("output/cleaned_data.csv", index=False)

print("\nCleaned dataset saved successfully!")
print("File location: output/cleaned_data.csv")
