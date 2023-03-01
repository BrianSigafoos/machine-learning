from pathlib import Path
from urllib.request import urlretrieve

TINY_SHAKESPEARE_URL = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
path_data = Path("data")
path_data.mkdir(exist_ok=True)
path_file = path_data / "tinyshakespeare.txt"

if not path_file.exists():
    urlretrieve(TINY_SHAKESPEARE_URL, path_file)

print("Data file now available at", path_file)
print("First 100 characters: \n")
print(path_file.read_text()[:100])
