import csv
import itertools

# Define column names
columns = ["c_H_1_1", "c_H_1_2", "c_H_2_1", "c_H_2_2",
           "c_G_1_1", "c_G_1_2", "c_G_2_1", "c_G_2_2", "c_F"]

# Output CSV file
output_file = "combinations.csv"

# Open file and stream write
with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(columns)  # write header
    
    # Generate combinations and write row by row
    for combo in itertools.product(range(1, 3), repeat=len(columns)):
        writer.writerow(combo)

print(f"Finished writing all combinations to {output_file}")
