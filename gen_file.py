import csv
import os
import hashlib

def generate_csv_file(file_name, num_rows, data_size):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["email_hash", "category"])

        categories = ["Shirts", "\"Gingham\" Shorts", "Cardigans"]
        category_index = 0
        for i in range(num_rows):
            email = os.urandom(data_size)
            email_hash = hashlib.sha256(email).hexdigest()
            writer.writerow([email_hash, categories[category_index]])

            category_index = (category_index + 1) % len(categories)

if __name__ == '__main__':
    # Set the number of rows and the size of the data to generate
    num_rows = 50000000
    data_size = 20

    # Generate the CSV file
    generate_csv_file('2GB.csv', num_rows, data_size)