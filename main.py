from youtube_transcript_api import YouTubeTranscriptApi
from ollama import AsyncClient
from colorama import Fore as fg
from colorama import init as colorama_init
import asyncio
import os

colorama_init()
MODEL = 'llama3.2:3b'

# Colors
def colorify(color: str):
    return lambda text: f"{color}{text}{fg.RESET}"

lgreenify = colorify(fg.LIGHTGREEN_EX)
lredify = colorify(fg.LIGHTRED_EX)
orangeify = colorify(fg.LIGHTYELLOW_EX)
bold = lambda text: f"\033[1m{text}\033[0m"  # noqa: E731


video_id = input(lgreenify("Input the video id: "))
subs = ""

# Create "subs" and     "summarizations" directories if they don't exist
if not os.path.exists("subs"):
    os.makedirs("subs")
if not os.path.exists("summarizations"):
    os.makedirs("summarizations")

# Check if file exists under the subs directory
try:
    with open(f"subs/{video_id}.txt", "r") as f:
        subs = f.read()
    print(lgreenify("\nSubtitles already fetched!"))

    if input(lgreenify('\nDo you want to make the AI summarize this again? Or do you want to use the existing summary? (y/n): ')).lower()[0] == 'n':
        with open(f"summarizations/{video_id}.txt", "r") as f:
            print(bold(orangeify('\n\nSummary:')))
            print(f.read())
        exit()
except FileNotFoundError:
    print(lredify("\nSubtitles not found. Fetching subtitles..."))
    subs = ""


# Subtitles
srt = YouTubeTranscriptApi.get_transcript(video_id)


with open(f"subs/{video_id}.txt", "w") as f:
    for i in srt:
        if i['text']:
            f.write(f"{i['text']}\n")
            subs += f"{i['text']}\n"

if subs:
    print(lgreenify("\nSubtitles fetched successfully!"))
else:
    print(lredify("\nNo subtitles found for the video id provided."))

# Summarizing
async def chat():
    summarized = ''
    message = {'role': 'user', 'content': f'Summarize the video from the following subtitles: {subs}'}

    print()
    print(bold(orangeify('\n\nSummary:')))
    async for part in await AsyncClient(host='http://localhost:11434').chat(model=MODEL, messages=[message], stream=True):
        summarized += part['message']['content']
        print(part['message']['content'], end='', flush=True)
    print('\n')
    summarized += '\n'

    with open(f"summarizations/{video_id}.txt", "w") as f:
        f.write(summarized)


asyncio.run(chat())
