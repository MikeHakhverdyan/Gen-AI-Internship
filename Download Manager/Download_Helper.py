import requests


def download(url: str):

    # if url.startswith('ftp') or url.startswith('http'):
    #     try:
    file = requests.get(url)
    return file.content
        # except:
        #     return 'Invalid URL'
