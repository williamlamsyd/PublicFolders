import googlemaps
import yaml
import os

# ============= #
# === INPUT === #
# ============= #

# source input 
# include full path to the working directory
dir = os.chdir("path")

# include abspath to the config file that stores the api key
file = os.path.abspath("auth.yaml")

# ----------------------------------------------------------------------------------------------

# ================= #
# === FUNCTIONS === #
# ================= #

# pass credentials and load maps
def load_gmaps():    
    with open(file) as stream:
        config= yaml.safe_load(stream)

    api_key = config['api_key']
    
    gmaps = googlemaps.Client(key=api_key)
    return gmaps


