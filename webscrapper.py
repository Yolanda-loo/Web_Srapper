import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk, messagebox
from urllib.parse import urljoin

class WebScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Scraper")
        self.root.geometry("600x400")

        # URL input
        self.url_label = ttk.Label(root, text="Website URL:")
        self.url_label.pack(pady=5)
        self.url_entry = ttk.Entry(root, width=50)
        self.url_entry.insert(0, "https://www.npr.org/")
        self.url_entry.pack(pady=5)

        # Scrape button
        self.scrape_button = ttk.Button(root, text="Scrape Website", command=self.scrape_website)
        self.scrape_button.pack(pady=10)

        # Results display
        self.tree = ttk.Treeview(root, columns=("Title", "Link"), show="headings")
        self.tree.heading("Title", text="Article Title")
        self.tree.heading("Link", text="Article URL")
        self.tree.column("Title", width=300)
        self.tree.column("Link", width=250)
        self.tree.pack(pady=10, fill="both", expand=True)

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")

    def scrape_website(self):
        # Clear previous results
        for item in self.tree.get_children():
            self.tree.delete(item)

        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a valid URL")
            return

        try:
            # Send HTTP request
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            # Parse HTML
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Find article elements (customize based on website structure)
            articles = soup.find_all("article") or soup.find_all("h2") or soup.find_all("div", class_="story")

            if not articles:
                messagebox.showwarning("Warning", "No articles found on the page")
                return

            # Extract titles and links
            for article in articles:
                title_elem = article.find("h2") or article.find("h3") or article.find("a")
                if not title_elem:
                    continue

                title = title_elem.get_text(strip=True)
                link_elem = article.find("a", href=True)
                link = urljoin(url, link_elem["href"]) if link_elem else "No link available"

                if title:
                    self.tree.insert("", "end", values=(title, link))

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to scrape website: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WebScraperApp(root)
    root.mainloop()
