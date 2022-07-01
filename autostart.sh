#!/bin/sh
setxkbmap es &

udiskie -t &

xrandr --output HDMI1 --primary --right-of eDP1 &

nm-applet &


picom --no-vsync &

cd .config/qtile

./key.sh


nitrogen --restore &
