import csv
import os
import requests


def enhance(row):
    api_key = open("API", "r").read()
    id = row[1]
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
        # get the images from the json data
        poster = data["poster_path"]
        backdrop = data["backdrop_path"]
        row.append(poster)
        row.append(backdrop)

    except Exception as e:
        print(e)
    return row


def main():
    with open("index.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        i = 0
        for row in reader:
            # write in enhanced.csv
            with open("enhanced.csv", "a") as enhanced:
                writer = csv.writer(enhanced)
                writer.writerow(enhance(row))
            i += 1
            print(str(i) + " movies enhanced")
