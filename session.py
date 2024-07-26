from client import client

class session(client):

    def login(self,credentials):
        login = self._get(
            path="/session/login",
            body=credentials
            )

        if login is not None:
            return login
        else:
            raise Exception(f"Error logging in.")
        