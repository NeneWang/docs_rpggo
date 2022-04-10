import re, random, string, json
#from google.colab import files
import files
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

import numpy as np
from collections import defaultdict
from csv import reader

from nltk.stem import WordNetLemmatizer, PorterStemmer
import nltk
from nltk import pos_tag
#nltk.download("all")

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

topic_list = ['business', 'food-and-drink', 'music', 'health', 'charity-and-causes', 'film-and-media', 'travel-and-outdoor', 'science-and-tech']

location_list = ['in a Castle', 'in a Village', 'at a Lake', 'in a Grove', 'at a Sea', 'in a Dungeon', 'in a Wilderness', 'in a Town']

race_list = ['An aristocrat', 'A noblewoman', 'A sage', 'A priest', 'An adventurer', 'An elf', 'A lady', 'A dwarf', 'A merchant', 'A goblin', 'A giant', 'An angel', 'A dragon', 'A demon']

#text = "Curiouser & Curiouser with Kai Alcé*, Rissa Garcia"
#location = "Green-Wood Cemetery"
#topic = "business"

def stem_lemmatization(ori_list):
    new_list = []
    for token in ori_list:
        token = lemmatizer.lemmatize(token)
        token = stemmer.stem(token)
        new_list.append(token)
    return new_list
#(" ".join(new_list))

def extractNN(postag):
    NN = []
    cur_NN = ""
    for cur_tag in postag:
        if cur_tag[1] == "NN" and cur_tag[0] != "thi" and not "," in cur_tag[0]:
            cur_NN = cur_NN + cur_tag[0] + " "
            selected_NN = cur_NN
        else:
            if len(cur_NN) != 0:
                NN.append(cur_NN)
            cur_NN = ""
    NN.append(cur_NN)
    if (len(NN) == 0):
        NN.append("flower ")
    return max(NN, key=len)

def extractLocation(topic):
    index = topic_list.index(topic)
    return location_list[index]

def questGenerator(NN, location, race):
    return race + " asks you to seek " + NN + location + "."
    
def latlngGenerator(location):
    geolocator = Nominatim(user_agent="geoapi")
    try:
        address = geolocator.geocode(location + ", United States")
        address_tuple = (address.latitude, address.longitude)
    except:
        address_tuple = (0, 0)
    return address_tuple
    
def processEvent(event):
    topic = event[0][1:-2]
    text = event[1][1:-2]
    location = event[3][1:-2]
    full_location = event[4][1:-1]
    text_token = re.split("\s+", text.rstrip())
    text_token = stem_lemmatization(text_token)
    postag = pos_tag(text_token)
    selected_NN = extractNN(postag)
    selected_location = extractLocation(topic) + " called " + location
    selected_race = random.choice(race_list)
    quest = questGenerator(selected_NN, selected_location, selected_race)
    address = latlngGenerator(full_location)
    
    result = {
        "topic": topic,
        "title": text,
        "location": location,
        "quest": quest,
        "target": address #(lat, lng)
    }
    return result
    
def readJsonFile(file_name):
    events = []
    cur_event = []
    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            cur_line = line.strip()
            if cur_line not in ["[", "]", "{", "}", "},"]:
                if len(cur_event) == 5:
                    events.append(cur_event)
                    cur_event = []
                cur_event.append(line.strip().split(": ", 1)[1])
    events.append(cur_event)
    return events

def writeJsonFile(events, file_name):
    json_list = list()
    for event in events:
        json_event = processEvent(event)
        json_list.append(json_event)
    with open(file_name, 'w') as file:
        json.dump(json_list, file)

def main():
    events = readJsonFile('event.json')
    writeJsonFile(events, 'output.json')
    #print(latlngGenerator("CIVILIAN HOTEL, New York, NY"))
    
if __name__ == "__main__":
    main()
    
    


