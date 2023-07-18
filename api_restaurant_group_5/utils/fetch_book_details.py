import requests


def fetch_book_details(book_id):
    google_books_api = f"https://www.googleapis.com/books/v1/volumes/{book_id}"
    response = requests.get(google_books_api)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
