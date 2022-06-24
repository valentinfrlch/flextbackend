# create a csv file with the following columns:
# name, id, path, type

import os
import csv
from pathlib import Path
import requests


def get_id(name):
    with open("API", "r") as keyfile:
        api_key = keyfile.read()
    baseurl = "https://api.themoviedb.org/3/"
    # make a search request
    url = "https://api.themoviedb.org/3/search/movie?api_key=" + \
        api_key + "&query=" + name + "&language=de-DE&page=1&include_adult=true"
    # get the response
    try:
        search = requests.get(url)
        # get the json data
        data = search.json()
        # get the id of the first result
        id = data["results"][0]["id"]
    except IndexError:
        id = ""
    return id


def index(path):
    i = 1
    # get all the files in path
    files = os.listdir(path)
    # check if index.csv exists in "home/scripts/flextbackend"
    if Path("index.csv").is_file():
        #if yes, delete it
        os.remove("index.csv")
    for file in files:
        # get the file's path
        filepath = os.path.join(path, file)
        # get the folder's name where the file is located
        nametype = os.path.basename(os.path.dirname(filepath))
        if nametype == "Filme":
            type = "movie"
        else:
            type = "series"
        name = file.replace(".mp4", "")
        id = get_id(name)
        # write the name, id, path and type to the csv file
        with open("index.csv", "a") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, id, type, filepath])
        print(name, str(i) + "/" + str(len(files)))
        i += 1


def main():
    index("/media/pi/F01/Flext/Filme")

