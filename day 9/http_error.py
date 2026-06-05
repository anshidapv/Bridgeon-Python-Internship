class HTTPError(Exception):
    def __init__(self, status_code):
        self.status_code = status_code
        super().__init__(f"HTTP Error {status_code}")
def get_or_404(collection: dict, id: int):
    if id not in collection:
        raise HTTPError(404)
    return collection[id]
tasks = {
    1: {"title": "Learn Python"},
    2: {"title": "Practice FastAPI"}
}
try:
    task = get_or_404(tasks, 1)
    print("Found:", task)
except HTTPError as e:
    print(e)
try:
    task = get_or_404(tasks, 3)
    print("Found:", task)
except HTTPError as e:
    print(e)