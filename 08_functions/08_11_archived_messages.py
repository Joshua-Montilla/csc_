message = ["Hi, how are you?", "Do you wanna talk about your car's extended warranty?", "That's an awfully hot coffee pot."]

def show_message(send):
    for text in send:
        print(text)

sent_messages = []
def send_messages(message):
    while message:
        sending = message.pop()
        print(f'Moving, "{sending}" over...')
        sent_messages.append(sending)

send_messages(message[:])

show_message(message)
print(sent_messages)