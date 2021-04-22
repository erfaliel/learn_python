"""
As user.py, designed your class post to interact with main.py.
A good way is to create one file for one clas…
"""

class Post:
    def __init__(self, message, author):
        self.message = message
        self.author = author

    def get_post_info(self):
        print(f"Post : {self.message} written by {self.author}.")

