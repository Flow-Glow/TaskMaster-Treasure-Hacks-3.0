# Path: Modules\Utils.py
import os
import pyrebase

# --- Paths ---
ModulesPath = os.path.dirname(os.path.abspath(__file__))
AssetsPath = os.path.join(ModulesPath, "Assets")


class fb:
    def __init__(self, config):
        self.firebase = pyrebase.initialize_app(config)
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









