import json
import argparse

def main():

    parser = argparse.ArgumentParser()
    # Input file format
    parser.add_argument('-i', '--input_file_format', required=True)
    # Output file
    parser.add_argument('-o', '--output', required=True)
    # First file index to start combining
    parser.add_argument('-s', '--start_index', required=True)
    # Last file index to be combined
    parser.add_argument('-e', '--end_index', required=True)
    args = parser.parse_args()

    total = open(args.output, "w")
    everything = {}
    for k in range(int(args.start_index), int(args.end_index) + 1):
        file_number = args.input_file_format.find(".json")
        file_name = args.input_file_format[:file_number] + str(k) + args.input_file_format[file_number:]
        example = open(file_name)
        data = json.load(example)
        example.close()
        for i in data:
            everything[i] = data[i]

    sorted(everything)
    print("Total number of entries:" + str(len(everything)))
    total.write(json.dumps(everything, indent=4, sort_keys=True))
    total.close()

if __name__ == '__main__':
    main()