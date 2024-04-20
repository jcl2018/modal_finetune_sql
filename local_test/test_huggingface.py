

###  load dataset (in load_data_sql) ###
from datasets import load_dataset
import os
import json
print("Begin loading dataset...")

dataset = load_dataset("b-mc2/sql-create-context")
print("Dataset loaded!")
print(dataset)

# Create a local directory to store data into files.
dataset_splits = {"train": dataset["train"]}
out_path = os.path.join(os.getcwd(), "local_dataset")
os.makedirs(out_path, exist_ok=True)
for key, ds in enumerate(dataset_splits.items()):
    with open(out_path, "w") as f:
        for item in ds:
            newitem = {
                "input": item["question"],
                "context": item["context"],
                "output": item["answer"],
            }
            f.write(json.dumps(newitem) + "\n")