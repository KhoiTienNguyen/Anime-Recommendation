from urllib.request import Request, urlopen
import json
import time
import argparse


def main():

    parser = argparse.ArgumentParser()
    # Output file
    parser.add_argument('-o', '--output', required=True)
    # Start requesting at this Anime ID
    parser.add_argument('-s', '--start_id', required=True)
    # Stop requesting at this Anime ID
    parser.add_argument('-e', '--end_id', required=True)
    # File number to start outputting at
    parser.add_argument('-c', '--file_count', required=True)
    # Number of anime per file
    parser.add_argument('-n', '--number_of_anime_per_file', required=True)

    args = parser.parse_args()

    filecount = int(args.file_count)
    count = 0
    file_number = args.output.find(".json")
    file_name = args.output[:file_number] + str(filecount) + args.output[file_number:]
    animelist1 = open(file_name, "w")

    all_anime = {}
    # As of July 2021, the highest anime ID on MyAnimeList is 54000
    for n in range(int(args.start_id), int(args.end_id) + 1):
        successful = False
        while not successful:
            print(count)
            if count % int(args.number_of_anime_per_file) == 0 and count != 0:
                print("here")
                filecount+=1
                animelist1.write(json.dumps(all_anime, indent=4, sort_keys=True))
                animelist1.close()
                all_anime = {}
                file_name = args.output[:file_number] + str(filecount) + args.output[file_number:]
                animelist1 = open(file_name, "w")
            print("ID: " + str(n))
            try:
                request = Request('https://api.jikan.moe/v3/anime/{number}/'.format(number = n))
                pages = urlopen(request, timeout = 10).read()
                pages = json.loads(pages.decode("utf-8"))
                print(pages["title"])
                temp = {"mal_id":n+1, "title":"", "score":-1,"rating":"","members":-1,"type":"","genres":[]}

                temp["mal_id"] = pages["mal_id"]
                temp["title"] = pages["title"]
                temp["score"] = pages["score"]
                temp["rating"] = pages["rating"]
                temp["members"] = pages["members"]
                temp["type"] = pages["type"]
                for i in pages["genres"]:
                    temp["genres"].append(i["name"])
                all_anime[temp["mal_id"]] = temp
                count+=1
                successful = True
            except Exception as error:
                print(error)
                successful = True
                if str(error) == "HTTP Error 429: Too Many Requests":
                    successful = False
                    time.sleep(0.5)
            time.sleep(2)

    animelist1.write(json.dumps(all_anime, indent=4, sort_keys=True))
    animelist1.close()

if __name__ == '__main__':
    main()