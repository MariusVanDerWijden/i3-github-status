#!/bin/bash
python ~/i3-github-status/i3-github-status.py &
i3status | while :
do
	read line
    value=$(<~/.ghnotes)
    echo "$value | $line" || exit 1
done
