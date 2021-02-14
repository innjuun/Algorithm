import os
import requests
from bs4 import BeautifulSoup


def crawler(url):
    py_files = []
    try:
        html = requests.get(url).text
    except:
        return
    soup = BeautifulSoup(html, "html.parser")
    select = soup.body.select(".css-truncate > .js-navigation-open")
    repositories = []
    for a in select:
        link = a.attrs.get("href")
        if link.endswith(".py"):
            py_files.append(link)
        else:
            repositories.append(a.attrs.get("href"))

    with open("README.md", "a") as f:

        current_directory = url.split("innjuun/")[-1]
        position = requests.utils.unquote(current_directory).split('master')[-1]
        f.write("### " + position + "\n")
        for link in py_files:
            unquoted_filename = requests.utils.unquote(
                os.path.splitext(link.split("/")[-1])[0]
            )
            f.write("+ [" + unquoted_filename + "]")
            f.write("(https://github.com/" + link + ")\n")
        f.close()

    for repo in repositories:
        if repo:
            crawler("https://github.com/" + repo)


if __name__ == "__main__":
    if os.path.isfile("README.md"):
        os.remove("README.md")
    with open("README.md", "a") as f:
        f.write(
            "# Algorithm study repository.\n## This README file made automatically by crawler\n"
        )
    crawler("https://github.com/innjuun/Algorithm")
