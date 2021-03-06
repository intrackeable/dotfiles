#!/usr/bin/env python3
#https://github.com/intrackeable/dotfiles

from lazy import Ricer
import argparse

def options():
    parser = argparse.ArgumentParser()
    parser.add_argument('-R', help='Set a random wallpaper', dest='wallpaper', action='store_true')
    parser.add_argument('-G', help='Gaps level between [0-30]', type=int, dest='gaps')
    parser.add_argument('-B', help='Blur level for picom [1-10]', type=int, dest='blur')
    flags = parser.parse_args()
    return flags.wallpaper, flags.gaps, flags.blur

def main():
    wm_path = '/home/intrackeable/.config/i3/config'
    wallpaper_path = '/home/intrackeable/.scripts/images/'
    blur_path = '/home/intrackeable/.config/picom/picom.conf'

    wallpaper, gaps, blur = options()

    manager = Ricer(wm_path,wallpaper_path,blur_path)

    if gaps:
        manager.set_gaps(gaps)
        manager.replace_gaps()
    elif wallpaper:
        manager.set_wallpaper()
    elif blur:
        manager.set_blur(blur)
        manager.replace_blur()

if __name__ == '__main__':
    main()
