from locust import HttpUser, TaskSet, task


class SearchTasks(TaskSet):
    @task(1)
    def simple_search(self):
        self.client.get("/arama?q=telefon")

    @task(1)
    def suggestion_search(self):
        self.client.get("/arama?q=kitap")

    @task(1)
    def filter_search(self):
        self.client.get("/arama?q=laptop&filter=price:1000-2000")

    @task(1)
    def empty_search(self):
        self.client.get("/arama?q=")


class WebsiteUser(HttpUser):
    tasks = [SearchTasks]
    min_wait = 1000
    max_wait = 2000