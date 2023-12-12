import os
import time
import threading
from flask import Flask, request

COMPUTES_FILE = "computes.md"

computes = {}

app = Flask(__name__)

def load_computes():
  global computes
  computes = {}
  if os.path.isfile(COMPUTES_FILE):
    with open(COMPUTES_FILE, "r") as f:
      for line in f.readlines():
        compute, ip, _ = line.strip().split(" ")
        computes[compute] = {"ip": ip, "uptime": 100}

def save_computes():
  with open(COMPUTES_FILE, "w") as f:
    for name, data in computes.items():
      ip, uptime = data["ip"], data["uptime"]
      f.write(f"{name} {ip} {uptime}\n")

def ping(ip):
  response = os.system(f"ping 1 {ip}")
  return response == 0

@app.route("/ping", methods=["POST"])
def receive_ping():
  ip = request.form["ip"]
  if ping(ip):
    return "OK"
  else:
    return "DOWN", 400

def update_uptimes():
  global computes
  for name, data in computes.items():
    ip = data["ip"]
    uptime = 100 if ping(ip) else 0
    computes[name]["uptime"] = uptime
  threading.Timer(10, update_uptimes).start()

def main():
  load_computes()
  update_uptimes()

while True:
    print("\n\nGemini Status")
    print(" ")
    print(" ")
    print("[1] Create a new compute to track")
    print("[2] Remove a compute")
    print("[3] List computes")
    print(" ")
    print(" ")
    print("Note: You are hosting a Flask app because this will make your computer accept the pings from the other computer if this computer is the host compute")

    choice = input("> ")

    if choice == "1":
      compute = input("Compute name: ")
      ip = input("IP address: ")
      computes[compute] = {"ip": ip, "uptime": 100}
      save_computes()
    elif choice == "2":
      compute = input("Compute name: ")
      if compute in computes:
        del computes[compute]
        save_computes()
    elif choice == "3":
      print("\nGemini Status")
      print("Computes:")
      for name, data in computes.items():
        ip, uptime = data["ip"], data["uptime"]
        print(f"- {name} [{ip}] [Uptime: {uptime}%]")
      print("\nPress p to exit the list and go to main menu")
      
      while True:
        choice = input("> ")
        if choice == "p":
          break
      
    else:
      print("Invalid choice.")

if __name__ == "__main__":
  main()
