import os
import datetime


ThemeList = ['Mc-OS-CTLina-Dark','Mojave-light-alt']

Nights = ['/home/anantha/Pictures/Wallpapers/Night.jpg','/home/anantha/Pictures/Wallpapers/Middnight.jpg']
Morrnings = ['/home/anantha/Pictures/Wallpapers/Morrning.jpg','/home/anantha/Pictures/Wallpapers/Noon.jpg','/home/anantha/Pictures/Wallpapers/Evening.jpg']

while True:

    CurrTime = datetime.datetime.now()

    Hour = CurrTime.hour

     # print(Hour)

    TimeList = ['06','12','17','19','24']

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

        os.system("gsettings get org.gnome.desktop.background picture-uri 'file:////home/anantha/Pictures/Wallpapers/Noon.jpg'").format(Morrnings[1])

        os.system('gsettings set org.gnome.desktop.interface gtk-theme "{}"'.format(ThemeList[1]))
    if Hour >= Evening and Night > Hour:

        os.system("gsettings get org.gnome.desktop.background picture-uri 'file:////home/anantha/Pictures/Wallpapers/Evening.jpg'").format(Morrnings[2])

        os.system('gsettings set org.gnome.desktop.interface gtk-theme "{}"'.format(ThemeList[1]))
    if Hour >= Night and Middnight > Hour:

        os.system("gsettings get org.gnome.desktop.background picture-uri 'file:///{}'").format(Nights[0])

        os.system('gsettings set org.gnome.desktop.interface gtk-theme "{}"'.format(ThemeList[0]))
    if Hour == Middnight:

        os.system("gsettings get org.gnome.desktop.background picture-uri 'file:///{}'").format(Nights[1])

        os.system('gsettings set org.gnome.desktop.interface gtk-theme "{}"'.format(ThemeList[0]))