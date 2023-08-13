import bs4, requests


def prepare_site(url):
    respons = requests.get(url)
    soup = bs4.BeautifulSoup(respons.text, "lxml")
    return soup


url = "https://google.com"
site = prepare_site(url)