import time, math

def slowdown(secs):
  start = time.clock()
  i = 0
  j = 0
  while time.clock()-start < secs:
    j += (math.cos(i) + math.sin(i*-1))
    k = math.hypot(j, i)
    i += 1

