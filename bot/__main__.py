import psutil
import os
import time
import server
import chat


print("Loading models...")
start = time.time()
model = chat.load_model()
end = time.time()
ram = psutil.Process(os.getpid()).memory_info().rss / 1000000
print("Done! Models loaded in", "{:.1f}".format(end - start),
      "seconds. Using", int(ram), "MB of RAM")

server.start(model)
