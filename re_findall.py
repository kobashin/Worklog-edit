import os
import re
import datetime

path = './worklog.txt'
path_to = './newworklog.txt'
checkpath = os.path.exists(path)

def calcmin(start, end):
    time_start = 60 * start.tm_hour + start.tm_min
    time_end = 60 * end.tm_hour + end.tm_min
    return time_end - time_start

with open(path, encoding='shift-jis') as r:
    lines = r.readlines()
    line_strip = [line.strip() for line in lines]

    regex = '\d+:\d{2}'
    pattern = re.compile(regex)
    timestamp = [pattern.findall(line) for line in line_strip if len(pattern.findall(line)) != 0]

    print(timestamp)

    starttime = [datetime.datetime.strptime(stamp[0], '%H:%M') for stamp in timestamp]
    endtime = [datetime.datetime.strptime(stamp[1], '%H:%M') for stamp in timestamp]
    spenttime = [end - start for end, start in zip(endtime, starttime)]
    spenttimeformat = ["{:02}:{:02}".format(delta.seconds // 3600, delta.seconds % 3600 // 60) for delta in spenttime]

    print(starttime)
    print(endtime)
    print(spenttime)
    print(spenttimeformat)
