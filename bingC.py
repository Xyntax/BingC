# coding:utf-8

"""
Usage:
  python bingC.py IP/MASK [output_path]
Example:
  python bingC.py 132.12.43.0/24 result.txt
  python bingC.py 132.12.43.0/24
"""

import requests
import Queue
import threading
import re
import sys
import time
from IPy import IPy
from api import BingSearch
from config import ENABLE_API

queue = Queue.Queue()
ips = set()
lock = threading.Lock()
thread_num = 20


def scan():
    global thread_num
    while 1:
        if queue.qsize() > 0:
            ip = queue.get()
            if ENABLE_API:
                ans_obj = BingSearch("ip:" + ip)
                for each in ans_obj['d']['results']:
                    ips.add(ip + ' -> ' + each['Url'].split('://')[-1].split('/')[0] + " | " + each['Title'])
            else:
                q = "https://www.bing.com/search?q=ip%3A" + ip
                c = requests.get(q, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}).content
                p = re.compile(r'<cite>(.*?)</cite>')
                l = re.findall(p, c)
                for each in l:
                    domain = each.split('://')[-1].split('/')[0]
                    msg = ip + ' -> ' + domain
                    ips.add(msg)
        else:
            thread_num -= 1
            break


def api_scan():
    global thread_num
    while 1:
        if queue.qsize() > 0:
            BingSearch(queue.get())


def setThreadDaemon(thread):
    # Reference: http://stackoverflow.com/questions/190010/daemon-threads-explanation
    PYVERSION = sys.version.split()[0]
    if PYVERSION >= "2.6":
        thread.daemon = True
    else:
        thread.setDaemon(True)


def runThreads():
    print "Running..."
    for i in range(thread_num):
        t = threading.Thread(target=scan, name=str(i))
        setThreadDaemon(t)
        t.start()
    # It can quit with Ctrl-C
    while 1:
        if thread_num > 0:
            time.sleep(0.01)
        else:
            break


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)

    try:
        _list = IPy.IP(sys.argv[1])
    except Exception, e:
        sys.exit('Invalid IP/MASK, %s' % e)
    for each in _list:
        queue.put(str(each))

    runThreads()
    for each in ips:
        try:
            print each
        except UnicodeEncodeError:
            pass
    print "Total: " + str(len(ips))

    if len(sys.argv) is 3:
        path = sys.argv[2]
        try:
            f = open(path, 'w')
            for each in ips:
                f.write(each + '\n')
            f.close()
        except IOError, e:
            sys.exit('Invalid file path')
