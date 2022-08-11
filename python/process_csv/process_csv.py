import pandas as pd
import pdb

def read_csv(file_path):
    data = pd.read_csv(file_path)
    return data

def reformat_csv(data):
    name = data['first_name'] + ' ' + data['last_name']
    data['name'] = name
    data = data.drop('first_name', axis=1)
    data = data.drop('last_name', axis=1)
    return data

def write_csv(data):
    data.to_csv("python/process_csv/output.csv", index=False)

def main():
    csv_path = "python/process_csv/input.csv"
    input = read_csv(csv_path)
    output = reformat_csv(input)
    write_csv(output)

if __name__ == "__main__":
    main()