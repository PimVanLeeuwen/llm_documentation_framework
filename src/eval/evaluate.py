"""
File that handles the evaluation of all of the files in doc

Author:
	Pim van Leeuwen (1303422, p.p.h.v.leeuwen@student.tue.nl)
"""

import os
import evaluate

def find_reference_file(file_name: str, folder: str, parent_name : str = ""):
    """Find the reference file for a given name.

    Args:
        parent_name (string): name of the parent (class in case of method) otherwise none.
        file_name (string): name of the method/class.
        folder (string): folder to search.

    Returns:
        string: path of the file.
    """

    for root, dirs, files in os.walk("reference/" + folder):
        for file in files:
            if parent_name != "" and parent_name + "_" + file_name + ".md" == file:
                return os.path.join(root, file)
            elif parent_name == "" and file == file_name + ".md":
                return os.path.join(root, file)

    return ""


def evaluate_documentation():
    """This will serve as a method to evaluate all the files in /docs if there are reference documentations in /reference.

    """
    # Get the first folder after "docs"
    first_folder = next(os.walk("docs"))[1]

    if first_folder and first_folder[0] == "JUCE":
        juce_processing = True
    else:
        juce_processing = False

    # Load the BLEU and ROUGE metrics
    bleu_metric = evaluate.load("bleu")
    rouge_metric = evaluate.load("rouge")

    nr_files = 0
    bleu_scores = []
    rouge_1_scores = []
    rouge_l_scores = []

    for root, dirs, files in os.walk("docs"):
        for file in files:
            print(nr_files)
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                candidate = f.read()

            if len(root.split("/")) == 1: continue

            file_name = file.split(".")[0]
            parent_name = ""

            if juce_processing:
                parent_name = root.split("/")[-1].split('_')[1:] if root.split("/")[-1] != "juce" else root.split("/")[-2].split('_')[1:]
                if len(parent_name) >= 1: parent_name = parent_name[0]
                else: parent_name = ""
                if parent_name.endswith(".cpp"): parent_name = parent_name[:-4]
            else:
                parent_name = root.split("/")[-2] if not root.split("/")[-2].endswith(".java") and not root.split("/")[-1].endswith(".java") else ""
                if parent_name == "":
                    parent_name = root.split("/")[-1] if not root.split("/")[-1].endswith(".java") else ""

            reference_file = find_reference_file(file_name=file_name, folder="juce" if juce_processing else "java_util", parent_name=parent_name)
            if reference_file != "":
                nr_files += 1
                with open(reference_file, 'r') as f:
                    reference = f.read()

                bleu_results = bleu_metric.compute(predictions=[candidate], references=[reference])
                bleu_scores.append(bleu_results['bleu']*100)

                # ROUGE expects plain text inputs
                rouge_results = rouge_metric.compute(predictions=[candidate], references=[reference])
                rouge_1_scores.append(rouge_results['rouge1'])
                rouge_l_scores.append(rouge_results['rougeL'])
                # Access ROUGE scores (no need for indexing into the result)


                # print(f'Matched {file} to {reference_file} (parent_name = {parent_name} | file_name = {file_name})')

    print(f"Evaluated {nr_files} files")
    print(f"BLEU Score: {sum(bleu_scores)/len(bleu_scores):.2f}")
    print(f"ROUGE-1 F1 Score: {sum(rouge_1_scores)/len(rouge_1_scores):.2f}")
    print(f"ROUGE-L F1 Score: {sum(rouge_l_scores)/len(rouge_l_scores):.2f}")
