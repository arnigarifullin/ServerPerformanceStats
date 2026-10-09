import psutil
import time
import datetime 


processes = []

def get_processes_list():
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try: 
            info = proc.info
            mem_usage = info['memory_precent']
            cpu_usage = info['cpu_precent']
            time = datetime.datetime.now

            procces_data = {
                'date': time.strftime("%H:%M:%S %m %d %Y"),
                'pid': info['pid'],
                'name': info['name'],
                'cpu_percent': cpu_usage,
                'memory_percent': mem_usage
            }
            processes.append(procces_data)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    




while True:
    get_processes_list
    time.sleep(1.0)
    print(processes)