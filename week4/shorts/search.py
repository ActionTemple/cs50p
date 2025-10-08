
import requests


def main():
    artwork = input("Artwork: ")
    artworks = get_artworks(query=artwork, limit=3)
    for artwork in artworks:
        print(f"* {artwork}")

def get_artworks(query, limit):
    try:
        response = requests.get(
             "http://api.artic.edu/api/v1/artworks/search",


        )


main()
