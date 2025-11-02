import requests


class DataLoader:
    def __init__(self, datasetName: str):
        self.datasetName = datasetName
        self.available = {
            "the-verdict": "https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/refs/heads/main/ch02/01_main-chapter-code/the-verdict.txt"
        }

    def load(self):
        if self.datasetName not in self.available:
            print("Dataset not available.")
            return None

        try:
            with open(f".data/{self.datasetName}", "r") as file:
                raw = file.read()
                return raw
        except (FileExistsError, FileNotFoundError):
            print("Error loading dataset, not found! trying to download...")

        # download from url into `.data`

        url = self.available[self.datasetName]
        response = requests.get(url)
        if response.status_code == 200:
            raw = response.text
            with open(f".data/{self.datasetName}", "w") as file:
                file.write(raw)
            return raw
        else:
            print("Error downloading dataset: ", response.status_code)
            return None
