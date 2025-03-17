from colorama import Fore, init
import requests
import random
import time
import asyncio

init()

print(Fore.CYAN + r"""
__________.__                           ___________                     __                 
\______   \  | _____  ___.__. __________\__    ___/___________    ____ |  | __ ___________ 
 |     ___/  | \__  \<   |  |/ __ \_  __ \|    |  \_  __ \__  \ _/ ___\|  |/ // __ \_  __ \
 |    |   |  |__/ __ \\___  \  ___/|  | \/|    |   |  | \// __ \\  \___|    <\  ___/|  | \/
 |____|   |____(____  / ____|\___  >__|   |____|   |__|  (____  /\___  >__|_ \\___  >__|   
                    \/\/         \/                           \/     \/     \/    \/       
                                        https://github.com/sudzythegoat/PlayerTracker
""")

TrackerName = input("Enter the name of your tracker:\n")
SessionTicket = input("Enter your session ticket:\n")
WEBHOOK_URL = input("Enter your tracker webhook url:\n")
STATUS_WEBHOOK_URL = input("Enter your webhook url that will receive status updates:\n")
ColorHexxed = input("Enter embed color (hex):\n")
StatusRole = input("Enter role (id) to get pinged when tracker is started:\n")

SharedGroupID = "63FDD"

Cosmetics = [
    {
        "CosmeticName": "Stick",
        "CosmeticId": "LBAAK.",
        "ImageURL": "https://cdn.discordapp.com/attachments/1190579178131697715/1344264139136303134/stick.jpg"
    },
    {
        "CosmeticName": "Admin Badge",
        "CosmeticId": "LBAAD.",
        "ImageURL": "https://cdn.discordapp.com/attachments/1190579178131697715/1344265627661238334/Adminbadge.webp"
    },
    {
        "CosmeticName": "Illustrator Badge",
        "CosmeticId": "LBAGS.",
        "ImageURL": "https://cdn.discordapp.com/attachments/1190579178131697715/1344265780937752586/IllustratorBadgeSprite.webp"
    },
    {
        "CosmeticName": "Finger Painter",
        "CosmeticId": "LBADE.",
        "ImageURL": "https://cdn.discordapp.com/attachments/1190579178131697715/1344264618750509159/er.webp"
    }
]

# ty for the codes notfish
Codes = [
    "TYLERVR", "ALECVR", "LUCIO", "DEEP", "JUAN", "JUANGTAG", "MELT", "JMAN", "JMANCURLY", "ELLIOT",
    "ELLIOT1", "ELLIOT2", "VMT", "K9", "HUNT", "MODS", "MOD", "MEET2", "MEET3", "GTAG", "MEET4",
    "MEET5", "MEET6", "MEET7", "MEET8", "QWERTY", "QWERTYUIOP", "SILLY", "TILLY", "VEN1", "VEN2",
    "RANG", "GTC", "DYL", "TAG", "TTT", "TTTPIG", "PIG", "MINIGAM", "MINIGAME", "MINIGAMES",
    "MALLRUSH", "COLORRUSH", "SHELF", "ROLEPLAY", "GORILLA", "MONKE", "MONKEY", "BOT", "GHOST",
    "MIRRORMAN", "ERROR", "RUN", "RUN555999", "SREN17", "SREN18", "SREN16", "COMP", "J3VU", "PBBV",
    "ECHO", "555999", "STATUE", "DAISYDAISY", "DAISY", "DAISY09", "DAISY08", "CHIPPD", "BANSHEE",
    "123", "1234", "12345", "123456", "1234567", "12345678", "123456789", "1234567890", "ALEC",
    "MAXO", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "ECT", "MINI", "VEN", "FOOT",
    "MONKER", "FAADDUU", "FAADDUUVR", "CUBCUB", "CUBCUB11", "BUBBLESVR", "ELLIOTVR", "ELLIOT3",
    "STYLED", "SNAIL", "STYLEDSNAIL", "JUITAR", "FIIZY", "ITSFIIZY", "CHRISNADO", "MAJORA",
    "ANTOCA", "STICK", "STICKS", "GTAG", "SKIBIDI", "IDEN", "IDENVR", "GAY", "ABC", "ABCD", "A",
    "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
    "T", "U", "V", "W", "X", "Y", "Z", "AMXR", "ZERDY", "DAPPER", "TURBO", "MOSA", "RAKZZ",
    "AUSSIE", "H4KPY", "DAPPERSLUG", "CODY", "QUINN", "LEOVR", "LEO", "PARTYMONKEY", "BOETHIA",
    "CHIVI", "HEADCHEF", "HEADCHEFVR", "KNINLY", "JAWCLAMPS", "KISHARK", "WIDDOM", "TIKTOK",
    "YOUTUBER", "GTC1", "GTC2", "GTC3", "GTC4", "GTC5", "GTC6", "GTC7", "GTC8", "GTC9", "GTC10",
    "AA", "THUMBZ", "JMAN1", "K8", "TIMMY", "JMAN2", "JMAN3", "GT", "CGT", "RUN1", "666",
    "DAISY099", "ENDISHERE", "BANJO", "CHIPPDBANJO", "GH0ST", "END", "DEATH", "FNAF", "ECH0",
    "BANANA", "SMILER", "UNKNOWN", "BOTS", "DEAD", "MORSE", "SPIDER", "MONK", "MODDER", "MODDERS",
    "MODERATOR", "BODA", "JOLYENE", "ELECTRONIC", "OWNER", "DEV", "CREATOR", "11", "12", "13", "14",
    "15", "16", "17", "18", "19", "20", "CREEP", "CREEPY", "SCARY", "SPOOKY", "SPOOK", "GAMES",
    "PLAY", "FINGERPAINTER", "CONTENTCREATOR", "CONTENT", "HELPME", "BEES", "NAMO", "WARNING",
    "HIDE", "WOW", "MITTENS", "RAY2", "RAY1", "GRAPES", "MICROPHONE", "BARK", "DURF", "JULIAN",
    "HAVEN", "VR", "WEAREVR", "FINGER", "PAINTER", "ADMIN", "STAFF", "CRASH", "YOUTUBE",
    "MODDING", "LEMMING"
]

def get_track_time():
    unix_timestamp = int(time.time())
    return f"<t:{unix_timestamp}:R>"

formatted_time = get_track_time()
print(formatted_time)

def Send(item, code, region, player_count, board_position, image_url, content=f"@everyone"):
    tracked_formatted = get_track_time()
    try:
        webhook_data = {
            "content": content,
            "embeds": [{
                "title": f"{item} was found",
                "color": int(ColorHexxed, 16),
                "fields": [
                    {"name": "**Code: **", "value": f"```{code}```", "inline": False},
                    {"name": "**Region: **", "value": f"```{region}```", "inline": False},
                    {"name": "**Player Count: **", "value": f"```{player_count}```", "inline": False},
                    {"name": "**Position: **", "value": f"```{board_position}```", "inline": False}
                ],
                "image": {"url": image_url},
                "footer": {
                    "text": f"Tracked by {TrackerName} {tracked_formatted}",
                }
            }]
        }

        requests.post(WEBHOOK_URL, json=webhook_data)

    except Exception as e:
        print(Fore.RED + f"Error sendind webhook: {e}")


def Start():
    try:
        current_time = time.strftime("%H:%M:%S", time.localtime())

        free_embed = [{
            "title": f"{TrackerName} has been started",
            "color": ColorHexxed,
            "fields": [
                {"name": "**Tracker Info**", "value": f"```Codes: {len(Codes)}```", "inline": True},
                {"name": "**Status**", "value": "```ONLINE```", "inline": True},
                {"name": "**Time**", "value": f"```{current_time}```", "inline": True},
            ],
            "footer": {"text": f"github.com/sudzythegoat/PlayerTracker"}
        }]

        requests.post(STATUS_WEBHOOK_URL, json={"content": f"<@{StatusRole}>", "embeds": free_embed})
    except Exception as e:
        print(Fore.RED + f"Error in Start: {str(e)}")

def Track():
    try:
        for code in Codes:
            for region in ['EU', 'US', 'USW']:
                try:
                    print(Fore.CYAN + f"Checking room code: {code}{region}")
                    headers = {"X-Authorization": SessionTicket}
                    json = {"SharedGroupId": code + region}

                    response = requests.post(
                        url=f"https://{SharedGroupID}.playfabapi.com/Client/GetSharedGroupData",
                        headers=headers,
                        json=json,
                        timeout=10
                    )

                    requestjson = response.json()

                    if 'code' not in requestjson:
                        print(Fore.YELLOW + f"Invalid response for {code}{region}")
                        continue

                    if requestjson['code'] == 200 and 'data' in requestjson:
                        room_data = requestjson['data'].get('Data', {})
                        player_count = len(room_data)
                        board_position = 0

                        if player_count > 0:
                            print(Fore.LIGHTBLACK_EX + f"Checked Room {code}{region} with {player_count} players")
                        else:
                            print(Fore.LIGHTBLACK_EX + f"{code}{region} is empty")

                        for key, value in room_data.items():
                            board_position += 1
                            concat = value.get('Value', '')

                            for CosmeticData in Cosmetics:
                                if CosmeticData['CosmeticId'] in concat:
                                    content = "@everyone"
                                    image_url = CosmeticData['ImageURL']
                                    send(CosmeticData['CosmeticName'], code, region, player_count, board_position, image_url, content)
                                    print(Fore.GREEN + f"Found {CosmeticData['CosmeticName']} in code: {code}")

                    elif requestjson['code'] == 429:
                        print(Fore.RED + f"Rate limit hit for {code}{region}")
                        continue

                except requests.exceptions.RequestException as e:
                    print(Fore.RED + f"Request error for {code}{region}: {str(e)}")
                    time.sleep(1)
                    continue

    except Exception as e:
        print(Fore.RED + f"Error in track function: {str(e)}")

if __name__ == "__main__":
    Start()
    while True:
        try:
            Track()
            time.sleep(1)
        except Exception as e:
            print(Fore.RED + f"Error: {e}")
            print(Fore.YELLOW + "Retrying...")
            time.sleep(1)
            continue
