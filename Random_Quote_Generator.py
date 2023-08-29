# Import the requests library
import requests

# Function to get a random quote from the API
def get_random_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        data = response.json()
        return data["content"], data["author"]
    else:
        return "No quote found", "Unknown"

# Function to print the quote
def quote():
    # Wait for user input to continue
    input("Press Enter To Continue")
    # Print header for the quote
    print(" "*10, end="")
    print("Quote Of The Day")
    print("*" * 40)
    # Get and print a random quote
    quote, author = get_random_quote()
    print(f'"{quote}" - {author}')

# Main program
if __name__ == "__main__":
    # Call the quote function to display a random quote
    quote()
