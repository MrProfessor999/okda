from Music import BOT_NAME , BOT_USERNAME , USERNAME , NAME


# Contents
MOVIE_STR = """
️<b>{}</b> : {}

• Status : <pre>{}</pre>
• Genres : <pre>{}</pre>
• Languages : <pre>{}</pre>
• Runtime : <pre>{} minutes</pre>
• Budget : <pre>{}</pre>
• Revenue : <pre>{}</pre>
• Release Date : <pre>{}</pre>
• Average Rating : <pre>{}</pre>
• Popularity : <pre>{}</pre>

• OverView : <em>{}</em>
"""

TV_STR = """
<b>{}</b>

• Created by : <pre>{}</pre>
• Genres : <pre>{}</pre>
• Languages : <pre>{}</pre>
• Episodes Runtime : <pre>{}</pre>
• First aired : <pre>{}</pre>
• Last aired : <pre>{}</pre>
• Status : <pre>{}</pre>
• Seasons : <pre>{}</pre>
• Total EPs : <pre>{}</pre>
• Average Rating : <pre>{}</pre>
• Production Company : <pre>{}</pre>

• OverView : <em>{}</em>
"""

ANIME_STR = """
<b>{}</b> | <b>{}</b>

• Category : <pre>{}</pre>
• Type : <pre>{}</pre>
• Average Rating : <pre>{}</pre>
• Status : <pre>{}</pre>
• First aired : <pre>{}</pre>
• Last aired : <pre>{}</pre>
• Runtime : <pre>{} minutes</pre>
• No of episodes : <pre>{}</pre>

• Synopsis : <em>{}</em>
"""

MANGA_STR = """
<b>{}</b> | <b>{}</b>
• Type : <pre>{}</pre>
• Average Rating : <pre>{}</pre>
• Status : <pre>{}</pre>
• First release : <pre>{}</pre>
• Last release : <pre>{}</pre>
• Volume count : <pre>{}</pre>
• No of chapters : <pre>{}</pre>
• Serialization : <pre>{}</pre>

• Synopsis : <em>{}</em>
"""

# Inline Content
INLINE_STR = """
• <b>Title</b> : {}
• <b>Release</b> : <pre>{}</pre>
• <b>Popularity</b> : <pre>{}</pre>
• <b>Language</b> : <pre>{}</pre>
• <b>Average Rating</b> : <pre>{}</pre>

• <b>OverView</b> : <em>{}</em>
"""

INLINE_DESC = """
<b>Usage:</b> <pre>&lt;tv&gt; title</pre> <b>or</b> <pre>&lt;movie&gt; title</pre> <b>in inline query.</b>

Examples:
× <pre>&lt;movie&gt; Avengers Endgame</pre>
× <pre>&lt;tv&gt; Breaking Bad</pre>
× <pre>&lt;anime&gt; Attack on Titan</pre>
• You can try on buttons below!
"""


# Start
START_STRING = """
Hey {}, I'm {BOT_NAME} and i can help you to play music on your group and channel and I can help you to get \
information about your favorite movies, tv and anime shows, you can also download \
music & can view song lyrics using me! Just click the button \
below to get started with list of possible commands...

You can also search movies, tvshows & \
anime inline! just type <pre>{BOT_USERNAME}</pre> in \
your message box and follow the instructions.

And don't forget to smile, atleast once in a while ;)
"""
START_STRING_GRP = "Hmmm?"


# About
ABOUT_STR = f"""
I'm fully written in \
Python3 by <a href="https://t.me/N_A_V_I_P_A_V_I">MrProfessor</a>, \
feel free to report him if you find any rough edge inside me.

<b>×</b> Name  : <a href="https://t.me/{BOT_USERNAME}">{BOT_NAME}</a>
<b>×</b> Creator : <a href="https://t.me/{USERNAME}">{NAME}</a>
<b>×</b> Python version : 3.9.8
<b>×</b> Library version : Pyrogram
<b>×</b> Movies & TV data : <pre>themoviedb.org</pre>
<b>×</b> Anime data from : <pre>kitsu.io</pre>
<b>×</b> Music data from : <pre>deezer.com</pre>
<b>×</b> Lyrics data from : <pre>genius.com</pre>

"""

# Help
HELP_STR = """
Hey there 👋, click on the buttons below to get Help \
for the related functions. 😜
"""

MOVIE_HELP = """
<b> help for Movies 😉 </b>

<b>×</b> /movies : Search for info about your favorite movies.
"""
SERIES_HELP = """
<b> help for Series 😉 </b>

<b>×</b> /tvshows : Get information for your favotite TV shows/Series.
"""
ANIME_HELP = """
<b> help for Anime 😉 </b>

<b>×</b> /anime : Search for info about your favorite Anime titles.
"""
MANGA_HELP = """
<b> help for Manga 😉 </b>

<b>×</b> /manga : Get information about your favorite Manga titles.
"""
MUSIC_HELP = """
<b> help for music 😉 </b>

<b>×</b> /music : Download your favorite music in high resolution.
"""
LYRICS_HELP = """
<b> help for Lyrics 😉 </b>

<b>×</b> /lyrics : Get lyrics for your favorite songs.
"""
SUB_HELP = """

<b>×</b> /subtitle : Download subtitles for your movies.
"""

# Errors
API_ERR = "Sorry, couldn't reach API at the moment :("
NOT_FOUND = "Sorry, couldn't find any results for the query :("
INVALIDCAT = "Hmmm.. maybe you've sent wrong category to look for, please try again!"
KEYERROR = "Oops! something went wrong. Please try again :("

# Cancel
CANCEL = "Cancelled the current task!"

# To search
TOSEARCHMOVIE = "Please reply with the movie title you wanna look for."
TOSEARCHTV = "Please reply with the TV title you wanna look for."
TOSEARCH_ANIME = "Please reply with the anime title you want to look for."
TOSEARCH_MANGA = "Please reply with the manga name you wanna look for."

# Subtitles
TOSEARCHSUBS = "Please reply with the Movie | Anime name you want subs for."
SUBS_STR = "🏷 Subtitles for <b>{}</b>.\nClick on buttons below to download!"
