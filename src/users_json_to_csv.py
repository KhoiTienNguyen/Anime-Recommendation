import csv
import json
import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', required=True)
    parser.add_argument('-i', '--input', required=True)
    args = parser.parse_args()

    all_users = open(args.input, encoding='utf-8')
    user_data = json.load(all_users)

    fieldnames = ["user", "ID", "score"]

    with open(args.output, mode='w', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for i in user_data:
            for n in user_data[i]:
                template = {}
                template["user"] = i
                template["ID"] = n
                template["score"] = user_data[i][n]
                writer.writerow(template)

if __name__ == '__main__':
    main()