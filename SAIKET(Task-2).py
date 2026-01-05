import requests

# Public Joke API URL
url = "https://official-joke-api.appspot.com/jokes/programming/ten"

# Fetch data from API
response = requests.get(url)

# Check if request is successful
if response.status_code == 200:
    data = response.json()

    print("Programming Jokes\n")

    # Display first 5 jokes
    for i in range(5):
        print("Joke", i + 1)
        print("Setup:", data[i]["setup"])
        print("Punchline:", data[i]["punchline"])
        print("-" * 40)

else:
    print("Failed to fetch data from API")
