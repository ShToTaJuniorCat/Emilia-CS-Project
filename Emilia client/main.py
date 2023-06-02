from datetime import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from json import loads
from constants import spotify_const, stt_const, input_const, configurations
from speech_recognition import get_input
from re import sub
from os import startfile, system


sp = spotipy.Spotify(
   auth_manager=SpotifyOAuth(scope=spotify_const.SCOPE,
                             client_id=spotify_const.CLIENT_ID,
                             client_secret=spotify_const.CLIENT_SECRET,
                             redirect_uri=spotify_const.REDIRECT_URI)
)


def get_time(args):
   current_time = datetime.now().strftime("%I:%M %p")

   return f"Now is {current_time}"


def search(args):
   return "Sorry, but this function isn't currently working."

   webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open(f"https://www.google.com/search?q={args[0]}")
   return "Search window opened."


def start_app(args):
    apps = configurations.SETTINGS["apps"]
    app_list = apps.replace("\n", " - ").split(" - ")
    app_dict = dict(zip([x.lower() for x in app_list[::2]], app_list[1::2]))

    if args not in app_dict.keys():
        return f"Sorry, I can't find app named {args}."

    path = app_dict[args]
    startfile(path)
    return f"Sure, opening {args}"


def stop_app(args):
    return "Sorry, this option is not available at the moment."

    apps = configurations.SETTINGS["apps"]
    app_list = apps.replace("\n", " - ").split(" - ")
    app_dict = dict(zip([x.lower() for x in app_list[::2]], app_list[1::2]))

    if args not in app_dict.keys():
        return f"Sorry, I can't find app named {args}."

    path = app_dict[args]
    system(f"taskkill /im {path}")
    return f"Sure, closing {args}"


def is_playing():
   return sp.currently_playing()['is_playing']


def pause_music(args):
   if is_playing():
       sp.pause_playback()

   return f"Music is now paused."


def play_music(args):
   if not is_playing():
       sp.start_playback()

   return f"Music is now playing."


def next_track(args):
   sp.next_track()
   return "Sure."


def previous_track(args):
   sp.previous_track()
   return "Sure."


def get_uri(name, search_type):
   return sp.search(name, 1, type=search_type)[search_type + "s"]["items"][0]["uri"]


def play_track_by_name(args):
   sp.start_playback(uris=[get_uri(args.lower(), "track")])
   return "Enjoy!"


def queue(args):
   sp.add_to_queue(uri=get_uri(args.lower(), "track"))
   return "Enjoy!"


def shuffle(args):
   sp.shuffle(args == "on")
   return f"Shuffle is now {args == 'on'}."


def command_to_function(command):
   translator = {
       "get-time": get_time,
       # "search": search,
       "open": start_app,
       "close": stop_app,
       "pause-music": pause_music,
       "resume-music": play_music,
       "next": next_track,
       "previous": previous_track,
       "play": play_track_by_name,
       "shuffle": shuffle,
       "queue": queue
   }

   try:
       return translator[command]
   except KeyError:
       return lambda args: f"Unknown command: {command}."


def text_to_command(text):
   if text in input_const.DICTIONARY.keys():
       return input_const.DICTIONARY[text]
   else:
       """
       Of the defined commands, the ones that'll end up here are:
       * play [track name]
       * queue [track name]
       * search [search query]
       * open [app name]
       * close [app name]

       They keyword is the first word in the command.
       For keywords "play", "queue", "search", "open", "close":
        - The command is just the input text.
        - Examples:
         ~ "play back from the dead" - command "play" with argument "back from the dead".
         ~ "queue back from the dead" - command "queue" with argument "back from the dead".
         ~ "search what is life" - command "search" with argument "what is life".
         ~ "open spotify" - command "open", with argument "spotify".
         ~ "close spotify" - command "close", with argument "spotify".

       Anything else is not defined, therefore raise an error.
       """

       keyword = text.split(" ")[0]
       if keyword in ["play", "queue", "search", "open", "close"]:
           return text

       raise ValueError(f"Unknown command: {keyword}")


def start_user_input(recorder):
    inp = get_input(recorder)

    if inp == None:
        return

    inp = sub(r"[^\w\s]", "", inp.lower()).strip()

    try:
        inp = text_to_command(inp).split(" ")
       
        cmd = inp[0]

        args = None

        if len(inp) > 1:
            args = " ".join(inp[1:])

        response = command_to_function(cmd)(args)
      
        return response

    except ValueError as e:
        return e


# TODO: Fix bug where if no device is playing, the app crashes.
# ?FIX: Play music on the latest used device
# print(sp.devices())
