import psutil
import requests
import time
from datetime import datetime

API_URL="http://localhost:8000/api/metrics/"

def collect_metrics():
 data = {
     "CPU ": f"{psutil.cpu_percent()}%",
     "Memory": f"{psutil.virtual_memory().percent}%",
     "Disk": f"{psutil.disk_usage('/').percent}%",
     "Timestamp": str(datetime.now())
 }
 return data 

def send_metrics(data):
 try:
    response=request.post(API_URL,json=data)
    print("sent:",data ,"\n" "status:",response.status_code)
 except Exception as e:
    print("Error aagya oyyeee", e)

if __name__ == "__main__":
 while True:
   metrics=collect_metrics()
   send_metrics(metrics)
   print(metrics)
   time.sleep(1)
