# initial release

import re
import win32clipboard
import win32con
import time

# Function to check if a string matches the given URL pattern
def is_valid_url(text):
    pattern = r"https?://([a-zA-Z0-9]+\.)*x\.com(/[\S]*)?"
    return re.match(pattern, text)

# Function to modify the URL
def modify_url(text):
    return re.sub(r"x\.com", "vxtwitter.com", text)

# Function to monitor the clipboard for changes
def monitor_clipboard():
    print("This script monitors the clipboard for URLs containing 'x.com' and modifies them to 'vxtwitter.com'.")

    recent_text = None
    check_interval = 0.2  # Check clipboard every 0.2 seconds
    report_interval = 5  # Report that the script is still running every 5 seconds
    next_report_time = time.time() + report_interval

    while True:
        if time.time() > next_report_time:
            print("Script is still running...")
            next_report_time = time.time() + report_interval

        win32clipboard.OpenClipboard()
        try:
            new_text = win32clipboard.GetClipboardData(win32con.CF_TEXT).decode("utf-8")
            if new_text != recent_text and is_valid_url(new_text):
                recent_text = new_text
                modified_text = modify_url(recent_text)
                print(f"Original URL: {recent_text}")
                print(f"Modified URL: {modified_text}")
                win32clipboard.EmptyClipboard()
                win32clipboard.SetClipboardText(modified_text)
        except TypeError:
            pass
        finally:
            win32clipboard.CloseClipboard()

        time.sleep(check_interval)

if __name__ == '__main__':
    monitor_clipboard()
