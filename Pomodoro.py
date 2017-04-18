#!/usr/bin/python2

import time
import pygame
import sys
import subprocess
import argparse

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

parser = argparse.ArgumentParser(description="Pomodoro Technique")
parser.add_argument('-n', type=str, help="Number of minutes", required=False)
cmdargs = parser.parse_args()

if int(cmdargs.n) == 1:
   count = int(cmdargs.n)
   start_timer(count)
else:
   start_timer(25)
