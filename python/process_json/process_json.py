import json

def read_csv(json_path):
    file_obj = open (json_path, "r")
    data = json.loads(file_obj.read())
    return data

def reformat_csv(data):
    for entry in data:
        entry['Name'] = entry.get("first_name", "") + " " + entry.get("last_name", "")
        entry.pop('first_name', None)
        entry.pop('last_name', None)
    return data

def write_csv(data):
    with open('python/process_json/output.json', 'w') as file_obj:
        json.dump(data, file_obj)
    file_obj.close()

def main():
    json_path = "python/process_json/input.json"
    input = read_csv(json_path)
    output = reformat_csv(input)
    write_csv(output)
    print(output)

if __name__ == "__main__":
    main()