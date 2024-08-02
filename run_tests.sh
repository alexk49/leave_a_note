#!/bin/bash

# starts server on localhost in background
# and then runs tests on localhost server

# make sure the background processes spawned by script are killed
# taken from https://stackoverflow.com/questions/360201/how-do-i-kill-background-processes-jobs-when-my-shell-script-exits
trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT
#trap "exit" INT TERM ERR
#trap "kill 0" EXIT

running=true

while "$running" '==' true; do
    .dev-venv/bin/python3 leave_a_note/app.py &
	.dev-venv/bin/python3 -m unittest discover -v
    running=false
done
