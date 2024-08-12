"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", "25064357")
        self.API_HASH: str = os.environ.get("API_HASH", "0c999a454fddd79251213be7944811e8")
        self.SESSION: str = os.environ.get("SESSION", "BQFQySMAux_IdPMjJoLo8YLxDe4g4DwMsgpJ0H1ahPDr7KMTfTXSPUIg7XiPA58A77HvafMjNAJvQUXQCe0TRILm5XSSGYP1hgVBL-rr9Ix8b19K9av1uOh_MAXfwHlUpWDJGQo31SyVqJZggnzwMRt42J3XChBXT7mdUlMZHmGT3TX3Tp0a51Ko5N_ZYYC1riXkBE9zdsZBAxvSkvWbwFgIzXI-OL_e3sKxP_eRXYepDhhw5hezUnA0dFrb9VIPDlPBUf3SXy3vdLc4E82NrgnGlhtOOKumpYVlMnWjsiua8oF3D2xNWWNwQqfwQ2Gf7jARLj5a3zhXF-SFRX0esEXYVlaQugAAAAGg5MS6AA")
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "7124627930:AAEcTz8_pNhjM_4C1bHHp9gL-jpmDB86W0w")
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", "1750583099").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)


config = Config()
