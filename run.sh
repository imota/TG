#!/bin/bash

cd ~/workspace/TG

gnome-terminal \
    --tab -e "roscore" \
    --tab -e "python main.py" \
    --tab -e "python agent.py" \