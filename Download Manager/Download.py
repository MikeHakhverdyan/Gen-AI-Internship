from Download_Helper import download


class Download:
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename

    def start_download(self):
        raise NotImplementedError("start_download method must be implemented in the subclasses.")

    def save_file(self, content):
        with open(self.filename, "wb") as file:
            file.write(content)

    def download_complete(self):
        print(f"Download from {self.url} completed.")


class ThreadingDownloader(Download):
    def start_download(self):
        content = download(self.url)
        self.save_file(content)
        self.download_complete()


class MultiprocessingDownloader(Download):
    def start_download(self):
        content = download(self.url)
        self.save_file(content)
        self.download_complete()

# class ThreadingDownloader(Download):
#     def return_value(self, url, q):
#         res = download(url)
#         q.put(res)
#
#     def start_download(self, downloads):
#         for site in downloads:
#             t = threading.Thread(target=self.return_value, args=(site, self.q))
#             t.start
