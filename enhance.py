import csv
import os
import requests


def enhance():
    # get the apikey from API
    with open("API", "r+") as keyfile:
        api_key = keyfile.read()
    # open the file "index.csv" in "home/scripts/flextbackend"
    with open("index.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        # for every row in the csv file make a request to the themoviedb.org API
        for row in reader:
            # get the id of the file
            id = row[1]
            #make a request to the themoviedb.org API
            url = "https://api.themoviedb.org/3/movie/" + \
                id + "?api_key="+api_key+"&language=de-DE"
            # get the response
            try:
                response = requests.get(url)
                # get the json data
                data = response.json()
                release_date = data["release_date"]
                row.append(release_date)
                # get the genres from the json data
                genres = []
                for genre in data["genres"]:
                    genres.append(genre["name"])
                row.append(genres)
                description = data["overview"]
                row.append(description)
                runtime = data["runtime"]
                row.append(runtime)
                print(genres)
            except Exception as e:
                print(e)
                continue


enhance()
