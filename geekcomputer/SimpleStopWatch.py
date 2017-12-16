import time

print('Press Enter to begin, Press Ctrl + C to stop')
while True:
    try:
        input()
        starttime = time.time()
        print('Started')
    except KeyboardInterrupt:
        print('Stopped')
        endtime = time.time()
        print('Total Time:', round(endtime - starttime, 2), 'secs')
        break
