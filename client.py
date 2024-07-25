import requests
import os


class client:

    def __init__(
            self,
            project_url="http://localhost:3000",
            auth_token= None
    ):
        self._project_url = project_url

        self._headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {auth_token}" if auth_token else ''
        }
    
    def _post(self,path,body=None) -> dict:
        try:
            response = requests.post(
                self._project_url,
                json={"query" : body},
                headers=self._headers
            )

            if response.status_code != 200:
                raise Exception(f"Error {response.status_code}. Msg: {response.json()["errors"][0]["message"]}")
            else:
                return response.json()
        except requests.ConnectionError:
            raise Exception(f"Error with the network, can't connect to {self._project_url}")
        
    def _get(self,path,body=None) -> dict:
        try:
            response = requests.get(
                f"{self._project_url}{path}",
                json={"query" : body},
                headers=self._headers
            )
            if response.status_code != 200:
                raise Exception(f"Error {response.status_code}. Msg: {response.json()["errors"][0]["message"]}")
            else:
                return response.json()
        except requests.ConnectionError:
            raise Exception(f"Error with the network, can't connect to {self._project_url}")


