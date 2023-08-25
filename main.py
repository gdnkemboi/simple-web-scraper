from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import mechanicalsoup

url = str(input('Enter the URL:'))

def main(url):
    browser = mechanicalsoup.Browser()
    login_page = browser.get(url)
    login_html = login_page.soup

    form = login_html.select("form")[0]
    form.select("input")[0]["value"] = "zeus"
    form.select("input")[1]["value"] = "ThunderDude"

    profiles_page = browser.submit(form, login_page.url)
    profiles_html = profiles_page.soup
    title = profiles_html.title.string
    print(f"Title: {title}")
    parsed_url = urlparse(profiles_page.url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    links = profiles_page.soup.select("a")
    for link in links:
        address = link.get("href")
        text = link.text
        print(f"{text}: {base_url}{address}")


if __name__ == "__main__":
    main(url)