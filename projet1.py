import requests, os, pathlib, csv, json
from typing import Any
from Projet1.methodes import GeoApi


def main():
    geo_api = GeoApi()
    code_departement = input("Veuillez entrer votre département : ")
    populations_communes = geo_api.get_population_departement(code_departement)

    somme_population = sum(populations_communes)
    print("Populations des communes :", populations_communes)
    print("Somme de la population :", somme_population)

if __name__ == "__main__":
    main()