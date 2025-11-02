import re


def createVocab(tokens):
    return {token: integer for integer, token in enumerate(sorted(set(tokens)))}


def preProcessText(text) -> list[str]:
    return [
        item.strip()
        for item in re.split(r'([,.:;?_!"()\']|--|\s)', text)
        if item.strip()
    ]


class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.str_to_id = vocab
        self.id_to_str = {id: s for s, id in vocab.items()}

    def encode(self, text: str) -> list[int]:
        return [self.str_to_id[token] for token in preProcessText(text)]

    def decode(self, token_ids: list[int]) -> str:
        text = " ".join([self.id_to_str[id] for id in token_ids])

        ## fix spacing before punctuation
        text = re.sub(r'\s+([,.?!"()\'])', r"\1", text)
        return text
