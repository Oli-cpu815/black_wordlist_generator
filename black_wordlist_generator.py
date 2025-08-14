#!/usr/bin/env python3
import itertools
import os
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

def print_banner():
    banner = f"""
{Fore.GREEN}
╔══════════════════════════════════════════════════╗
║        Welcome to Black Personal Wordlist        ║
╚══════════════════════════════════════════════════╝
{Style.RESET_ALL}
    """
    print(banner)

def leetspeak(word):
    replacements = {
        'a': ['a', '@', '4'],
        's': ['s', '$', '5'],
        'i': ['i', '1', '!'],
        'o': ['o', '0'],
        'e': ['e', '3']
    }
    variations = ['']
    for char in word:
        new_variations = []
        if char.lower() in replacements:
            for v in variations:
                for repl in replacements[char.lower()]:
                    new_variations.append(v + repl)
        else:
            for v in variations:
                new_variations.append(v + char)
        variations = new_variations
    return variations

def generate_wordlist(info, output_file="wordlist.txt", max_words=300000):
    print(Fore.CYAN + f"[*] Generating wordlist (max {max_words} words)...")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, output_file)
    written = 0

    with open(output_path, "w") as f:
        def save_word(word):
            nonlocal written
            if written >= max_words:
                return False
            f.write(word + "\n")
            written += 1
            return True

        # Basic variations
        for item in info:
            for var in [item, item.lower(), item.upper(), item.capitalize(), item[::-1], item + item]:
                if not save_word(var): return written
            for l in leetspeak(item):
                if not save_word(l): return written

        # Combine multiple inputs safely
        max_combo_length = 3  # limit to 3-word combos
        for r in range(2, min(len(info)+1, max_combo_length+1)):
            for combo in itertools.permutations(info, r):
                for var in ["".join(combo), "".join(combo).lower(), "".join(combo).upper(), "".join(combo).capitalize()]:
                    if not save_word(var): return written

        # Add extras
        extras = ["123", "321", "000", "9999", "!", "@", "#", "$", "%", "&", "2024", "2025"]
        for item in info:
            for extra in extras:
                if not save_word(item + extra): return written
                if not save_word(extra + item): return written

    print(Fore.GREEN + f"[+] Wordlist generated successfully: {output_path}")
    print(Fore.GREEN + f"[+] Total words written: {written}")
    return written

def main():
    print_banner()
    print(Fore.MAGENTA + "Enter the following information (press Enter to skip):")

    fields = [
        "Target's name", "Nickname", "Birthday (e.g., 1998 or 15081998)", "Pet name",
        "University ID", "Phone number", "Phone number last 8 digits", "Reversed last 8 digits",
        "Father's name", "Mother's name", "Partner's name", "Favorite color",
        "Favorite place", "Company/school name", "Hobby", "Vehicle/plate number",
        "Social media username", "Favorite person's name", "Best friend's name"
    ]

    info = [input(Fore.MAGENTA + f"{field}: ").strip() for field in fields]
    info = [i for i in info if i != ""]

    add_more = input(Fore.MAGENTA + "Add extra custom words? (yes/no): ").strip().lower()
    if add_more in ['yes', 'y']:
        while True:
            word = input(Fore.MAGENTA + "Enter custom word (or press Enter to stop): ").strip()
            if not word:
                break
            info.append(word)

    filename_input = input(Fore.MAGENTA + "Output filename (default: timestamped): ").strip()
    if not filename_input:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename_input = f"wordlist_{timestamp}.txt"

    # Automatic 300k word generation
    generate_wordlist(info, output_file=filename_input, max_words=300000)

if __name__ == "__main__":
    main()

