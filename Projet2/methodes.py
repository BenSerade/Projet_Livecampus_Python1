import os
import psutil
import platform
import socket
import subprocess
import pathlib
import json
import shutil
import pandas as pd

class info_os:

    # Fonction pour obtenir les informations sur le système d'exploitation (OS)
    def get_os_info():
        return platform.system(), platform.release()

    # Fonction pour obtenir les informations sur le processeur (CPU)
    def get_cpu_info():
        return platform.processor()

    # Fonction pour obtenir les informations sur la mémoire RAM
    def get_ram_info():
        return f"{psutil.virtual_memory().total / (1024**3):.2f} GB"

    # Fonction pour obtenir les 5 processus les plus gourmands en mémoire
    def get_top_processes(num_processes=5):
        processes = [(p.pid, p.name(), p.memory_info().rss) for p in psutil.process_iter(['pid', 'name', 'memory_info'])]
        processes.sort(key=lambda x: x[2], reverse=True)
        return processes[:num_processes]

    # Fonction pour obtenir les variables d'environnement du système
    def get_environment_variables():
        return os.environ

    # Fonction pour obtenir les partitions de disque
    def get_disk_partitions():
        return psutil.disk_partitions()

    # Fonction pour obtenir l'utilisation de l'espace disque pour une partition donnée
    def get_disk_usage(partition):
        return psutil.disk_usage(partition.mountpoint)

    # Fonction pour obtenir les interfaces réseau
    def get_network_interfaces():
        return psutil.net_if_addrs()

    # Fonction pour obtenir le temps de démarrage du système
    def get_boot_time():
        return psutil.boot_time()

    # Fonction pour formater le temps de démarrage au format "heures:minutes:secondes"
    def format_boot_time(timestamp):
        from datetime import datetime
        boot_time = datetime.fromtimestamp(timestamp)
        return boot_time.strftime("%H:%M:%S")
    
class info:
    

    def ouvrir_json():

        root_file = pathlib.Path(__file__).parent.resolve()
        file_path = os.path.join(root_file, "ntt.json")
        file_excel = os.path.join(root_file, "data.xlsx")

        with open(file_path, "r") as mon_fichier:
            data = json.load(mon_fichier)

        ma_liste_a_parcourir = data["hits"]["hits"]
        resultats = []

        for item in ma_liste_a_parcourir:
            log_level = item["_source"]["log"]["level"]            

            if log_level == "warning" or log_level == "error":
                
                messages = item["_source"]["message"]
                station = item["_source"]["host"]["name"]
                
                resultats.append({"Niveau":log_level,"Message": messages, "Station": station})

                df = pd.DataFrame(resultats)

                error_df = df[df["Niveau"] == "error"]
                autres_niveau_df = df[df["Niveau"] != "error"].sort_values(by="Niveau")

                df = pd.concat([error_df, autres_niveau_df])
                df = df.reset_index(drop=True)

        df.to_excel(file_excel, index=False, engine='openpyxl')

                # print(log_level)
                               
                # print(messages)
                # print(station)
                # print("-" * 100)
            

    
info.ouvrir_json()



