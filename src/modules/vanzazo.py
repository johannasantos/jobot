import random

from ..base.jobot import jobot


def vanzazo(update, context):
    id_images = [
        "AgACAgEAAx0CWF9M_QACkzJepg7XccLJag62rrF-W0YC9_iy-wACX6gxG34WEUSItCIrBI-PrL8hFDAABAEAAwIAA3kAA-WBBgABGQQ",
        "AgACAgEAAx0CWF9M_QACkzFepg7XWOetd6HxRgsjptmwpdkKiwACSagxGzRg8UerDtoBsKiaznHabgYABAEAAwIAA3kAAzFgAQABGQQ",
        "AgACAgEAAx0CWF9M_QACkyZephFWHAvjKai4boNoC4McnOfPigACs6gxG7bmsETvGzjDglouXiHrawYABAEAAwIAA3kAA6teAwABGQQ",
        "AgACAgEAAx0CWF9M_QACkyVephGDP2JclLcr56CDmVEziPNvmQACsqgxG7bmsESeCOG4GzxxRm3jbgYABAEAAwIAA3kAA56aAQABGQQ",
        "AgACAgEAAx0CWF9M_QACkyRephGo-nqzEvcSwRUQNlOZpbBgoQACZ6gxG583mUQTpDpbRstcMpLaawYABAEAAwIAA3kAA11VAwABGQQ",
        "AgACAgEAAx0CWF9M_QACk01ephH9o6RLXvlILHQZjv8NGcAcuQACNKgxGzrXIUdGl6bKNT_LWUv1awYABAEAAwIAA3kAA6q2AgABGQQ"
    ]

    image_to_send = random.choice(id_images)

    context.bot.send_photo(chat_id=update.message.chat_id, photo=image_to_send)

jobot.add_command("vanzazo", vanzazo, args=False, 
                   description="Envía una foto random de Van")