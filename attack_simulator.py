import requests
import random
import time

URL = "http://127.0.0.1:5000/predict"

print("🚀 Starting Simulation...")

for i in range(300):
    if random.random() < 0.7:
        size = random.randint(50, 100)
        ttl = random.randint(50, 70)
    else:
        size = random.randint(1500, 3000)
        ttl = random.randint(1, 10)

    features = [size, ttl] + [0]*83

    res = requests.post(URL, json={"features": features}).json()
    print(res)

    time.sleep(0.2)