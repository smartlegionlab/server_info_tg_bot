# Server Info - Telegram Bot

---

### Description of the Python application:

**Name:** Server Info Telegram Bot

**Description:**
Server Info Telegram Bot is a simple and effective application written in Python,
which allows you to send system information from the server to users specified in the configuration file.
The application automatically extracts the login of the current user,
local IP address and generates a command for connecting via SSH.
All necessary parameters, such as token and chat IDs, are stored and configured in the configuration file.

You can add this application to autorun on your server to get the necessary information in tg when running. 
This can be especially useful on home computers, 
which many people sometimes use as a test server or a server for hosting telegram bots.

**Main functions:**
- Sending notifications to specified Telegram chats.
- Automatically receiving user login and local IP address.
- Forming an SSH command for remote connection.
- Customizable configuration file for ease of use.

**Requirements:**
- Python 3.x

**Installation:**
- Clone the repository. 
- Create a `config.json` file in your project folder.

Exemple `config.json`:
```json
{
    "token": "your telegram token",
    "admins": [
        "chat_id1",
        "chat_id1"
    ]
}

```

- Add the bot's token to the file, and the chat IDs of those to whom the bot will send messages.


- Run the application. `python app.py`

---

### Images:

![LOGO](https://github.com/smartlegionlab/server_info_tg_bot/raw/master/data/images/py_logo.png)

---

### Description of the Bash script (.sh):


**Description:**
The Bash version of Telegram SSH Notifier performs the same functions as the Python application,
but is written as a Bash script. This script allows you to send notifications to Telegram,
including the user login, local IP address, and the generated command for connecting via SSH.
All parameters are also configured through the configuration file.

**Main functions:**
- Sending notifications to specified Telegram chats.
- Automatically receiving user login and local IP address.
- Forming an SSH command for remote connection.
- Customizable configuration file for ease of use.

**Requirements:**
- Bash (usually pre-installed on most Unix-like systems).
- `curl` or `wget` utilities for sending requests to the Telegram API.

**Installation:**
- Clone the repository. 
- Create a `config.ini` file in your project folder.

Exemple `config.ini`:
```ini
# Token for the Telegram bot
token=your telegram token

# Admin chat IDs
admins=chat_id1,chat_id2
```

- Add the bot's token to the file, and the chat IDs of those to whom the bot will send messages.
- Make the script executable with `chmod +x app.sh`.
- Run the application. `. app.sh`

---

### Images:

![LOGO](https://github.com/smartlegionlab/server_info_tg_bot/raw/master/data/images/sh_logo.png)

***

### WARNING:

Both versions send information 30 seconds after startup. 
This time is necessary for the server to start all the required services, 
including internet connection settings, before sending data. 
This approach ensures the system operates correctly and minimizes the 
likelihood of errors during automatic startup after being powered on.

***


    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

***

    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2018-2024, A.A. Suvorov
    All rights reserved.