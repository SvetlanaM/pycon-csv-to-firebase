import json
import uuid
import datetime
from datetime import timedelta
import dateutil.parser
import csv
from firebase import Firebase




if __name__ == '__main__':
    file_name = input("Enter the name of the csv file: ")

    with open(file_name + '.csv', 'r') as csv_file:

        def get_dates(date):
            if date != "":
                date_parsed = dateutil.parser.parse(date).date()
                final_date = str(date_parsed.day) + "." + str(date_parsed.month) + "." + str(date_parsed.year)
                return final_date

        def get_times(date, type):
            if date != "":
                date = date[0:18]
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
                if type == "workshop":
                    new_date2 = new_date + timedelta(hours = 1)
                elif type == "talk":
                    new_date2 = new_date + timedelta(hours = 2)
                else :
                    new_date2 = new_date + timedelta(hours = 1)
                final_time = new_date2.strftime("%H:%M")
                return final_time

        def get_end_time(date, type):
            if date != "":
                date = date[0:18]
                new_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
                if type == "workshop":
                    new_date2 = new_date + timedelta(hours = 1.5)
                elif type == "talk":
                    new_date2 = new_date + timedelta(hours = 2.5)
                else :
                    new_date2 = new_date + timedelta(hours = 1.5)
                final_time = new_date2.strftime("%H:%M")
                return final_time



        def get_rooms():
            rooms = []
            for room in csv.DictReader(csv_file):
                rooms.append(room['room'])
            rooms = dict.fromkeys(rooms).keys()
            return rooms

        rooms = get_rooms()
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
                            'start_time' : get_times(talk['date_start'], talk['type']),
                            'end_time' :  get_end_time(talk['date_start'], talk['type']),
                            'type' : talk['type'],
                            'title' : talk['title'],
                            'description' : talk['description'],
                            'speaker' : talk['speaker'],
                            'bio' : talk['bio'],
                            'avatar' : talk['avatar'],
                            'twitter' : set_twitter(talk['twitter']),
                            'github' : talk['github'],
                            'votes' : [""],
                            'active' : True
                    })
                    final_output.update(output)



    for room in rooms:
        map_rooms(room)

    f = Firebase('https://pycon-630b8.firebaseio.com/')
    f.child('rooms').set(final_output)
    csv_file.close()

    with open('data.json', 'w') as outfile:
        output_json = json.dump(final_output,  outfile, sort_keys = False, indent = 4, ensure_ascii=False)



    print ("Conversion is done")
