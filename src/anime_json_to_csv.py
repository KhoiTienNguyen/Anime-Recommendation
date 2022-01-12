import csv
import json
import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', required=True)
    parser.add_argument('-i', '--input', required=True)
    args = parser.parse_args()

    all_anime = open(args.input, encoding='utf-8')
    anime_data = json.load(all_anime)

    fieldnames = ["ID", "title"]

    with open(args.output, mode='w', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for i in anime_data:
            template = {}
            template["ID"] = anime_data[i]["mal_id"]
            template["title"] = anime_data[i]["title"]
            writer.writerow(template)

if __name__ == '__main__':
    main()