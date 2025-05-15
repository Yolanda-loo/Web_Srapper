Web Scraper App
A simple web scraper application built with Python, BeautifulSoup, and Tkinter. This app allows users to scrape article titles and links from a specified website and display them in a structured, scrollable table through a graphical user interface.
Features

Scrape article titles and URLs from a user-provided website
Display results in a structured table with scrollable view
User-friendly GUI with error handling for invalid URLs or network issues
Simple and intuitive design
Customizable for different website structures (with minor code adjustments)

Prerequisites
To run this application, you need:

Python 3.x installed on your system
Required Python libraries: requests, beautifulsoup4
Tkinter (usually included with Python standard library)

Installation

Clone the repository to your local machine:
git clone https://gitlab.com/Yolanda-loo/web-scraper.git


Navigate to the project directory:
cd web-scraper


Ensure Python is installed:
python --version


Install the required Python libraries:
pip install requests beautifulsoup4



Usage

Run the application:
python web_scraper.py


The app window will open, allowing you to:

Enter a website URL (e.g., https://www.npr.org/) in the input field
Click "Scrape Website" to fetch article titles and links
View results in a scrollable table with columns for "Article Title" and "Article URL"


Error messages will appear if:

You enter an invalid or empty URL
The website cannot be reached (e.g., network issues)
No articles are found on the page



Project Structure
│
├── web_scraper.py  # Main application code
├── README.md       # Project documentation

Contributing
Contributions are welcome! Please follow these steps:

Fork the repository
Create a new branch (git checkout -b feature-branch)
Make your changes
Commit your changes (git commit -m 'Add new feature')
Push to the branch (git push origin feature-branch)
Open a Pull Request

License
This project is licensed under the MIT License - see the LICENSE file for details.
Contact
For any questions or suggestions, feel free to open an issue or contact me at londie970918@gmail.com.
