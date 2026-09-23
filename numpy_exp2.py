import numpy as np

# ============================================
# NumPy Array Operations
# ============================================

# Create a 2D array
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Original Array:")
print(arr)


# ============================================
# 1. Arithmetic Operations
# ============================================

print("\n--- Arithmetic Operations ---")

# Addition
print("Addition (+ 10):")
print(arr + 10)

# Subtraction
print("Subtraction (- 10):")
print(arr - 10)

# Multiplication
print("Multiplication (* 2):")
print(arr * 2)

# Division
print("Division (/ 2):")
print(arr / 2)

# Power
print("Power (** 2):")
print(arr ** 2)


# ============================================
# 2. Aggregation Functions
# ============================================

print("\n--- Aggregation Functions ---")

# Sum
print("Sum:", np.sum(arr))

# Mean
print("Mean:", np.mean(arr))

# Median
print("Median:", np.median(arr))

# Minimum
print("Minimum:", np.min(arr))

# Maximum
print("Maximum:", np.max(arr))


# ============================================
# 3. Standard Deviation
# ============================================

print("\n--- Standard Deviation ---")

std = np.std(arr)

print("Standard Deviation:", std)


# ============================================
# 4. Axis-Based Operations
# ============================================

print("\n--- Axis-Based Operations ---")

# axis=0 → calculate column-wise
print("Column-wise Sum (axis=0):")
print(np.sum(arr, axis=0))

print("Column-wise Mean (axis=0):")
print(np.mean(arr, axis=0))

# axis=1 → calculate row-wise
print("Row-wise Sum (axis=1):")
print(np.sum(arr, axis=1))

print("Row-wise Mean (axis=1):")
print(np.mean(arr, axis=1))


# ============================================
# 5. More Axis-Based Aggregations
# ============================================

print("\n--- More Axis-Based Operations ---")

print("Column-wise Maximum:")
print(np.max(arr, axis=0))

print("Row-wise Maximum:")
print(np.max(arr, axis=1))

print("Column-wise Minimum:")
print(np.min(arr, axis=0))

print("Row-wise Minimum:")
print(np.min(arr, axis=1))

print("Column-wise Standard Deviation:")
print(np.std(arr, axis=0))

print("Row-wise Standard Deviation:")
print(np.std(arr, axis=1))