locationOfScript=$(dirname "$(readlink -e "$0")")

screen -S "draw_screen" -d -m
screen -r "draw_screen" -X stuff 'sudo '$locationOfScript'/script/stream.py '$1' /dev/ttyUSB0\n'
screen -r "draw_screen"
