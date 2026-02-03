print("Hello World?")

#import lab_chat < is fine
#from lab_chat import < better
#V is recommended by trevor.
import lab_chat as lc
#as is a keyword you cant use normally
def get_group():
    return get_input_upper("Enter your group: ")


def get_message():
    return get_input_upper("Enter your message: ")

def get_username():
    return get_input_upper("Enter your username: ")

def get_input_upper(mesg):
    return get_input(mesg).upper()
#its going to take a while for anything to make serious sense.

#In good programming, we want to make things more generic and re-useable.

def get_input(mesg):
    str_in = input(mesg)
    return str_in.strip()


#print(get_username())
#print(get_group())
#print(get_message())


#Try to recognize the parts of a function and the parameters. what line,
# where does it ends. what they are for what they are useful for.

#created seperate notepad txt file with completed ish assignment.

#familiarize yourself with importings

print('-'*120)

def initialize_chat():
    user_name = get_username()
    group = get_group()
    node = lc.get_peer_node(user_name)
    lc.join_group(node, group)
    return  lc.get_channel(node, group)

def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")

#most chat things you want to run forever, at least until we exit.

#control c is the keyboard interrupt.

#start_chat()


