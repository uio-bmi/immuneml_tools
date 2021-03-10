




def get_labels(path):
    print(path)
    with open(path, 'r') as metadataFile:
        labels = metadataFile.readline()
        if labels:
            labels = labels.split(",")

    return [(label, label, False) for label in labels]