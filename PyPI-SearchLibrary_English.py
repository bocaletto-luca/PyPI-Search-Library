# Software Name: PyPI Search Library
# Author: Luca Bocaletto

import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QListWidget, QListWidgetItem

class PyPIBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyPI Search Library")  # Set the window title
        self.setGeometry(100, 100, 800, 600)  # Set the window's position and dimensions

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)  # Set the central widget for the window

        self.layout = QVBoxLayout()  # Create a vertical layout
        self.central_widget.setLayout(self.layout)  # Set the layout as the central layout

        self.search_input = QLineEdit(self)  # Create an input field for searching
        self.search_input.setPlaceholderText("Search for libraries on PyPI")  # Set a placeholder text
        self.layout.addWidget(self.search_input)  # Add the input field to the layout

        self.search_button = QPushButton("Search", self)  # Create a search button
        self.layout.addWidget(self.search_button)  # Add the search button to the layout

        self.result_list = QListWidget(self)  # Create a list widget for displaying results
        self.layout.addWidget(self.result_list)  # Add the list widget to the layout

        self.search_button.clicked.connect(self.search_pypi)  # Connect the button click to the search_pypi function

    def search_pypi(self):
        query = self.search_input.text()  # Get the text entered by the user
        if query:
            self.result_list.clear()  # Clear previous results from the list
            url = f"https://pypi.org/simple/{query}/"  # Build the URL for searching on PyPI
            response = requests.get(url)  # Make an HTTP request to get data
            if response.status_code == 200:  # Check if the request was successful
                data = response.text  # Get data from the response
                package_names = self.extract_package_names(data)  # Extract package names
                for package_name in package_names:
                    item = QListWidgetItem(package_name)  # Create an item for the list
                    self.result_list.addItem(item)  # Add the item to the list

    def extract_package_names(self, data):
        package_names = data.split('\n')  # Split the data into lines to get package names
        return package_names

def main():
    app = QApplication(sys.argv)  # Create a Qt application
    window = PyPIBrowser()  # Create the main window
    window.show()  # Show the window
    sys.exit(app.exec_())  # Run the application

if __name__ == "__main__":
    main()  # Start the application when the module is run
