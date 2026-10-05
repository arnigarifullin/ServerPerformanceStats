import psutil
import time

def main_usage(cpu_usage, memory_usage):
    print(cpu_usage)
    print(memory_usage)



while True:
    main_usage(psutil.cpu_percent, psutil.virtual_memory.percent)
    time.sleep(1.0)