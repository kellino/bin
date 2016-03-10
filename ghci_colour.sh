#!/bin/sh
# Colors
red=`echo “33[91m"`
green=`echo "33[92m"`
yellow=`echo "33[93m"`
blue=`echo "33[94m"`
purple=`echo "33[95m"`
cyan=`echo "33[96m"`
# Bold colors
bold=`echo "33[1m"`
bold_red=`echo "33[1;91m"`
bold_green=`echo "33[1;92m"`
bold_yellow=`echo "33[1;93m"`
bold_blue=`echo "33[1;94m"`
bold_purple=`echo "33[1;95m"`
bold_cyan=`echo "33[1;96m"`
# Color reset
reset=`echo "33[0m"`
# Patterns
double_colon="s/::/$red&$reset/;"
rocket="s/=>/$red&$reset/;"
left_arrow="s//$red&$reset/;"
strings="s/"[^"]*”/$yellow&$reset/g;”
chars=”s/’[a-zA-Z]*’/$purple&$reset/g;”
exec “`which ghc`” –interactive ${1+”$@”} |
sed “$double_colon
$rocket
$right_arrow
$left_arrow
$strings
$chars”
