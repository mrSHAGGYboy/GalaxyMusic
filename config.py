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
SESSION_NAME = getenv("", "session")
BOT_TOKEN = getenv("")
BOT_NAME = getenv("")
admins = {}
API_ID = int(getenv(""))
API_HASH = getenv("")

DURATION_LIMIT = int(getenv("7", "7"))

COMMAND_PREFIXES = list(getenv("/", "/ !").split())

SUDO_USERS = list(map(int, getenv("").split()))
