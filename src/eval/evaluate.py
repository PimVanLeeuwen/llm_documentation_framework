"""
File that handles the evaluation of all of the files in doc

Author:
	Pim van Leeuwen (1303422, p.p.h.v.leeuwen@student.tue.nl)
"""

import os
import warnings

from tqdm import tqdm

def find_reference_file(name: str):
    """Find the reference file for a given name.

    Args:
        name (string): name of the reference file to find.

    Returns:
        string: path of the file.
    """

    output_files = []

    for root, dirs, files in os.walk("reference/juce"):
        for file in files:
            if file.split(".")[0] == name and len(file.split(".")) == 2:
                output_files.append(os.path.join(root, file))

    return output_files


def evaluate_documentation():
    """This will serve as a method to evaluate all the files in /docs if there are reference documentations in /reference.

    """

    nr_files = 0

    # Small check for the status bar, adds negligible time
    for root, dirs, files in os.walk("docs"):
        for file in files:

            # print("class" + "_".join(root.split("/")[-1].split('_')[1:]).split(".")[0] + "_" + file.split(".")[0])
            reference_files = find_reference_file(file.split(".")[0]) + find_reference_file(root.split("/")[-1] + "_" + file.split(".")[0]) +       	find_reference_file("class" + "_".join(root.split("/")[-1].split('_')[1:]).split(".")[0] + "_" + file.split(".")[0])
            if len(reference_files) == 1:
                nr_files += 1
                print(f'Matched {file} to {reference_files[0]}')

    print(f"Found {nr_files} files to evaluate")
