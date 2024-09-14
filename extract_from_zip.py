import subprocess
import os

def extract_all_zips(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):   ### loop through files in input directory
        if filename.endswith(".zip"):   ### check filename that ends with .zip
            zip_path = os.path.join(input_dir, filename)  
            extract_subdir = os.path.join(output_dir, os.path.splitext(filename)[0]) ##subdirectory for each file in output directory
            if not os.path.exists(extract_subdir):
                os.makedirs(extract_subdir)
            try:
                subprocess.run(['unzip', zip_path, '-d', extract_subdir], check=True)
                print(f"Extracted {filename} to {extract_subdir}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to extract {filename}: {e}")


if __name__ == "__main__":
    # Define input and output directories
    input_directory = '/input_dir'
    output_directory = '/output_dir'

    # Call the function to extract all zip files in the input directory
    extract_all_zips(input_directory, output_directory)
