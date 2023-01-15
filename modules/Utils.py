# Path: Modules\Utils.py
import os
import pyrebase

# --- Paths ---
ModulesPath = os.path.dirname(os.path.abspath(__file__))
AssetsPath = os.path.join(ModulesPath, "Assets")


class fb:
    def __init__(self):
        self.firebase = pyrebase.initialize_app({
            "apiKey": "AIzaSyDkiJYNGsRnSlVAd1eQ5Am8IWYgUgsdgBo",
            "authDomain": "taskmaster-992bc.firebaseapp.com",
            "projectId": "taskmaster-992bc",
            "storageBucket": "taskmaster-992bc.appspot.com",
            "messagingSenderId": "309035351282",
            "appId": "1:309035351282:web:d7e157294b37453e4ea46b",
            "measurementId": "G-CK5YXPBD98",
            "databaseURL": "https://taskmaster-992bc-default-rtdb.firebaseio.com/"
        }
        )
        self.db = self.firebase.database()

    def get_data(self, path):
        """Get data from the specified path in the database."""
        return self.db.child(path).get().val()

    def set_data(self, path, data):
        """Set data at the specified path in the database."""
        self.db.child(path).set(data)

    def update_data(self, path, data):
        """Update data at the specified path in the database."""
        self.db.child(path).update(data)

    def delete_data(self, path):
        """Delete data at the specified path in the database."""
        self.db.child(path).remove()

    def check_exist(self, path):
        """Check if path exists at the specified path in the database."""
        return self.db.child(path).get().val() is not None

    def get_all_data(self, path):
        """Get all data from the specified path in the database."""
        return self.db.child(path).get().val()

    def add_data(self, path, data):
        """Add data to the specified path in the database."""
        self.db.child(path).push(data)

    def clear_database(self):
        """Clear the database."""
        self.db.remove()
