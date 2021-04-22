from user import User # import User Class
from post import Post

app_user_one = User("nn@nn.com", "Nana Janashia", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()
app_user_one.change_job_title("DevOps Trainer")
app_user_one.get_user_info()
print(app_user_one)  # use __repr__ method : very usefull for debug.

app_user_two = User("secret@mm.com", "James Bond", "007", "Secret Agent")
app_user_two.get_user_info()

new_post = Post("On a secret mission today", app_user_two.name)
new_post.get_post_info()

