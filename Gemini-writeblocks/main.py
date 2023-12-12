import os
import random

def clear_cmd():
    if os.name == 'nt': 
        _ = os.system('cls')
    else:   
        _ = os.system('clear')

clear_cmd()

def create_cpu():
    cpu_name = input("Enter the name of the CPU: ")
    cpu_cores = int(input("Enter the number of CPU cores: "))
    cpu_ghz = float(input("Enter the GHz of the CPU: "))
    cpu = {
        "Name": cpu_name,
        "Type": "CPU",
        "Ghz": cpu_ghz,
        "Cores": cpu_cores
    }
    return cpu

def create_ram():
    ram_name = input("Enter the name of the RAM: ")
    ram_mhz = int(input("Enter the MHz of the RAM: "))
    ram_size = int(input("Enter the size of the RAM (in GB): "))
    ram = {
        "Name": ram_name,
        "Type": "RAM",
        "Mhz": ram_mhz,
        "Size": ram_size
    }
    return ram

def create_disk():
    disk_name = input("Enter the name of the disk: ")
    disk_type = input("Enter the type of disk (SSD or HDD): ")
    disk_size = int(input("Enter the size of the disk (in PB): "))
    disk = {
        "Name": disk_name,
        "Type of Disk": disk_type,
        "Type": "Disk",
        "Size": disk_size
    }
    return disk

def create_gpu():
    gpu_name = input("Enter the name of the GPU: ")
    gpu_vram = int(input("Enter the VRAM of the GPU (in TB): "))
    gpu = {
        "Name": gpu_name,
        "Type": "GPU",
        "VRAM": gpu_vram
    }
    return gpu

def create_hardware(folder_name, hardware):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    random_number = random.randint(100000, 999999)
    file_name = f"{hardware['Name']}{random_number}.txt"
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, "w") as file:
        file.write(f"Name: {hardware['Name']}\n")
        for key, value in hardware.items():
            if key != "Name":
                file.write(f"{key}: {value}\n")
    print(f"{hardware['Name']} created successfully!")

def main():
    while True:
        print("\nGemini WriteBlocks\n")
        print("[1] Create a Processor (Max 1024Ghz 1024 cores)")
        print("[2] Create RAM (Max 1024GB RAM)")
        print("[3] Create Disk [Max 1024PB]")
        print("[4] Create GPU [Max 1024TB VRAM]")
        print("[5] Quit")
        choice = input("\nSelect an option: ")
        if choice == "1":
            cpu = create_cpu()
            create_hardware("CPUs", cpu)
        elif choice == "2":
            ram = create_ram()
            create_hardware("RAM", ram)
        elif choice == "3":
            disk = create_disk()
            create_hardware("Disk", disk)
        elif choice == "4":
            gpu = create_gpu()
            create_hardware("GPUs", gpu)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()