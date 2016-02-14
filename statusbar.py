from i3pystatus import Status

status = Status(standalone=True)

black = "#2c2836"
darkblack = "#73707e"
red = "#bb7473"
darkred = "#cf9fa4"
green = "#68b782"
darkgreen = "#9acbad"
yellow = "#abb773"
darkyellow = "#c5cba4"
blue = "#7865c5"
darkblue = "#a396d9"
magenta = "#bb65b6"
darkmagenta = "#cf96cf"
cyan = "#68a8c5"
darkcyan = "#9ac1d9"
white = "#f1edfb"
darkwhite = "#f1edfb"
background = "#133B47"

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock", format="%a %-d %b %X CW%V",)

# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)
status.register("load")

# Shows your CPU temperature, if you have a Intel CPU
status.register("temp", format="{temp:.0f}°C",)

status.register("cpu_usage",)

status.register("mem",
                format="MEM: {percent_used_mem}%",)

status.register("battery",
                format="{status} {percentage:.0f}% {remaining:%E%hh:%Mm}",
                alert=True,
                alert_percentage=5,
                color=white,
                critical_color=red,
                charging_color=yellow,
                full_color=green,
                status={
                    "DIS": "DIS",
                    "CHR": "CHR",
                    "FULL": "full",
                },)

# Note: requires both netifaces and basiciw (for essid and quality)
status.register("network",
                interface="wlp3s0",
                format_up="{essid} {quality:3.0f}%",
                color_up="#3eb0dl",)

status.register("openvpn",
                vpn_name="openvpn",)

# Shows disk usage of /
# Format:
# 42/128G [86G]
status.register("disk",
                path="/",
                format="{used}/{total}G [{avail}G]",)

# shows alsamixer volume
status.register("alsa",
                format="♪{volume}",
                color_muted=red,
                color=cyan,)

# shows cmus status
status.register("cmus",)

status.run()
