from urllib.request import Request, urlopen
import json
import time
import math
import argparse

def main():

    parser = argparse.ArgumentParser()
    # Output is a .txt file
    parser.add_argument('-o', '--output', required=True)
    args = parser.parse_args()

    # List of most popular clubs' ID on MyAnimeList
    # Modify the IDs if we want to extract users from specific clubs
    club_list = [22714,63421,17888,32683,19736,70668,256,34838,39921,2056,67199]
    for j in club_list:
        club_number = j
        file_object = open(args.output, "a")
        request = Request('https://api.jikan.moe/v3/club/{club}'.format(club = club_number))
        pages = urlopen(request).read()
        pages = json.loads(pages.decode("utf-8")).get('members_count')
        print("Total Number of Members for Club #" + str(j) + ": " + str(pages))
        print("Total Number of Pages: " + str(math.ceil(pages/35)))
        for n in range(math.ceil(pages/35)):
            print("Page: " +str(n+1))
            try:
                request = Request('https://api.jikan.moe/v3/club/{club}/members/{page}'.format(club = club_number, page = n+1))
                response_body = urlopen(request).read()
                members_list = json.loads(response_body.decode("utf-8")).get('members')
                for i in members_list:
                    file_object.write(i.get('username') + "\n")
                    print(i.get('username') + "\n")
                time.sleep(2)
            except Exception:
                print("No more pages")
                time.sleep(2)
                break
            file_object.close()
            file_object = open(args.output, "a")
        file_object.close()

if __name__ == '__main__':
    main()