import spotipy
import os
import spotipy.util as Util
import json
class bot_plugin(object):

    def __init__(self):
        f = open('spotify_creds.json','r')
        creds = json.loads(f.read())
        f.close()
        os.environ['SPOTIPY_CLIENT_ID'] = creds['SPOTIPY_CLIENT_ID']
        os.environ['SPOTIPY_CLIENT_SECRET'] = creds['SPOTIPY_CLIENT_SECRET']
        os.environ['SPOTIPY_REDIRECT_URI'] = creds['SPOTIPY_REDIRECT_URI']

        self.token = Util.prompt_for_user_token(username='jay101pk', scope='user-library-read')
        self.spotify = spotipy.Spotify(auth=self.token)
        

    def get_playlist(self, playlist, username=None):
        if username is None:
            username = self.spotify.current_user()['id']
        
        playlists = self.spotify.user_playlists(username)['items']
        for p in playlists:
            if p == playlist:
                break
        tracks_temp = self.spotify.user_playlist_tracks(username, p['id'])
        tracks_final= []
        for track in tracks_temp['items']:
            track = track['track']
            track_temp = ''
            for artist in track['artists']:
                track_temp += artist['name'] + ' '
            tracks_final.append(track_temp + track['name'])
        return tracks_final

    
        



# print(results.keys())
bot = bot_plugin()
sp = bot.spotify

print(bot.get_playlist('My Shazam Tracks','jay101pk'))
        