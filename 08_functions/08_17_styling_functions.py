def make_car(maker, model, **car_info):
    car_info["manufacturer"] = maker
    car_info["car model"] = model
    return car_info

car= make_car("Lamborghini", "Temerario", 
               color = "blue", 
               elctric_vehicle = True)

print(car)

print("\n")

message= ["Hi, how are you?", 
           "Do you wanna talk about your car's extended warranty?", 
           "That's an awfully hot coffee pot."]

def show_message(send):
    for text in send:
        print(text)

sent_messages= []
def send_messages():
    while message:
        sending= message.pop()
        print(f'Moving, "{sending}" over...')
        sent_messages.append(sending)

send_messages()

print(message)
print(sent_messages)

print("\n")

def make_album(name, album, songs=None):
    artist= {"Artist": name, "Album": album}
    if songs:
        artist["Number of Songs"]= songs
    return artist

musician1= make_album("Eminem", "The Eminem Show", 38)
print(musician1)
musician2= make_album("Siames", "HOME")
print(musician2)
musician3= make_album("Cigarettes After Sex", "Cry")
print(musician3)