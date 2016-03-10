#!/usr/bin/sh

jar=$(which jar)

if [ -x "$jar" ]; then
    LIST=$(jar tf "$1") 
else
    echo "jar must be available on your path"
    exit
fi

for f in $LIST; do 
    $(javap -classpath "$f")
done 
