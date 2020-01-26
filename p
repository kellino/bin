#!/bin/bash

cd "$HOME" || exit 
TARGET=$(fd -e pdf -e djvu -E Library/ -E Documents/PhD-Miscellany -E Documents/Scores | fast-p |\
            fzf --read0 --reverse -e -d ' '\
                --preview-window down:40% \
                --preview 'v=$(echo {q} | tr " " "|"); echo -e {1}"\n"{2} | rg "^$|v" -i --color=always' \
                | awk '/./{print; exit}' | cut -d$'\t' -f1 | tr -d '\n')

MON=$(chunkc tiling::query --monitor-for-desktop 3)

if [ -z "$TARGET" ]; then
    exit 0
fi

if [ -z "$MON" ]; then
    open "$TARGET"
else
    open "$TARGET"
    sleep 2
    wins=$(chunkc tiling::query --desktop windows)
    case "$wins" in
        *Skim*) 
            chunkc tiling::window --focus Skim
            chunkc tiling::window --send-to-monitor 3
            chunkc tiling::monitor -f 3
            ;;
        *DjView*)
            chunkc tiling::window --focus DjView
            chunkc tiling::window --send-to-monitor 3
            chunkc tiling::monitor -f 3
            ;;
        *) 
            exit
            ;;
    esac
fi 
