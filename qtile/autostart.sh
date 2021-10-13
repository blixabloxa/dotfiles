#!/usr/bin/env bash 

nitrogen --restore &
picom -b -f &
nm-applet &
/usr/bin/dunst &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/bin/gnome-keyring-daemon --start --components=secrets &
