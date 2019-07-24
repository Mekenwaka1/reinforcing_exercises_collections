rooms_and_events = { 'data': { 'rooms': 
    [ { 'id': 1, 'room_number': "201", 'capacity': 50}, { 'id': 2, 'room_number': "301", 'capacity': 200 }, { 'id': 3, 'room_number': "1B", 'capacity': 100}
    ],
    'events': [
      { 'id': 1, 'room_id': 2, 'start_time': 18, 'end_time': 20, 'attendees': 75 },
      { 'id': 2, 'room_id': 1, 'start_time': 10, 'end_time': 18, 'attendees': 25 },
      { 'id': 3, 'room_id': 2, 'start_time': 10, 'end_time': 18, 'attendees': 20 },
      { 'id': 4, 'room_id': 3, 'start_time': 18, 'end_time': 21, 'attendees': 56 },
    ]
  }
}

# Exercise 1
room_201_capacity = (rooms_and_events['data']['rooms'][0]['capacity'])
# print(room_201_capacity)

# Exercise 2
def room_events_by_capacity(capacity, room_id, rooms_and_events):

  for item in rooms_and_events['data']["events"]:
    if ((item["attendees"] <= rooms_and_events["data"]["rooms"][0]["capacity"]) and (item["room_id"] == room_id)):
        print("ok")

room_events_by_capacity(50, 1, rooms_and_events)
