# my_scripts
Where I'll dump all my bash scripts

### flash-test
*Must have F3 installed*
```bash
sudo apt install f3
```
- must be run as root
- will run lsblk then ask you for the disk and the mountpoint

Uses F3 to:
1) DESTRUCTIVELY check if the device is the size it claims
2) Get write speed
3) Get read speed

it took about an hour for a 16 GB cheapo sd card to run on my machine, nice to have it fire and forget and not take 3 commands and now I don't have to remember them

### dns
I couldn't remember the DNS command and just want to check my pihole is still running
it also reminds me of nslookup so I can check if it's not only running but still blocking the webistes I asked it to block

### fans
I couldn't remember how to get current fan info on linux so I wrote this, when the fans ramp up I just like to know how ramped up the are *shrug*

### fix-settings
I kept breaking my regolith-linux settings app and had to run this every time and had to spend 20 minutes googling how. Now if I break it I just run fix-settings and move on

### fontcharlist
Outputs current font characters to a file so you can peruse them to see what you want to use as an icon in the i3 bar. I didn't like my computer being an engine but when I found nothing better in my font I gave up and stuck with it

### opusToMp3
This is more as notes, probably shouldn't be left executable. It changes all opus it finds in a directory (recursively) and makes an mp3 version
There's also a command to do it in parallel

### pic_print
Someday I'll get to making a cli to make 2 images fit on a 4x6... Someday maybe. Great for scrapbooking is all

### yt-dl-stuff
Similar to opusToMp3, mostly as notes so I can remember the commands to actually get yt playlists either as audio only or audio video
