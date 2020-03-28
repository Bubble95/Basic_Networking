import networking, time

s = networking.Server('',23)
s.send_file('hund.txt')

time.sleep(10)
