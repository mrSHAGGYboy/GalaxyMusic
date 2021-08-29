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
SESSION_NAME = getenv("BQCScgKMNih42LDfyLdObjuFg6J-H-JaQ_mrgRwRC0dGKdXqtVHNz1Che-dr6MiQTu6FyIyHVKjT40GPZEqQ3g-s_bG_UxqN92bw1a23w8Oh8s-jKjyGQgt4384NcvjFJDFXhnzSvwFz1udRP41FAiSMResACSoZKpkMej4-okm1rtYey89P2Q9PisXCjrjBgsqHN3FKOuS9RdABdKIs5VpjvpgDYlJ8tekreHgwHPXi5abx_XVq-vktKQQZ_lLe2ZHSxdy292GvEA-nLOEP53Z3RJEMbYJXaGIgRxnkaGgweJdOxTwqdTNKuK4270LozXqXyCIcldQ8cqV1auOCJ5MPaWdR3QA", "session")
BOT_TOKEN = getenv("1723953864:AAENuZPvZHtythK1bykjMr-I8v5QyK06DE0")
BOT_NAME = getenv("Music player")
admins = {}
API_ID = int(getenv("4763422"))
API_HASH = getenv("87ec2c03054386ef4aea87fb09050a1b")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
