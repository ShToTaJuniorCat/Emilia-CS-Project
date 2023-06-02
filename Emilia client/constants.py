from pyaudio import paInt32

class configurations:
    JSON_FILENAME = "configurations.json"
    VOICE_DICT = {
        "Female": 1,
        "Male": 2
    }
    SPEED_DICT = {
        "Slow": 1,
        "Normal": 2,
        "Fast": 3
    }
    KEY_DICT = {
        "Win + J": 1,
        "Ctrl + Alt + Shift": 2,
        "Ctrl + Win": 3
    }

    KEY_NUM_TO_CODE = {
        1: "<cmd_l>+j",
        2: "<ctrl>+<shift>+<alt>",
        3: "<ctrl>+<cmd_l>"
    }

    VOICE_DEFAULT = 1
    SPEED_DEFAULT = 2
    KEY_DEFAULT = 1
    APPS_DEFAULT = r"""Spotify - C:\Users\USER\AppData\Roaming\Spotify\Spotify.exe
Chrome - C:\Program Files\Google\Chrome\Application\chrome.exe
Word - C:\Program Files\Microsoft Office\root\Office16\WINWORD.exe"""

    SETTINGS = {
                'voice': VOICE_DEFAULT,
                'speed': SPEED_DEFAULT,
                'key': KEY_DEFAULT,
                'apps': APPS_DEFAULT
            }

    """
        CALC_SPEED: lambda
        :param s: Speed index. The higher, the faster.
        Returns the speed for the speech, indicated by parameter s.
    """
    CALC_SPEED = lambda s: 80 + 60 * s

class spotify_const:
    # Device IDs of every device used. Might get in handy.
    PHONE_ID = "PHONE_ID"
    LAPTOP_ID = "LAPTOP_ID"
    DESKTOP_ID = "DESKTOP_ID"

    # Literally everything possible to do with spotipy!
    SCOPE = "ugc-image-upload " \
            "user-modify-playback-state " \
            "user-read-playback-state " \
            "user-read-currently-playing " \
            "user-follow-modify " \
            "user-follow-read " \
            "user-read-recently-played " \
            "user-read-playback-position " \
            "user-top-read " \
            "playlist-read-collaborative " \
            "playlist-modify-public " \
            "playlist-read-private " \
            "playlist-modify-private " \
            "app-remote-control " \
            "streaming " \
            "user-read-email " \
            "user-read-private " \
            "user-library-modify " \
            "user-library-read"

    # Spotify API credentials
    CLIENT_ID = "CLIENT_ID"
    CLIENT_SECRET = "CLIENT_SECRET"
    REDIRECT_URI = "http://localhost:8989/spotifyCallback"

class stt_const:
    CHUNK = 1024  # Record in chunks of 1024 samples
    SAMPLE_FORMAT = paInt32  # 16 bits per sample
    CHANNELS = 1
    FS = 25000  # Record at this many samples per second
    FILENAME = "output.mp3"
    MIN_DURATION = 1.5  # Minimum duration of a recording. Seconds
    SILENCE_TIME = 2
    THRESHOLD_CALC_TIME = 3
    MODEL = "base.en"
    ADD_THRESHOLD = 10


class input_const:
    DICTIONARY = {
        "previous song": "previous",
        "next song": "next",
        "get time": "get-time",
        "pause music": "pause-music",
        "resume music": "resume-music",
        "shuffle on": "shuffle on",
        "shuffle off": "shuffle off"
    }
