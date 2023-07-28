import os
import psutil
import platform
import socket
import subprocess
from Projet2.methodes import info_os

def main():

    # Obtenir les informations sur le système d'exploitation
    os_info = info_os.get_os_info()

    # Obtenir les informations sur le processeur (CPU)
    cpu_info = info_os.get_cpu_info()

    # Obtenir les informations sur la mémoire RAM
    ram_info = info_os.get_ram_info()

    # Obtenir les 5 processus les plus gourmands en mémoire
    top_processes = info_os.get_top_processes()

    # Obtenir les variables d'environnement du système
    environment_variables = info_os.get_environment_variables()

    # Obtenir les partitions de disque
    disk_partitions = info_os.get_disk_partitions()

    print("OS:", os_info)
    print("CPU:", cpu_info)
    print("RAM:", ram_info)

    print("\nTop processes (PID, Name, Memory Usage):")
    for pid, name, mem_usage in top_processes:
        print(f"{pid}, {name}, {mem_usage / (1024**2):.2f} MB")

    print("\nEnvironment Variables:")
    for key, value in environment_variables.items():
        print(f"{key}={value}")

    print("\nDisk Partitions and Usage:")
    for partition in disk_partitions:
        usage = info_os.get_disk_usage(partition)
        print(f"{partition.device} ({partition.mountpoint}): Total={usage.total / (1024**3):.2f} GB, Free={usage.free / (1024**3):.2f} GB")

    # Obtenir les interfaces réseau
    network_interfaces = info_os.get_network_interfaces()
    print("\nNetwork Interfaces:")
    for interface, addresses in network_interfaces.items():
        for address in addresses:
            print(f"{interface}: {address.family.name} - {address.address}")

    # Obtenir le temps de démarrage du système
    boot_time = info_os.get_boot_time()
    formatted_boot_time = info_os.format_boot_time(boot_time)
    print("\nBoot Time:", formatted_boot_time)

if __name__ == "__main__":
    main()