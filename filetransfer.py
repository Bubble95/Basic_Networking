import networking

s = networking.Server('',1)
s.launch()

while True:
    s.send_file('hund.txt')

