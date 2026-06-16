import time
from collections import deque
import numpy as np

TIME_WINDOW = 5
buffer = deque()

def add_packet(size, ttl):
    now = time.time()
    buffer.append((now, size, ttl))

    while buffer and now - buffer[0][0] > TIME_WINDOW:
        buffer.popleft()

def get_features():
    if len(buffer) == 0:
        return None

    sizes = [x[1] for x in buffer]
    ttls = [x[2] for x in buffer]

    return {
        "rate": len(buffer) / TIME_WINDOW,
        "avg_size": np.mean(sizes),
        "ttl_avg": np.mean(ttls)
    }