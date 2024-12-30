import os
import re
from tokenizers import Tokenizer
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.trainers import BpeTrainer
from tokenizers.models import BPE


bpe_path = './data/bpe/LibriSpeech/books/utf-8'
texts = []


def normalize_text(text: str):
        text = text.lower()
        text = re.sub(r"[^a-z ]", "", text)
        return text


for root_path, dirs, _ in os.walk(bpe_path):
    for dir_i in dirs:
        for root2, _, files in os.walk(os.path.join(root_path, dir_i)):
            for file in files:
                file_path = os.path.join(root2, file)
                with open(file_path, 'r', encoding="utf-8") as f:
                    text = f.read().strip().lower()
                    texts.append(text)


tokenizer = Tokenizer(BPE())
tokenizer.pre_tokenizer = Whitespace()
trainer = BpeTrainer(special_tokens=[" "], vocab_size=200)
texts = [normalize_text(text) for text in texts]
tokenizer.train_from_iterator(texts, trainer)
tokenizer.save("./data/bpe_tokenizer.json")
