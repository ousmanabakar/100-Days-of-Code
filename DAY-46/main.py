from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
ClientID = "27e993d052d149478fb9d4ca08173765"
ClientSecret = "6f2f3fca8eb340eaa0ba1aae0419097d"
scope = "playlist-modify-private"
redirect_uri = "http://example.com"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(url="https://www.billboard.com/charts/hot-100/"+date)
soup = BeautifulSoup(response.text, "html.parser")

song_title = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
song_list = [song.getText() for song in song_title]
# for title in song_title:
#     text = title.getText()
#     song_list.append(text)2019
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=ClientID, client_secret=ClientSecret, redirect_uri=redirect_uri,
                                               scope=scope, show_dialog=True, cache_path="token.txt",))

user_id = sp.current_user()["id"]
print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"The 100 Hot Billboard of {date}", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
