# import django libraries/module/packages/settings
from Onefin_project.settings import retry_count, movie_url, movie_url_username, movie_url_pswd

# import non django module/packages 
import requests
from requests.auth import HTTPBasicAuth

class Api_call:
    @staticmethod 
    def api_call():
        for _ in range(retry_count):
            try:
                movies_response = requests.get(movie_url, verify = False)
                return movies_response
            except Exception as e:
                
                continue 
        return {
            "message":f"Request tried {retry_count} times. Please try after some time"
            }
