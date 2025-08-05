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

def generate_wordlist(info, output_file="wordlist.txt", max_words=100000):
    print(Fore.CYAN + f"[*] Generating wordlist (max {max_words} words)...")

    # Always save in script folder
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, output_file)

    written = 0

    with open(output_path, "w") as f:
        def save_word(word):
            nonlocal written
            if written < max_words:
                f.write(word + "\n")
                written += 1
                if written % 1000 == 0:
                    print(Fore.YELLOW + f"[*] Progress: {written}/{max_words} words...")
                return True
            return False

        # Basic variations
        for item in info:
            for var in [item, item.lower(), item.upper(), item.capitalize(),
                        item[::-1], item + item]:
                if not save_word(var): return written
            for l in leetspeak(item):
                if not save_word(l): return written

        # Combine multiple inputs (2-word combos only for safety)
        for r in range(2, 3):
            for combo in itertools.permutations(info, r):
                for var in [ "".join(combo), "".join(combo).lower(),
                             "".join(combo).upper(), "".join(combo).capitalize() ]:
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

    name = input(Fore.MAGENTA + "Target's name: ").strip()
    nickname = input(Fore.MAGENTA + "Nickname: ").strip()
    birthday = input(Fore.MAGENTA + "Birthday (e.g., 1998 or 15081998): ").strip()
    pet = input(Fore.MAGENTA + "Pet name: ").strip()
    university_id = input(Fore.MAGENTA + "University ID: ").strip()
    phone = input(Fore.MAGENTA + "Phone number: ").strip()
    phone_last8 = input(Fore.MAGENTA + "Phone number last 8 digits: ").strip()
    phone_last8_rev = input(Fore.MAGENTA + "Reversed last 8 digits: ").strip()
    father = input(Fore.MAGENTA + "Father's name: ").strip()
    mother = input(Fore.MAGENTA + "Mother's name: ").strip()
    partner = input(Fore.MAGENTA + "Partner's name: ").strip()
    fav_color = input(Fore.MAGENTA + "Favorite color: ").strip()
    fav_place = input(Fore.MAGENTA + "Favorite place: ").strip()
    company = input(Fore.MAGENTA + "Company/school name: ").strip()
    hobby = input(Fore.MAGENTA + "Hobby: ").strip()
    vehicle = input(Fore.MAGENTA + "Vehicle/plate number: ").strip()
    username = input(Fore.MAGENTA + "Social media username: ").strip()
    fav_person = input(Fore.MAGENTA + "Favorite person's name: ").strip()
    best_friend = input(Fore.MAGENTA + "Best friend's name: ").strip()

    info = [name, nickname, birthday, pet, university_id, phone,
            phone_last8, phone_last8_rev, father, mother, partner,
            fav_color, fav_place, company, hobby, vehicle, username,
            fav_person, best_friend]

    info = [i for i in info if i != ""]

    add_more = input(Fore.MAGENTA + "Do you want to add extra custom words? (yes/no): ").strip().lower()
    if add_more in ['yes', 'y']:
        while True:
            word = input(Fore.MAGENTA + "Enter custom word (or press Enter to stop): ").strip()
            if word == "":
                break
            info.append(word)

    # Ask safe limit
    limit_input = input(Fore.MAGENTA + "Maximum words to generate (default 100000): ").strip()
    max_words = 100000
    if limit_input.isdigit():
        max_words = int(limit_input)

    # Ask output filename
    filename_input = input(Fore.MAGENTA + "Enter output filename (default: timestamped): ").strip()
    if filename_input == "":
        # Add timestamp if no filename given
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename_input = f"wordlist_{timestamp}.txt"

    generate_wordlist(info, output_file=filename_input, max_words=max_words)

if __name__ == "__main__":
    main()

