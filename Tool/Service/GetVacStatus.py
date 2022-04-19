import Tool.Data.ModuleJSON as ModuleJSON
import requests, bs4

def IsBlock():
    Link = ModuleJSON.ReadConfig("VAC")["Account"]

    Response = requests.get(Link, verify = True)
    Site = bs4.BeautifulSoup(Response.text, "lxml").html

    if (Site.find_all("div", class_ = "profile_ban")):
        return True

    else:
        return False