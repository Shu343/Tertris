
START_MSG = """
Hello <b>{}</b> ! I'm <b>Tetris</b>.
I'll guess your character by some questions.
Do /play 
"""

ME_MSG = """
<b>Name :</b> <code>{}</code>
<b>User Name :</b> <code>{}</code>
<b>User ID :</b> <code>{}</code>
<b>Language :</b> <code>{}</code>
<b>Child Mode :</b> <code>{}</code>
<b>Total Guess :</b> <code>{}</code>
<b>Correct Guess :</b> <code>{}</code>
<b>Wrong Guess :</b> <code>{}</code>
<b>Unfinished Guess :</b> <code>{}</code>
<b>Total Questions :</b> <code>{}</code>
"""

AKI_LANG_CODE = {
    'en': 'English',
    'ar': 'Arabic',
    'cn': 'Chinese',
    'de': 'German',
    'es': 'Spanish',
    'fr': 'French',
    'il': 'Hebrew',
    'it': 'Italian',
    'jp': 'Japanese',
    'kr': 'Korean',
    'nl': 'Dutch',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'ru': 'Russian',
    'tr': 'Turkish',
    'id': 'Indonesian',
}

AKI_LANG_MSG = """
Change Playing Language.
<b>NOTE : This does not change the Bot language.</b>
<b>Current Language :</b> <pre>{}</pre>
"""

CHILDMODE_MSG = """
If Child mode is enabled, Tetris won't show any NSFW content.
<b>Current Status :</b> <pre>Child mode is {} !</pre>
"""

AKI_FIRST_QUESTION = "This is the first question. You can't go back any further!"