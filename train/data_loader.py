import json

# TODO: Rewrite as pytorch DataLoader
def data_loader(source):
    with open(source, 'r') as f:
        data = json.load(f)
        print(data)

if __name__ == '__main__':
    source = 'data/dataset/processed.json'
    data_loader(source)