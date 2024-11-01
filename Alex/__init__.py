# Core imports
from Alex.core.dir import dirr
from Alex.core.git import git
from Alex.misc import dbb, heroku
from .logging import LOGGER

# Execute functions
dirr()
git()
dbb()
heroku()

# Initialize app and userbot, but do not import them in __init__.py directly
from Alex.core.bot import Anony
from Alex.core.userbot import Userbot

app = Anony()
userbot = Userbot()

# Import platforms at the end to avoid potential circular import issues
from .platforms import AppleAPI, CarbonAPI, SoundAPI, SpotifyAPI, RessoAPI, TeleAPI, YouTubeAPI

# Initialize platform instances
Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()