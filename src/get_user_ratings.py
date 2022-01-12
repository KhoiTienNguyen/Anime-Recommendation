from urllib.request import Request, urlopen
import json
import time
import argparse

def main():

    parser = argparse.ArgumentParser()
    # Output file format
    parser.add_argument('-o', '--output', required=True)
    # Input .txt file containing list of usernames generated from get_users_from_clubs.py
    parser.add_argument('-i', '--input', required=True)
    # File number to start outputting at
    parser.add_argument('-c', '--file_count', required=True)
    # Number of users per file
    parser.add_argument('-n', '--number_of_users_per_file', required=True)
    args = parser.parse_args()

    filecount = int(args.file_count)
    file_number = args.output.find(".json")
    file_name = args.output[:file_number] + str(filecount) + args.output[file_number:]
    # Input is the .txt file generated from clubs.py
    userlist = open(args.input, "r")
    # Output is a .json file containing all relevant information from the users
    file_object = open(file_name, "w")
    user_dict = {}
    Lines = userlist.readlines()

    count = 0
    for j in Lines:
        if count % int(args.number_of_users_per_file) == 0 and count != 0:
            filecount +=1
            file_object.write(json.dumps(user_dict, indent=4, sort_keys=True))
            file_object.close()
            user_dict = {}
            file_name = args.output[:file_number] + str(filecount) + args.output[file_number:]
            file_object = open(file_name, "w")
        username = j.strip()
        user_dict[username] = {}
        print(str(count) + ": " + username)
        for i in range(99999):
            if i == 0:
                print("File " + str(filecount))
            try:
                request = Request('https://api.jikan.moe/v3/user/{username}/animelist/all/{page}'.format(username = username, page = i + 1))
                pages = urlopen(request, timeout = 10).read()
                print("Page " + str(i+1))
                pages = json.loads(pages.decode("utf-8"))
                if pages.get("anime") == []:
                    print("No more pages")
                    # time.sleep(0.5)
                    break
                # user_dict[username].append(pages.get("anime"))
                for n in pages.get("anime"):
                    if n.get("score") == 0:
                        continue
                    user_dict[username][n.get("mal_id")] = n.get("score") # added score
                # time.sleep(0.5)
            except Exception as error:
                print(error)
                time.sleep(2)
                break
        count+=1

    file_object.write(json.dumps(user_dict, indent=4, sort_keys=True))
    file_object.close()

if __name__ == '__main__':
    main()