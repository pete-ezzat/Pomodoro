#!/usr/bin/python2

import time
import pygame
import sys
import subprocess

user = subprocess.check_output(['whoami'])
user = str(user).rstrip()
alarm_file = "/home/" +user +"/bin/IndustrialAlarm.mp3"

def raise_alarm():
    pygame.init()
    pygame.mixer.music.load(alarm_file)
    pygame.mixer.music.play(10)

def start_timer(count):
   while count >= 0:
       if count == 0:
           raise_alarm()
           time.sleep(20)
           break
       print "Minutes Remaining: ", count
       time.sleep(60)
       count -= 1

if len(sys.argv) == 1:
   start_timer(25)
elif sys.argv[1] == "-n":
   count = int(sys.argv[2])
   start_timer(count)
