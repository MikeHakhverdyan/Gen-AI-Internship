from Download_Manager import Download_manager


manager = Download_manager(max_thread=2, max_process=2)

manager.download("https://www.instagram.com/", "ig.txt")
manager.download("https://www.fb.com/", "fb.txt")
manager.download("https://www.vk.com/", "vk.txt")

manager.start()
manager.wait()