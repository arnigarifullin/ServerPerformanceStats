import psutil
import time
import datetime 
import json
import os

def get_processes_list():

    processes = []

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try: 
            
            info = proc.info
            mem_usage = info['memory_percent'] or 0.0
            cpu_usage = info['cpu_percent'] or 0.0

            procces_data = {
                'pid': info['pid'],
                'name': info['name'],
                'cpu_percent': cpu_usage,
                'memory_percent': mem_usage
            }
            processes.append(procces_data)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    cpu_top_usage = sorted(processes, key=lambda x: x['cpu_percent'],reverse=True)[:5]
    mem_top_usage = sorted(processes, key=lambda x: x['memory_percent'],reverse=True)[:5]

    now = datetime.datetime.now()
    
    return {
        'timestamp': now.strftime("%H:%M:%S %Y-%m-%d"),
        'system_summary': {
            'total_cpu_percent': psutil.cpu_percent(interval=None),
            'total_ram_percent': psutil.virtual_memory().percent
        },
        'cpu_top_5': cpu_top_usage,
        'ram_top_5': mem_top_usage
    }

def save_to_json(data, filename="metrics.json"):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("Starting. To exit Ctrl + C\n")
    
    try:
        while True:
            metrics = get_processes_list()

            save_to_json(metrics)

            print(f"[{metrics['timestamp']}]")
            
            time.sleep(10.0)

    except KeyboardInterrupt:
        print("\n\nEND.")