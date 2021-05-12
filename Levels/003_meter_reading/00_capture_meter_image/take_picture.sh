# fswebcam is for USB camera
# raspistill is for RPi bus camera
#
# crontab periodically run this script
#!/bin/bash
DATE=$(date +"%Y-%m-%d_%H%M")
fswebcam -r 1280x720 --font luxisr:24 --title $DATE /home/pi/Pictures/$DATE.jpg
#raspistill -o /home/pi/Pictures/$DATE.jpg

# Once take a picture, it upload to implement http://bit.ly/websensor1
/usr/bin/python3 upload.py $DATE.jpg
