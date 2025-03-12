import pandas as pd
import os

def load_data(file_path):
    """Load data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(data):
    """Clean the data by handling missing values and removing duplicates."""
    if data is not None:
        # Fill missing values with the mean for numeric columns
        numeric_columns = data.select_dtypes(include=['number']).columns
        data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())

        # Fill missing values in categorical columns with 'Unknown'
        categorical_columns = data.select_dtypes(include=['object']).columns
        data[categorical_columns] = data[categorical_columns].fillna('Unknown')

        # Remove duplicate rows
        data = data.drop_duplicates()
        print("Data cleaned successfully.")
    return data

def transform_data(data):
    """Transform the data by creating new columns or aggregating data."""
    if data is not None:
        # Example: Create a new column 'Total' as the sum of numeric columns
        numeric_columns = data.select_dtypes(include=['number']).columns
        data['Total'] = data[numeric_columns].sum(axis=1)

        # Example: Group data by a categorical column and calculate the mean
        if 'Category' in data.columns:
            grouped_data = data.groupby('Category').mean(numeric_only=True)
            print("Data transformed and aggregated successfully.")
            return data, grouped_data
    return data, None

def save_data(data, output_path):
    """Save the processed data to a CSV file."""
    if data is not None:
        try:
            data.to_csv(output_path, index=False)
            print(f"Processed data saved to {output_path}")
        except Exception as e:
            print(f"Error saving data: {e}")

def automate_data_processing(input_file, output_file):
    """Automate the entire data processing workflow."""
    # Step 1: Load the data
    data = load_data(input_file)

    # Step 2: Clean the data
    data = clean_data(data)

    # Step 3: Transform the data
    data, grouped_data = transform_data(data)

    # Step 4: Save the processed data
    save_data(data, output_file)

    # Optionally, save the aggregated data
    if grouped_data is not None:
        aggregated_output_file = os.path.splitext(output_file)[0] + "_aggregated.csv"
        save_data(grouped_data, aggregated_output_file)

if __name__ == "__main__":
    # Specify input and output file paths
    input_file = "C:"  # Replace with your input file path
    output_file = "C:"  # Replace with your output file path

    # Run the data automation tool
    automate_data_processing(input_file, output_file)
