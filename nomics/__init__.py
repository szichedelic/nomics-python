import json
import requests

class Nomics:
    def __init__(self, key):
        self.key = key
    
    def get_url(self, endpoint):
        return "https://api.nomics.com/v1/{}?key={}".format(endpoint, self.key)