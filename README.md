## Black Personal Wordlist 

A Python-based personal wordlist generator designed for ethical hacking, penetration testing, and cybersecurity research.
Generates custom wordlists using target-specific information with leetspeak variations, permutations, and appended numbers/symbols. Capable of producing up to 300,000+ entries safely.

## Features

Generates wordlists from personal information: name, nickname, birthday, pets, family, hobbies, social usernames, etc.

Supports leetspeak transformations (a -> @, 4, s -> $, 5, i -> 1, !, etc.).

Creates permutations and combinations of multiple inputs (up to 3-word combos to ensure performance).

Appends common numbers and symbols (123, 321, !, @, 2024, etc.) for better coverage.

Generates large wordlists safely (default limit: 300,000 words).

Automatically creates timestamped output files.

Optional custom words can be added for more targeted wordlists.

Cross-platform support (Linux, macOS, Windows with Python 3).


## Installation & Usage
```bash
1: Clone the repository
git clone https://github.com/Oli-cpu815/black_wordlist_generator.git

2: Navigate to the project folder
cd black_wordlist_generator

3: Make the script executable
sudo chmod +x black_wordlist_generator.py

4: Create a virtual environment and activate it
python3 -m venv venv && source venv/bin/activate

5: Install required dependencies
pip install colorama

# 6: Run the wordlist generator
python3 black_wordlist_generator.py

7: Deactivate the virtual environment when done
deactivate
```

## Example

```bash
$ python3 black_wordlist_generator.py
Target's name: John
Nickname: Johnny
Birthday: 15081998
Pet name: Max
Add extra custom words? yes
Enter custom word: Secret123
```


The script generates combinations and leetspeak variations, producing a comprehensive personal wordlist ready for use in security testing.


## License

This project is released under the MIT License.
Use responsibly and only for ethical hacking and cybersecurity purposes.

## Disclaimer

This tool is intended solely for educational purposes and authorized security testing.
Do not use it for illegal activities. The author is not responsible for misuse.

## Author

Oli Ahamed

Cybersecurity Analyst | Red Team Specialist | Ethical Hacker

GitHub: https://github.com/Oli-cpu815

