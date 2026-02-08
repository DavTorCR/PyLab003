print("Hello World.")

#this lab we will build a basic peer to peer chat system using existing python
# libraries and the lab_chat.py file shared in this repo. The goal is to create functions
# that allows users to join a chat group and send and receive messages.
#we'll explore core concepts of pyton defining function, parameters,
# simple loops, and importing and calling existing functions.

#This lab is divided into four parts and should take approx. two hours to complete.
#"I'm hoping I can manage that as opposed to taking longer like I usually do."#

#Pre Reqs: install zero mq pyre.

#Part one: Core functions, Data handling and user input.
#we'll create several basic functions to handle user input and data that will be used in the later stages
#we will begin by practicing creating proper functions headers and bodies.

#This is a line break function, it displays a line break by printing out one hundred dashes
def lb():
    print("-"*100)
#zeromq0pyre installed using the pycharm python packages left hand menu, The Python Packages I
# also have installed shows that ipaddress(1.0.23), pip(25.0.1), pyzmq(27.1.0), zeromq-pyre(0.3.4)

lb()

import lab_chat as lc


def get_user_input(messages, to_upper = True):
    if to_upper:
        response = input(messages).strip().upper()
    else:
        response = input(messages).strip()
    return response

def get_username():
      return get_user_input("Please enter your preferred User Name: ")

def get_group():
    return get_user_input("Please enter the Name of the Group you would like to join: ")

def get_message():
    return get_user_input("Please enter the message you would like to send: ", False)

def initialize_chat():
    users = get_username()
    groups = get_group()
    node = lc.get_peer_node(users)
    lc.join_group(node, groups)
    channel = lc.get_channel(node, groups)
    return channel

def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf-8'))
        except (KeyboardInterrupt, SystemExit):
            break
        channel.send("$$$STOP".encode('utf-8'))
        print("FINISHED")

print(start_chat())




