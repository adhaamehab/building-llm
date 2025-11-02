class DataLoader:
    def __init__(self, datasetName: str, local=False):
        self.datasetName = datasetName
        self.local = local
        self.available = {
            "the-verdict": "https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/refs/heads/main/ch02/01_main-chapter-code/the-verdict.txt"
        }

    def load(self):
        if self.local:
            try:
                with open(f".data/{self.datasetName}", "r") as file:
                    raw = file.read()
                    return raw
            except (FileExistsError, FileNotFoundError) as e:
                print("Error loading dataset ", e)
        else:
            # download from url into `.data`
            import requests

            if self.datasetName in self.available:
                url = self.available[self.datasetName]
                response = requests.get(url)
                if response.status_code == 200:
                    raw = response.text
                    return raw
                else:
                    print("Error downloading dataset: ", response.status_code)
            else:
                print("Dataset not available.")
