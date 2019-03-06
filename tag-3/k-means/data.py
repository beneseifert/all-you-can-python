import random

data = []
# cluster 1
for i in range(40):
    data.append((random.randint(20, 130), random.randint(280, 360)))

# cluster 2
for i in range(40):
    data.append((random.randint(120, 320), random.randint(140, 240)))

# cluster 3
for i in range(40):
    data.append((random.randint(280, 400), random.randint(220, 320)))

# cluster 4
for i in range(40):
    data.append((random.randint(40, 140), random.randint(80, 160)))

# noise
for i in range(40):
    data.append((random.randint(0, 400), random.randint(0, 400)))
