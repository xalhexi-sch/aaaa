class Browser:
    def __init__(self):
        self.history = []  # Stack to store visited pages
        self.current_page = None  # To store the current page URL

    def visit(self, url):
        """Simulates visiting a new URL.
       
        The current page should be pushed to the history stack,
        and the current page is updated to the new URL.
        """
        # If the current page is not None, push it onto the history stack
        if self.current_page is not None:
            self.history.append(self.current_page)
       
        # Update the current page to the new URL
        self.current_page = url
       
        # Print the current page after visiting
        print(self.current_page)

    def go_back(self):
        """Simulates clicking the back button.
       
        The most recent URL is popped from the history stack and
        becomes the new current page. If the history is empty,
        the current page remains unchanged.
        """
        # Check if the history stack is not empty
        if self.history:
            # Pop the last visited URL and set it as the current page
            self.current_page = self.history.pop()
       
        # Print the current page after going back
        print(self.current_page)

# --- Main execution part of the script (DO NOT MODIFY) ---
browser = Browser()

while True:
    command = input()  # Read the command from user input
   
    if command.startswith("visit "):
        url = command.split(" ", 1)[1]  # Extract the URL
        browser.visit(url)
    elif command == "back":
        browser.go_back()
    elif command == "exit":
        break
