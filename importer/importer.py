import requests
from bs4 import BeautifulSoup
import queue
from threading import Thread
import time
import random

class Crawler:

    visited_urls = []
    urls = queue.PriorityQueue()
    workers = 0
    i = 0

    def __init__(self, base_url):
        super().__init__()
        self.urls.put((0.5, base_url))

    def crawl(self):
        worker_id = self.i
        self.i = self.i + 1
        print(f"Worker init {worker_id}")
        while not self.urls.empty():
            time.sleep(random.uniform(1, 3))
            # ignore the priority value
            _, current_url = self.urls.get()
            self.visited_urls.append(current_url)
            print(f"Page [{worker_id}] {self.urls._qsize()}, {len(self.visited_urls)}: {current_url}")

            # crawling logic
            response = requests.get(current_url)
            try:
                soup = BeautifulSoup(response.content, "html.parser")

                link_elements = soup.select("a[href]")
                for link_element in link_elements:
                    url = link_element['href']
                    if url.startswith(base_url):
                        if url not in self.visited_urls and url not in [item[1] for item in self.urls.queue]:
                            # default priority score
                            priority_score = 1
                            self.urls.put((priority_score, url))
            except Exception as e:
                print(f"Error [{current_url}]: {e}")
            finally:
                if self.workers < 2 and self.urls.not_empty:
                    self.create_worker()
        print(f"Worker done {worker_id}")
        self.workers = self.workers - 1

    def create_worker(self):
        Thread(target=self.crawl, daemon=True).start()
        self.workers = self.workers+1

    def start(self):
        self.create_worker()
        self.urls.join()

base_url = "https://kobietazesmakiem.pl/"

# Thread(target=queue_worker, args=(len(workers), urls, visited_urls, workers), daemon=True).start()

print("Start")
# urls.join()
crawler=Crawler(base_url)
crawler.start()
print(f"Visited urls: {crawler.visited_urls}")
print(f"Left urls   : {crawler.urls}")
