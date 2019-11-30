import psutil
import os
import src.server as server
import time


def current_ram():
    process = psutil.Process(os.getpid())
    ram = process.memory_info().rss / 1000000

    return str(int(ram)) + " MB"


print("Loading models...")
start = time.time()
end = time.time()
print("Done! Models loaded in", "{:.1f}".format(end - start),
      "seconds. Using", current_ram(), "of RAM")

server.start()
