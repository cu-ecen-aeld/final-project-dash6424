# Author: Daanish Shariff
# Name: i2s_sequencer.py
# Description: Audio play sequencer script. This script continuously polls the value at audio_test.txt file and executes the respective command. By default it writes a valid 9 to be the invalid command.
# Commands:
# 1 - Play
# 2 - Previous
# 3 - Next
# 4 - Stop
# 9 - Default invalid command
# Date Modified: 05/01/2023
# References: 
# 1. File read write operation: https://www.guru99.com/reading-and-writing-files-in-python.html
# 2. aplay command for audio playback: https://stackoverflow.com/questions/45136500/using-aplay-to-play-a-sound-through-subprocess-within-a-python-script
# 3. File mutex lock: https://stackoverflow.com/questions/6931342/system-wide-mutex-in-python-on-linux

########################################## Imports ################################################
import os
import fcntl
import time

########################################## Global Variables ################################################
# Define the file path and songs
songs = ["/usr/bin/test1.wav", "/usr/bin/test2.wav", "/usr/bin/test3.wav", "/usr/bin/test4.wav"]
file_path = "/usr/bin/audio_test.txt"

# Initialize the current song variable to hold current song
current_song = None
# idx of song offset in list
idx = 0

# Set the file to default state.
with open(file_path, "w") as f:
    fcntl.flock(f, fcntl.LOCK_EX)
    f.write("9\n") 
    fcntl.flock(f, fcntl.LOCK_UN)

# Wait for a few seconds before checking the file again
time.sleep(2)

while True:
    with open(file_path, "r") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        lines = f.readlines()
        fcntl.flock(f, fcntl.LOCK_UN)
        last_line = lines[-1].strip()

    # Check if the last line is a valid command
    if last_line == "1": # Play command
        # Stop the current song, if there is one
        if current_song is not None:
            os.system("killall aplay")
            time.sleep(1)  # wait for the current song to stop
        
        # Play the new song
        current_song = songs[idx]
        os.system(f"aplay -q {current_song} &")
        # Set the file to default state.
        with open(file_path, "w") as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            f.write("9\n") 
            fcntl.flock(f, fcntl.LOCK_UN)

    elif last_line == "2": # Previous command
        # Stop the current song, if there is one
        if current_song is not None:
            os.system("killall aplay")
            time.sleep(1)  # wait for the current song to stop  
        
        # Play the previous song
        idx = idx - 1
        if idx < 0:
            idx = 3
        current_song = songs[idx]
        os.system(f"aplay -q {current_song} &")  # add "&" to run in the background
        # Set the file to default state.
        with open(file_path, "w") as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            f.write("9\n") 
            fcntl.flock(f, fcntl.LOCK_UN) 

    elif last_line == "3": # Next command
        # Stop the current song, if there is one
        if current_song is not None:
            os.system("killall aplay")
            time.sleep(1)  # wait for the current song to stop
        
        # Play the next song
        idx = idx + 1
        if idx == 4:
            idx = 0
        current_song = songs[idx]
        os.system(f"aplay -q {current_song} &")  # add "&" to run in the background
        # Set the file to default state.
        with open(file_path, "w") as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            f.write("9\n") 
            fcntl.flock(f, fcntl.LOCK_UN)

    elif last_line == "4": # Stop command
        # Stop the current song, if there is one
        if current_song is not None:
            os.system("killall aplay")
            current_song = None  # reset the current song variable
            idx = 0
        # Wait for a few seconds before checking the file again
        time.sleep(2)
        # Set the file to default state.
        with open(file_path, "w") as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            f.write("9\n") 
            fcntl.flock(f, fcntl.LOCK_UN)
    else: # Invalid command
        pass
    
    # Wait for a few seconds before checking the file again
    time.sleep(2)