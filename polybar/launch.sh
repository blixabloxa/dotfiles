#!/usr/bin/env bash

# Terminate already running bar instances
killall -q polybar
# If all your bars have ipc enabled, you can also use 
# polybar-msg cmd quit

# Launch mybar
echo "---" | tee -a /tmp/polybar1.log /tmp/polybar2.log
polybar mybar >>/tmp/polybar.log 2>&1 & disown

echo "Bar launched..."
