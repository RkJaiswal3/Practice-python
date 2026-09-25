import pandas as pd
import numpy as np

# ============================================================
# 1. CREATE A REALISTIC CUSTOMER DATASET
# ============================================================

data = {
    "customer_id": [101, 102, 103, 104, 105, 106, 107, 108, 108, 110],
    "name": [
        "Rohit", "Sita", "Amit", "Priya", "Ram",
        "Anita", "Bikash", "Nisha", "Nisha", "Kiran"
    ],
    "age": [24, 29, np.nan, 35, 42, 27, 31, np.nan, np.nan, 38],
    "city": [
        "Kathmandu", "Pokhara", "Lalitpur", "Kathmandu",
        "Pokhara", "Bhaktapur", None, "Kathmandu",
        "Kathmandu", "Lalitpur"
    ],
    "salary": [
        35000, 45000, 52000, np.nan, 70000,
        40000, 55000, 48000, 48000, np.nan
    ],
    "purchase_amount": [
        5000, 7500, 3000, 9000, np.nan,
        4500, 8000, 6500, 6500, 4000
    ],
    "status": [
        "Active", "Active", "Inactive", "Active", "Active",
        "Inactive", "Active", "Active", "Active", "Inactive"
    ]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)


# ============================================================
# 2. DATA EXPLORATION
# ============================================================

# -------------------------
# info()
# -------------------------

print("\n========== INFO ==========")

df.info()


# -------------------------
# describe()
# -------------------------

print("\n========== DESCRIBE ==========")

print(df.describe())


# -------------------------
# Check Missing Values
# -------------------------

print("\n========== MISSING VALUES ==========")

print(df.isnull().sum())


# Percentage of missing values
print("\nMissing Value Percentage:")

print(df.isnull().mean() * 100)


# -------------------------
# Check Duplicates
# -------------------------

print("\n========== DUPLICATES ==========")

print("Number of duplicate rows:")
print(df.duplicated().sum())

print("\nDuplicate rows:")
print(df[df.duplicated()])


# ============================================================
# 3. SELECTING COLUMNS
# ============================================================

print("\n========== SELECTING COLUMNS ==========")

# Select one column
print("\nCustomer Names:")
print(df["name"])


# Select multiple columns
print("\nName, City and Salary:")
print(df[["name", "city", "salary"]])


# ============================================================
# 4. FILTERING ROWS
# ============================================================

print("\n========== FILTERING ROWS ==========")

# Customers whose age is greater than 30
print("\nCustomers older than 30:")
print(df[df["age"] > 30])


# Customers with salary greater than 50000
print("\nCustomers with salary > 50000:")
print(df[df["salary"] > 50000])


# Customers from Kathmandu
print("\nCustomers from Kathmandu:")
print(df[df["city"] == "Kathmandu"])



# Multiple conditions
print("\nActive customers with salary > 40000:")

print(
    df[
        (df["status"] == "Active") &
        (df["salary"] > 40000)
    ]
)


# ============================================================
# 5. SORTING DATA
# ============================================================

print("\n========== SORTING ==========")

# Sort by salary ascending
print("\nSalary - Ascending:")

print(
    df.sort_values("salary")
)


# Sort by salary descending
print("\nSalary - Descending:")

print(
    df.sort_values("salary", ascending=False)
)


# Sort by multiple columns
print("\nSort by city and salary:")

print(
    df.sort_values(
        ["city", "salary"],
        ascending=[True, False]
    )
)


# ============================================================
# 6. DATA CLEANING
# ============================================================

print("\n========== DATA CLEANING ==========")

# Make a copy so original data remains unchanged
clean_df = df.copy()


# -------------------------
# Handle Missing Values
# -------------------------

print("\nMissing values before cleaning:")

print(clean_df.isnull().sum())


# -------------------------
# fillna()
# -------------------------

# Fill missing age with median age
clean_df["age"] = clean_df["age"].fillna(
    clean_df["age"].median()
)


# Fill missing salary with median salary
clean_df["salary"] = clean_df["salary"].fillna(
    clean_df["salary"].median()
)


# Fill missing purchase amount with median
clean_df["purchase_amount"] = clean_df["purchase_amount"].fillna(
    clean_df["purchase_amount"].median()
)


# Fill missing city with the most common city
clean_df["city"] = clean_df["city"].fillna(
    clean_df["city"].mode()[0]
)


print("\nMissing values after fillna():")

print(clean_df.isnull().sum())


# ============================================================
# 7. dropna()
# ============================================================

# Example dataset with missing values
dropna_example = df.copy()

print("\n========== DROPNA EXAMPLE ==========")

print("Rows before dropna:")

print(len(dropna_example))


# Remove rows containing any missing value
dropna_example = dropna_example.dropna()

print("\nRows after dropna:")

print(len(dropna_example))

print("\nCleaned dataset using dropna():")

print(dropna_example)


# ============================================================
# 8. REMOVE DUPLICATES
# ============================================================

print("\n========== REMOVE DUPLICATES ==========")

print("Duplicates before removal:")

print(clean_df.duplicated().sum())


# Remove duplicate rows
clean_df = clean_df.drop_duplicates()


print("\nDuplicates after removal:")

print(clean_df.duplicated().sum())


# ============================================================
# 9. CHANGING DATA TYPES
# ============================================================

print("\n========== DATA TYPES ==========")

print("Before changing data types:")

print(clean_df.dtypes)


# Convert customer_id to integer
clean_df["customer_id"] = clean_df["customer_id"].astype(int)

# Convert age to integer
clean_df["age"] = clean_df["age"].astype(int)

# Convert salary to float
clean_df["salary"] = clean_df["salary"].astype(float)

# Convert purchase amount to float
clean_df["purchase_amount"] = clean_df["purchase_amount"].astype(float)

# Convert status to string
clean_df["status"] = clean_df["status"].astype(str)


print("\nAfter changing data types:")

print(clean_df.dtypes)


# ============================================================
# 10. FINAL CLEAN DATASET
# ============================================================

print("\n========== FINAL CLEAN DATASET ==========")

print(clean_df)

print("\nFinal Shape:")

print(clean_df.shape)

print("\nFinal Missing Values:")

print(clean_df.isnull().sum())

print("\nFinal Duplicate Rows:")

print(clean_df.duplicated().sum())