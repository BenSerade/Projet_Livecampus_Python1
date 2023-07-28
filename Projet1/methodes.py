import requests
from pprint import pprint

class GeoApi:
    def get_population_departement(self, code_departement):
        self.base_url = 'https://geo.api.gouv.fr'  # URL de base de l'API "geo.api.gouv.fr"
        # Construire l'URL pour obtenir les informations du département
        url = f'{self.base_url}/departements/{code_departement}/communes'
        response = requests.get(url)
        if not response.ok:
            print(f"Impossible d'obtenir les informations pour le département {code_departement}.")
            return []
        data = response.json()
        # Créer une liste pour stocker les populations des communes du département
        populations = []

        # Parcourir les données JSON et récupérer les populations des communes
        for commune in data:
            population = commune.get('population', None)
            if population is not None:
                populations.append(population)
        return populations

        
    
        

        
        

