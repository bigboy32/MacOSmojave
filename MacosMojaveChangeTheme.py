# Made by Github/BigBoy32
'''
Made for Everyone!

Please Change the Code: * Link your files (CTRL-H find all my files and replace with yours), Set Your timeings!

If you wan't Download the Wallpapers and the Themes (Move the themes to .themes or make .themes and move them)

Run the code when you wan't to check the time and automaticly Change it!

Feel free to edit and comment issues!
'''

CurrTime = datetime.datetime.now()

Hour = CurrTime.hour

TimeList = ['06','12','17','20','24']

Morrning = TimeList[0]

Morrning = int(Morrning)

Noon = TimeList[1]

Noon = int(Noon)

Evening = TimeList[2]

Evening = int(Evening)

Night = TimeList[3]

Night = int(Night)

Middnight = TimeList[4]

Middnight = int(Middnight)

Hour = int(Hour)

if Hour >= Morrning and Noon > Hour:

    os.system("gsettings set org.gnome.desktop.background picture-uri 'file:////home/anantha/Pictures/Wallpapers/Morrning.jpg'")

    os.system('gsettings set org.gnome.desktop.interface gtk-theme "Mojave-light-alt"')
elif Hour >= Noon and Evening > Hour:

    os.system("gsettings set org.gnome.desktop.background picture-uri 'file:////home/anantha/Pictures/Wallpapers/Noon.jpg'")

    os.system('gsettings set org.gnome.desktop.interface gtk-theme "Mojave-light-alt"')
if Hour >= Evening and Night > Hour:

    os.system("gsettings set org.gnome.desktop.background picture-uri 'file:////home/anantha/Pictures/Wallpapers/Evening.jpg'")

    os.system('gsettings set org.gnome.desktop.interface gtk-theme "Mc-OS-CTLina-Dark"')
if Hour >= Night and Middnight > Hour:

    os.system("gsettings set org.gnome.desktop.background picture-uri 'file:////home/anantha/Pictures/Wallpapers/Night.jpg'")

    os.system('gsettings set org.gnome.desktop.interface gtk-theme "Mc-OS-CTLina-Dark"')
if Hour == Middnight:
    os.system("gsettings set org.gnome.desktop.background picture-uri 'file:////home/anantha/Pictures/Wallpapers/Middnight.jpg'")

    os.system('gsettings set org.gnome.desktop.interface gtk-theme "Mc-OS-CTLina-Dark"')
