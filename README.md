# Cookie Clicker Bot

- This script is designed to automate Cookie Clicker.

# Hello 👋

- This is the first code I wrote, and it was a lot of fun to create, so I hope you'll be understanding.
- Please don't take it too seriously; I spent two days on it, and while most features work as intended, there may still be some issues.
- I plan to continue developing and improving the code when I have some free time.

# Usage

- Run the script.
- If this is the first run, please close all pop-ups that may appear. ❗❗❗
- The script will automatically start performing its tasks.
- To stop the script, press the ESC key.
- Runtime Issues: If the script fails to execute as expected, ensure that your ChromeDriver is properly set up (see line 349). ❗❗❗

# Lastly

-You can modify or disable certain functions according to your needs. 
If you have suggestions for improving this script or if you have developed a better version, please feel free to share your ideas. 
Have fun! 😎

# Technical Details

### Version
- This script was created using Cookie Clicker v2.052. Note that newer features may not be compatible.

### Requirements

- Python 3.x
- Selenium WebDriver
- ChromeDriver
- Make sure to install the required Python packages using:

# Function Descriptions

### big_cookie_click:
- Responsible for collecting golden cookies and clicking the big cookie.

### auto_upgrades:
- Handles upgrades.
- A very simple function. Initially, I intended to create a function that performs calculations based on the cost of an upgrade, its efficiency, and the time required to gather enough resources for that upgrade.
- However, the function always ends up upgrading the last upgrade, regardless of other factors, which is not the desired behavior.
- I’m very curious about the best way to implement this. If you have any ideas for a better function, please give me a hint.

### close_popups:
- Responsible for closing pop-ups.

### change_bakery_name:
- Notifies everyone that the bot is running (completely useless).

### use_lumps:
- (To activate, uncomment lines 385 and 386). ❗
- Responsible for using sugar lumps. It upgrades each upgrade evenly.

### gain_lumps:
- (To activate, uncomment lines 388 and 389). ❗
- Responsible for adding a sugar lump. It works very well but may disrupt the fun.
- Gives you a sugar lump every 10 seconds, which is extremely overpowered.
- If you want to be even more overpowered, you can change the amounts or time in the code (lines 140 to 143), or simply use Game.gainLumps(999999999999999) in the console (press F12).

### ascend: ❗❗❗
- This function may cause issues with other functions and can disrupt the program.
- It is advised not to use it, as it may halt the program.
- Auto-upgrades are performed in a specified order (chosen by me), but no calculations were made when creating this bot.
- I plan to fix this function soon.	👍 

### measure_working_time:
- A simple function that tracks the runtime duration of the program.

### upgrade_dragon:
- Responsible for upgrading the dragon.
