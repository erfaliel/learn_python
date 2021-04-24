import requests

response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
print(response.json())          # convert json response into a list
print(type(response.json()))    # You can check here
print(f"First element is {response.json()[0]}")    # You can print first element like that
print(type(response.json()[0]))   # each element is a Dictionnary.
projects = response.json()

for project in projects:
    print(f"Project Name: {project['name']}\nProject Url: {project['web_url']}\n")

def pop_poject_item(project):
    return f"Project Name: {project['name']}\nProject Url: {project['web_url']}\n"

result = map(pop_poject_item, projects)
print("result is :\n", result)
print(set(result))