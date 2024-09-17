#!/usr/bin/env python3

import os
import pandas as pd

def convert_txt_to_csv(file_name, input_dir, output_dir, chunk_size=1000000):
    """
    Converts a pipe-delimited text file to a CSV file in chunks to manage memory usage, skipping malformed lines.
    Automatically infers the column headers from the input file.

    Parameters:
    file_name (str): The name of the text file to convert.
    input_dir (str): The directory where the input text file is located.
    output_dir (str): The directory where the output CSV file will be saved.
    chunk_size (int): The number of rows to process at a time.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Construct the full path to the input file
    input_file = os.path.join(input_dir, file_name)

    # Check if the file exists and ends with .txt
    if os.path.exists(input_file) and file_name.endswith('.txt'):
        try:
            # Construct the output file path
            output_file = os.path.join(output_dir, file_name.replace('.txt', '.csv'))
            
            # Open output CSV file in write mode
            with open(output_file, 'w') as f_out:
                # Process the file in chunks and let pandas infer the header
                for chunk in pd.read_csv(input_file, delimiter='|', chunksize=chunk_size, on_bad_lines='skip'):
                    # Write each chunk to the CSV file, keeping the header only for the first chunk
                    chunk.to_csv(f_out, header=f_out.tell()==0, index=False)

        except Exception as e:
            raise e
    else:
        raise FileNotFoundError(f"File {file_name} does not exist in the input directory or is not a .txt file.")
        
# Main execution if run as a script
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python3 convert_txt_to_csv.py <file_name> <input_dir> <output_dir>")
    else:
        file_name = sys.argv[1]
        input_dir = sys.argv[2]
        output_dir = sys.argv[3]
        convert_txt_to_csv(file_name, input_dir, output_dir)
