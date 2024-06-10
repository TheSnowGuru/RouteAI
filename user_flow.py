import sys

def main():
    # Print the command prompt in green
    print("\033[92mrouteai\033[0m")
    
    # Prompt the user to enter a URL
    url = input("Please enter a URL: ")
    
    # Print the entered URL
    print(f"Entered URL: {url}")

if __name__ == "__main__":
    main()
