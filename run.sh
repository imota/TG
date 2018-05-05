#!/bin/bash

cd ~/workspace/TG

gnome-terminal \
    --tab -e "roscore" \
    "source devel/setup.bash" \
    "source devel/setup.sh" \
    --tab -e "rosrun tg_package main.py" \
    "source devel/setup.bash" \
    "source devel/setup.sh" \
    --tab -e "rosrun tg_package agent.py" \