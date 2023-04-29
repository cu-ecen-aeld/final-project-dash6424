import os

# Set the audio files
songs = ["test1.wav", "test2.wav", "test3.wav", "test4.wav"]
file_path = "audio_test.txt"

# Set the initial song to play and create a variable to keep track of the current song
current_song = songs[0]
song_index = 0

# Create a pipe to communicate with aplay
aplay_input, aplay_output = os.pipe()

# Start the loop for taking user input
while True:
    with open(file_path, "r") as f:
        lines = f.readlines()
        last_line = lines[-1].strip()
        
        # Check if the last line is a valid command
        if last_line == "1":
            # If the current song is paused, unpause it
            if aplay_process.closed or aplay_process.poll() is not None:
                aplay_process = os.popen(f"aplay -D sysdefault:CARD=0 -q -N {current_song} <&{aplay_output}", "w")
            # Otherwise, do nothing
            else:
                pass
                
        elif last_line == "2":
            # Pause the current song
            os.write(aplay_input, b"\x03")  # send the SIGINT signal to aplay
            
        elif last_line == "3":
            # Stop the current song and move to the previous song
            os.write(aplay_input, b"\x03")  # send the SIGINT signal to aplay
            song_index -= 1
            if song_index < 0:
                song_index = len(songs) - 1
            current_song = songs[song_index]
            aplay_process = os.popen(f"aplay -D sysdefault:CARD=0 -q -N {current_song} <&{aplay_output}", "w")

        elif last_line == "4":
            # Stop the current song and move to the next song
            os.write(aplay_input, b"\x03")  # send the SIGINT signal to aplay
            song_index += 1
            if song_index >= len(songs):
                song_index = 0
            current_song = songs[song_index]
            aplay_process = os.popen(f"aplay -D sysdefault:CARD=0 -q -N {current_song} <&{aplay_output}", "w")

        elif last_line == "5":
            # Stop playing songs
            os.write(aplay_input, b"\x03")  # send the SIGINT signal to aplay

# Close the pipe
os.close(aplay_input)
os.close(aplay_output)