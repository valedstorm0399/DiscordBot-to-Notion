import discord
from typing import Union

class EmbedTemplate:
    """Discord Embed 訊息的範本"""

    @staticmethod
    def normal(message: str, **kwargs) -> discord.Embed:
        """正常訊息的 Embed 範本"""
        return discord.Embed(color=0x7289DA, description=message, **kwargs)

    @staticmethod
    def error(exception: Union[Exception, str], **kwargs) -> discord.Embed:
        """錯誤訊息的 Embed 範本"""
        embed = discord.Embed(color=0xB54031, **kwargs)
        embed.description = str(exception)

        if "title" not in kwargs:
            embed.title = "Oops! An error occurred."

        return embed

# from: https://github.com/KT-Yeh/Genshin-Discord-Bot/blob/master/utility/discord_ui_template.py