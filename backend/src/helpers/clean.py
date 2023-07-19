from util import clean_space, clean_lemma, clean_lower
import spacy
import os

nlp = spacy.load("en_core_web_sm")

# Directory paths
input_directory = "../../docs"
output_directory = "../../docs/cleaned"


def process_file(file_path):
    # Read the contents of the file
    with open(file_path, "r") as file:
        text = file.read()

    doc = nlp(text)
    base_clean = clean_space(doc)

    # Return the processed content
    return {"base": base_clean}


# Get all text files in the input directory
text_files = [file for file in os.listdir(input_directory) if file.endswith(".txt")]

for file_name in text_files:
    input_file_path = os.path.join(input_directory, file_name)
    output_file_path = os.path.join(output_directory, file_name)
    output = output_file_path.split(".txt")[0]

    cleaned_formats = process_file(input_file_path)

    for key, value in cleaned_formats.items():
        with open(f"{output}-{key}.txt", "w") as file:
            file.write(value)
