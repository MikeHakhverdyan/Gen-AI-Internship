from Download import ThreadingDownloader
import threading
import multiprocessing


class Download_manager:

    def __init__(self, max_thread, max_process):
        self.__max_thread = max_thread
        self.__max_process = max_process
        self.__downloads = []

    @property
    def max_thread(self):
        return self.__max_thread

    @property
    def max_process(self):
        return self.__max_process

    @property
    def downloads(self):
        return self.__downloads

    def download(self, url, filename):
        download = ThreadingDownloader(url, filename)  # Could be changed to MultiProcess
        self.downloads.append(download)

    def start(self):
        num_threads = min(self.max_thread, len(self.downloads))
        num_processes = min(self.max_process, len(self.downloads))

        thread_pool = []
        process_pool = []

        for _ in range(num_threads):
            if self.downloads:
                download = self.downloads.pop()
                thread = threading.Thread(target=download.start_download)
                thread_pool.append(thread)
                thread.start()

        # for _ in range(num_processes):
        #     if self.downloads:
        #         download = self.downloads.pop()
        #         process = multiprocessing.Process(target=download.start_download)
        #         process_pool.append(process)
        #         process.start()

        for thread in thread_pool:
            thread.join()

        for process in process_pool:
            process.join()

    def wait(self):
        for download in self.downloads:
            download.start_download()
