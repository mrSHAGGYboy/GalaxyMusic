# Calls Music 1 - Telegram bot for streaming audio in group calls
# Copyright (C) 2021  Roj Serbest

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by Inukaasith
# Relared By Prabhasha 

from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("BQACqD33kVKRS-5etL2BOyKO3F5xqTz2AhiNqDGR1Lrv6sddw3wfJzQBJ_mKpsXD--Y7y6jnglS9UDdYnV622dzIvpPN2XgYYWDXEorF0Gk6cWHJ_RHrLd6X2HWrd7BukbyN121L4q0EhrgdsevzUemx__SZbOJ8-r_Td6YkJ_MJR5skt4eBzdHUU0KzOdik0AKcHfEcvnaFyruzlIpUGiCn68WaWa14tMwivAlgwexWQSVcLWMpXGMQn2cyE8FgpJrXlaF_hu-XdAjbv26XV5ldNMyfahaQGylI672vJT44VdTkjOvA38jDid8pPoBmCyl6z4gSpynDW2C7YxqRo0g0YhViYgA", "session")
BOT_TOKEN = getenv("1955724129:AAHn8D2Uu8-lu72onLEY44GNiPD_JfMoVu8")
BOT_NAME = getenv("Music player")
admins = {}
API_ID = int(getenv("6065291"))
API_HASH = getenv("dc7873c0a5c737af4356d4f245fe696d")

DURATION_LIMIT = int(getenv("7", "7"))

COMMAND_PREFIXES = list(getenv("/", "/ !").split())

SUDO_USERS = list(map(int, getenv("1153898821").split()))
