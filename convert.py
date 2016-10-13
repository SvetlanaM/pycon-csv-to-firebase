import json
import pandas as pd
import uuid
import datetime
import dateutil.parser
import csv

file_name = input("Enter the name of the csv file: ")

if __name__ == '__main__':
    with open(file_name + '.csv', 'r') as csv_file:

        def get_dates(date):
            if date != "":
                date_parsed = dateutil.parser.parse(date).date()
                final_date = str(date_parsed.day) + "." + str(date_parsed.month) + "." + str(date_parsed.year)
                return final_date

        def get_times(date):
            if date != "":
                date_parsed = dateutil.parser.parse(date).time()
                final_time = str(date_parsed.hour) + "." + str(date_parsed.minute)
                return final_time

        rooms = ['d0206', 'd0207', 'd105', 'a112', 'a113']
        final_output = {}

        def set_twitter(twitter):
            if twitter != "":
                if twitter[0] == "@":
                    return twitter
                else:
                    return "@" + twitter



        def map_rooms(room):
            with open('pyconcz_schedule.csv', 'r') as csv_file:
                output = {room : []}
                for talk in csv.DictReader(csv_file):
                    if talk['room'] == room:
                        output[room].append({
                            'id' : str(uuid.uuid4()),
                            'start_date' : get_dates(talk['date_start']),
                            'end_date' : get_dates(talk['date_end']),
                            'start_time' : get_times(talk['date_start']),
                            'end_time' :  get_times(talk['date_end']),
                            'type' : talk['type'],
                            'title' : talk['title'],
                            'description' : talk['description'],
                            'speaker' : talk['speaker'],
                            'bio' : talk['bio'],
                            'avatar' : talk['avatar'],
                            'twitter' : set_twitter(talk['twitter']),
                            'github' : talk['github'],
                            'votes' : [""]
                    })

                    final_output.update(output)

    for room in rooms:
        map_rooms(room)

    csv_file.close()

    with open('data.json', 'w') as outfile:
        output_json = json.dump(final_output,  outfile, sort_keys = False, indent = 4, ensure_ascii=False)

    print ("Conversion is done")
