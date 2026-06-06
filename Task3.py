from urllib.request import urlopen

url = "https://raw.githubusercontent.com/spyguessgame-boop/own_dataset/refs/heads/main/data.txt"


text_data = urlopen(url).read().decode("utf-8")[:1000]

tokens = text_data.split()
print(tokens)
print("number of tokens: ", len(tokens))
