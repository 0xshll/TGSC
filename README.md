# Telegram Group Member Transfer Script

A Python script built with **Telethon** to transfer members between Telegram groups efficiently. This script provides an interactive menu to transfer members, reset sessions, and handle errors gracefully.

---

## 📦 Installation

### 1. Install Telethon
To install the required dependencies, run the following command in your Python environment (e.g., Pydroid 3):

```bash
pip install -r requirements.txt
```

### 2. Install Python (if not installed)
If Python is not installed, download it from the official website:  
[**Download Python**](https://www.python.org/downloads/)

### 3. Obtain Telegram API ID and API HASH
To access the Telegram API, create an application by following these steps:
1. Visit [my.telegram.org](https://my.telegram.org).
2. Log in with your phone number.
3. Click on **API development tools**.
4. Create a new application to obtain your **API ID** and **API HASH**.

---

## 🚀 Running the Script

### 1. Navigate to the Script Directory
Open a terminal and navigate to the folder containing the script:

```bash
cd TGSC
```

### 2. Run the Script
Execute the script with the following command:

```bash
python script.py
```

On the first run, the script will prompt you to enter your **API ID** and **API HASH**.

---

## 🛠️ Using the Script

Upon launching, the script displays an interactive menu with the following options:

1. **Transfer Members**: Move members from a source group to a target group.
2. **Exit**: Close the script.
3. **Reset Session**: Delete the current session to log in with a different phone number.

### Transfer Members
When selecting the **Transfer Members** option, you will be prompted to:
- Enter the **source group** username or link.
- Enter the **target group** username or link.
- Specify the **number of members** to transfer.

The script will begin transferring members, logging results and handling errors automatically.

---

## 🔧 Error Handling

- **Rate Limiting**: If Telegram's rate limit is exceeded, an error message will appear, and the script will pause. Wait and retry later.
- **Invite Restrictions**: Users with privacy settings blocking invites will be logged, and the script will proceed to the next user.
- **Other Errors**: Unexpected errors will be logged and displayed for troubleshooting.

---

## 🗑️ Deleting Session

To switch accounts, select the **Reset Session** option. This will delete the current session and prompt you to log in with a new phone number.

---

## 📂 Notes

- **Permissions**: Ensure you have the necessary permissions in both source and target groups to invite users.
- **Rate Limits**: Telegram imposes strict rate limits. Avoid transferring large numbers of users at once.
- **Privacy Settings**: Users with restricted invite settings will be logged in a `failed.txt` file.

---

## 📞 Support

For questions ,DM on Telegram:  
[@yyeir](https://t.me/yyeir)

---

## ⚠️ Disclaimer

Use this script responsibly and in compliance with Telegram's Terms of Service. The developer is not responsible for any misuse or account restrictions resulting from improper use.
