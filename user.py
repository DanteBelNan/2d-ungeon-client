from client import client

class user(client):

    def get_all(self):
        users_found = self._get(
            path="/users",
            )

        if users_found is not None:
            return users_found
        else:
            raise Exception(f"No users found.")
        
    def get_by_username(self,username):
        user_found = self._get(
            path=f"/users/{username}",
            body=username
            )

        if user_found is not None:
            return user_found
        else:
            raise Exception(f"Username {username} not found.")