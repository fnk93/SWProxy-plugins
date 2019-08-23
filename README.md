## SWProxy Plugins
plugins for the SW Proxy

To get the latest versions of the plugins that are guaranteed to work with the latest SWProxy release, please visit the [Releases](https://github.com/lstern/SWProxy-plugins/releases) section. If you download the plugins directly from the repository they may not be fully compatible with the latest release of SWProxy and may have some reduced or no functionality.

Each plugin has 2 files, a .py file with the actual plugin code and a .yapsy-plugin file with the plugin description.
To install the plugins just drop the desired plugins in the /plugins folder, copy and edit the .config file to the parent folder and restart sw proxy.

You can have multiple users connected and actively using the same proxy. It will separate users based on their user_id and create separate files for each account.

* [Video Tutorial](https://www.youtube.com/watch?v=T4zI6HViV9g)

### Install
Install [Python >= 3.6](https://www.python.org/downloads/)
```
git clone https://github.com/fnk93/SWProxy-plugins.git
cd SWProxy-plugins
py -m pip install --user virtualenv
```
Now either set up a virtual environment or install to your main python distribution.
```
py -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```

### Run
Run the proxy through mitmdump
Alternative way up to do.
Open your shell / PowerShell in the SWProy-plugins folder
```
.\env\Scripts\activate
mitmdump -s ./mitm_script.py --ignore-hosts '^((?!qpyou\.cn).)*$'
```
This will listen on port 8080 on your current ip.

First off, for iOS you don't need any special preparation.
For Android 7+ you need to have root.
Once you installed and started the proxy and set up the proxy in your mobile phone you need to navigate to (mitm.it) where you download the certificate.

iOS: (not tested by me)
```
1. Download & Install
2. Yes
3. Go to setting
4. Enter iOS password
5. Signed
6. Go to settings
7. Search for "Certificate"
8. Toggle "On" the certificate you signed
```

Android (7-):
```
Just install the certificate.
```

Android (7+):
```
1. You need a rooted phone
2. Download certificate
3. Rename certificate to ca.crt
4. Install app "Root Certificate Manager"
5. Install certificate in that app.
6. Hide root
```

### Arena Logger
Logs all attacks you make including rivals. In order to correctly record the opponent's name, the proxy must be connected when your phone recieves the arena log (on login, list refresh or when a new attack is recieved), otherwise it will just record the enemy team. The output filename is [user_id]_arena.csv

### Full Logger
Dumps the contents of the requests and responses from/to com2us servers on a text file ("full_log_filename" from swproxy.config)

### Generate Friend Swarfarm
Generates data for visited friends for use with Swarfarm. The generate data will not contain any inventory rune.

### Google Sheet Writer
Allows all reports to be written directly to Google Sheets. Requires an API key and extra dependencies. Once these dependencies are built into SWProxy a video tutorial will be made showing how to set it up.

### Raid Logger
Will log raid results including time, reward and raid members. The output filename is [user_id]_raids.csv

### Recruit Evaluator
This plugin will generate extra data when visiting friend. The extra data is intended to help with guild recruit evaluation.

### Run Logger
Will log runs and drops from Necro, Dragons, Giants, elemental halls and HoH. The outut filename is [user_id]_runs.csv

### Summon Logger
Will log summons of any type of scroll, including social and crystal summon. Does not work with individual monster pieces (from SD).  The outut filename is [user_id]_summons.csv

### ToA Logger
Will log results from ToA attempts, it includes floor, difficulty, team used and monster faced in the last wave. The outut filename is [user_id]_toa.csv

### World Boss Logger
Will log each attack against the world boss, including the attack power, elemental bonus, total damage, grade and all the mobs selected for the fight. The outut filename is [user_id]_worldboss.csv

### SWarfarm Logger
Will send data about your runs and summons to [swarfarm](https://swarfarm.com/) where you will have access to full data and statistics about your runs. Site will also offer aggregate statistics using data from all users.
