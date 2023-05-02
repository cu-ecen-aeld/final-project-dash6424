# Audio Playback using Bluetooth Control

# Project Team:
Daanish Shariff \
Sachin Mathad \
Sudarshan Jagannathan 

# Project Overview:
The overview is hosted at this [link](https://github.com/sachininja/final-project-SachinMathad/wiki/Project-Overview).

# Project Schedule:
The Project schedule is hosted at this [link](https://github.com/users/sachininja/projects/1/views/1?groupedBy%5BcolumnId%5D=39014094).


# Description:
This git hub link contains the database required to be loaded on the buildroot image.

i2s configuration and audio Playback, refer to buildroot image:
https://github.com/cu-ecen-aeld/final-project-sachininja/tree/i2s-buildroot

Entire audio playback with bluetooth commands, refer to buildroot image:
https://github.com/cu-ecen-aeld/final-project-sachininja/tree/integrated_build

# Files:
1. asound.conf - Contains the soundcard configuration details with default media format to be 44100kHz, 16bits per sample and stereo channel. Sets the i2s in master mode.
Add this file to the following path of buildroot image:
<Base_directory>//buildroot/board/raspberrypi3/config_3.txt --> Considering raspberry pi 3B/3B+. In case of other targets, add it to respective boot config.txt
2. config.txt - This is a bootup config file that is not required to be pushed on buildroot but has 3 important soundcard packages that need to be booted on rpi.
dtoverlay=hifiberry-dac
dtoverlay=i2s-mmap
3. i2s_sequencer.py - Is the script that polls the audio_test.txt file to receive commands and plays digital data over i2s pins on rpi.
4. max98357a - The hw codec that supports i2s to read digital data and play audio over speaker.
5. test1.wav, test2.wav, test3.wav & test4.wav - are the 4 audio files that are loaded on the buildroot image to test audio functionality.