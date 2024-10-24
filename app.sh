#!/bin/bash

center_text() {
    local text="$1"
    local width="${COLUMNS:-$(tput cols)}"
    printf "%*s\n" $(((${#text} + width) / 2)) "$text"
}

print_line() {
    local char="$1"
    printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' "$char"
}

print_line '*'
center_text "Server Informer (Telegram Bot)"
print_line '*'
echo "Waiting 30sec ..."
sleep 30

LOCAL_IP=$(ip addr show | grep 'inet ' | grep -v '127.0.0.1' | awk '{print $2}' | cut -d'/' -f1)
echo "Local IP received"

USER_NAME=$(whoami)
echo "User name received"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE="$SCRIPT_DIR/config.ini"

get_value() {
    local key="$1"
    grep -oP "^$key=\K.*" "$CONFIG_FILE"
}

SERVER_INFO_BOT_TOKEN=$(get_value "token")
ADMIN_CHAT_IDS=$(get_value "admins" | tr ',' '\n')

mask_chat_id() {
    local chat_id="$1"
    echo "${chat_id:0:2}****${chat_id: -2}"
}

MESSAGE="User: $USER_NAME | Local IP: $LOCAL_IP | Command: ssh $USER_NAME@$LOCAL_IP"

echo "Message generated"

print_line '-'
center_text "Sending information:"
print_line '-'

if [ -n "$ADMIN_CHAT_IDS" ]; then
    for CHAT_ID in $ADMIN_CHAT_IDS; do
        MASKED_CHAT_ID=$(mask_chat_id "$CHAT_ID")
        RESPONSE=$(curl -s -X POST "https://api.telegram.org/bot$SERVER_INFO_BOT_TOKEN/sendMessage" -d "chat_id=$CHAT_ID&text=$MESSAGE")

        if echo "$RESPONSE" | grep -q '"ok":true'; then
            echo "Admin $MASKED_CHAT_ID: OK"
        else
            echo "Admin $MASKED_CHAT_ID: Error"
        fi
        print_line '-'
    done
else
    echo "No admin chat IDs found."
    print_line '-'
fi
center_text "https://github.com/smartlegionlab/server_info_rg_bot/"
center_text "The work is completed"
print_line '='
