import os, sys, time, shutil, random, math

# ---------- SETTINGS ----------
SETTINGS = {
    "USERNAME": "",
    "TYPE_SPEED": 0.02,
    "QUICK_START": False
}
START_TIME = time.time()

# ---------- FAKE FILESYSTEM ----------
FAKE_FILESYSTEM = [
    {"name": "document.txt", "type": "file", "content": "This is a sample document."},
    {"name": "image.png", "type": "file", "content": "Fake image preview..."},
    {"name": "music.mp3", "type": "file", "content": "♫ ♫ ♫"},
    {"name": "Videos", "type": "folder", "content": []},
    {"name": "Notes", "type": "folder", "content": []},
]

# ---------- CUSTOM COMMANDS ----------
CUSTOM_COMMANDS = {}

# ---------- UTILITY FUNCTIONS ----------
def typewrite(text, speed=None, newline=True):
    speed = speed if speed is not None else SETTINGS["TYPE_SPEED"]
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    if newline:
        print()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def center_text(text):
    width = shutil.get_terminal_size((80, 20)).columns
    return text.center(width)

def show_logo():
    logo = [
        "██████╗ ██╗   ██╗██████╗ ██╗ █████╗ ███╗   ██╗",
        "██╔══██╗██║   ██║██╔══██╗██║██╔══██╗████╗  ██║",
        "██████╔╝██║   ██║██████╔╝██║███████║██╔██╗ ██║",
        "██╔═══╝ ██║   ██║██╔══██╗██║██╔══██║██║╚██╗██║",
        "██║     ╚██████╔╝██████╔╝██║██║  ██║██║ ╚████║",
        "╚═╝      ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝",
    ]
    for line in logo:
        typewrite(center_text(line), speed=0.003)
    typewrite(center_text("PYBIAN GNU/Linux Terminal Emulator v5.1"), speed=0.02)
    print()

# ---------- SETUP ----------
def setup():
    clear()
    typewrite(center_text("Welcome to PYBIAN Setup Wizard!"), speed=0.02)
    try:
        SETTINGS["USERNAME"] = input("Enter your username: ").strip() or "boats_are_goats"
    except EOFError:
        SETTINGS["USERNAME"] = "boats_are_goats"
        typewrite("\nNo input detected. Using default username.")
    try:
        ts = input("Enter typing speed (0.01=fast, 0.05=slow, default 0.02): ").strip()
        SETTINGS["TYPE_SPEED"] = float(ts) if ts else 0.02
    except (EOFError, ValueError):
        SETTINGS["TYPE_SPEED"] = 0.02
        typewrite("Invalid input. Using default 0.02")
    try:
        quick = input("Enable Quick Start? (y/n): ").strip().lower()
        SETTINGS["QUICK_START"] = quick == "y"
    except EOFError:
        SETTINGS["QUICK_START"] = False
    typewrite(f"Setup complete! Hello {SETTINGS['USERNAME']}!\n", speed=SETTINGS["TYPE_SPEED"])
    time.sleep(0.5)
    clear()

# ---------- CREATORDEV FUNCTION ----------
def creator_dev():
    typewrite("Enter the new command name: ", speed=0.01)
    cmd_name = input().strip()
    if not cmd_name:
        typewrite("Cancelled — no command name entered.", speed=0.01)
        time.sleep(1)
        return

    typewrite(f"Creating code for command '{cmd_name}' in Dex editor...\n", speed=0.01)
    content_lines = []

    while True:
        line = input(">>> ")  # Dex-style code input
        if line.strip().lower() == "!save!":
            CUSTOM_COMMANDS[cmd_name.lower()] = "\n".join(content_lines)
            typewrite(f"Command '{cmd_name}' created successfully!", speed=0.01)
            time.sleep(1)
            break
        elif line.strip().lower() == "!cancel!":
            typewrite("Command creation cancelled.", speed=0.01)
            time.sleep(1)
            break
        else:
            content_lines.append(line)

# ---------- DEX FAKE FILE EXPLORER ----------
def fake_file_explorer():
    index = 0
    while True:
        clear()
        typewrite("Dex - Fake File Explorer (w=up, s=down, enter=open, 9=create file, d=creatordev, q=exit):", speed=0.01)
        for i, f in enumerate(FAKE_FILESYSTEM):
            selector = "-> " if i == index else "   "
            typewrite(f"{selector}{f['name']} ({f['type']})", speed=0.005)
        choice = input().lower()

        if choice == "w":
            index = (index - 1) % len(FAKE_FILESYSTEM)
        elif choice == "s":
            index = (index + 1) % len(FAKE_FILESYSTEM)
        elif choice == "":
            selected = FAKE_FILESYSTEM[index]
            if selected["type"] == "file":
                clear()
                typewrite(f"Opening {selected['name']}...\n", speed=0.01)
                typewrite(selected["content"], speed=0.005)
                input("\nPress Enter to go back to Dex...")
            elif selected["type"] == "folder":
                typewrite(f"{selected['name']} is a folder. Nothing inside yet.", speed=0.01)
                input("\nPress Enter to go back to Dex...")

        elif choice == "9":
            clear()
            typewrite("Dex File Creator\n", speed=0.01)
            filename = input("Enter filename (e.g. notes.txt): ").strip()
            if not filename:
                typewrite("Cancelled — no filename entered.", speed=0.01)
                time.sleep(1)
                continue

            typewrite(f"Start typing below. Type '!save!' to save, or '!cancel!' to cancel.\n", speed=0.01)
            content_lines = []
            while True:
                line = input()
                if line.strip().lower() == "!save!":
                    FAKE_FILESYSTEM.append({"name": filename, "type": "file", "content": "\n".join(content_lines)})
                    typewrite(f"File '{filename}' saved successfully!", speed=0.01)
                    time.sleep(1)
                    break
                elif line.strip().lower() == "!cancel!":
                    typewrite("File creation cancelled.", speed=0.01)
                    time.sleep(1)
                    break
                else:
                    content_lines.append(line)

        elif choice == "d":  # creatordev shortcut in Dex
            creator_dev()

        elif choice == "q":
            break

# ---------- TEXTGUI FAKE WINDOW ----------
def textgui_window():
    gui_running = True
    options = [
        "1 - Say Hello",
        "2 - Show Time",
        "3 - Random Joke",
        "4 - Count 1 to 5",
        "5 - Exit GUI",
        "6 - DO NOT PRESS (virus-like)"
    ]

    def virus_like_command():
        print("\n!!! WARNING: DO NOT USE 6 !!!\n")
        for i in range(10):
            print(f"Random text {random.randint(1000,9999)}")
            time.sleep(0.2)
        print("\n***** DON'T USE 6 *****")
        input("\nPress Enter to continue...")

    while gui_running:
        clear()
        print("+-------------------------+")
        print("|      TextGUI Window     |")
        print("|  [X] Close (doesn't work) |")
        print("+-------------------------+")
        print("\nCommands:")
        for o in options:
            print("   " + o)
        choice = input("\nEnter command number: ").strip()
        
        if choice == "1":
            print("Hello!")
            input("Press Enter to continue...")
        elif choice == "2":
            print("Current time:", time.strftime("%H:%M:%S"))
            input("Press Enter to continue...")
        elif choice == "3":
            jokes = [
                "Why did the chicken cross the road? To get to the other side!",
                "I told my computer I needed a break, and it said no problem – it needed one too!"
            ]
            print(random.choice(jokes))
            input("Press Enter to continue...")
        elif choice == "4":
            for i in range(1, 6):
                print(f"Count: {i}")
                time.sleep(0.5)
            input("Press Enter to continue...")
        elif choice == "5":
            gui_running = False
        elif choice == "6":
            virus_like_command()
        else:
            print("Invalid choice!")
            input("Press Enter to continue...")

# ---------- TERMINAL LOOP ----------
def terminal_loop():
    global START_TIME
    START_TIME = time.time()
    show_logo()
    typewrite(center_text("Type 'help' for commands.\n"), speed=SETTINGS["TYPE_SPEED"])
    
    while True:
        cmd = input(f"{SETTINGS['USERNAME']}@pybian:~$ ").strip()
        if not cmd:
            continue

        # ---------- CUSTOM COMMAND ----------
        if cmd.lower() == "creatordev":
            creator_dev()
        elif cmd.lower() in CUSTOM_COMMANDS:
            try:
                exec(CUSTOM_COMMANDS[cmd.lower()], globals())
            except Exception as e:
                typewrite(f"Error executing custom command: {e}", speed=0.01)

        # ---------- SYSTEM COMMANDS ----------
        elif cmd.lower() in ["clear", "cls"]:
            clear()
        elif cmd.lower() == "help":
            typewrite("""
=================== PYBIAN TERMINAL HELP ===================

SYSTEM COMMANDS:
 help                → Show this detailed help manual.
 clear / cls         → Clear the terminal screen.
 info                → Show system and Python version info.
 setup               → Start the setup wizard again.
 restart             → Restart the terminal session.
 exit                → Shut down the emulator safely.
 version             → Show current emulator version.
 whoami              → Display your username.
 who                 → Show logged-in user info.
 uptime              → Display time since startup.
 uptimefull          → Show detailed uptime info.
 time                → Display the current time (HH:MM:SS).
 date                → Display full date and time.
 ping <host>         → Simulate pinging a host (fake result).
 name <new_name>     → Change your username.
 typespeed <num>     → Change typing speed (0.01 fast, 0.05 slow).
 helpme              → Shortcut reminder about help command.

FILESYSTEM COMMANDS:
 ls                  → List files in the current directory.
 pwd                 → Show current working directory.
 mkdir <name>        → Create a new folder.
 rmdir <name>        → Remove a folder.
 rm <file>           → Delete a file.
 touch <file>        → Create an empty file.
 cat <file>          → Show contents of a text file.
 echo <text> [n]     → Print text; optionally repeat n times.
 repeat <text> [n]   → Same as echo, repeats text.
 repeatword <w> <n>  → Repeat one word n times.
 tree                → Show folder and file structure.
 dex                 → Open Dex, the fake file explorer.
 creatordev          → Create a custom Python command using Dex text editor.

MATH COMMANDS:
 calc <expr>         → Evaluate a math expression safely.
 sqrt <num>          → Calculate the square root.
 sin <deg>           → Sine (angle in degrees).
 cos <deg>           → Cosine (angle in degrees).
 tan <deg>           → Tangent (angle in degrees).
 log <num>           → Base-10 logarithm.
 ln <num>            → Natural logarithm (base e).
 abs <num>           → Absolute value.
 ceil <num>          → Round up to the nearest integer.
 floor <num>         → Round down to the nearest integer.
 bin <num>           → Convert integer to binary.
 hex <num>           → Convert integer to hexadecimal.
 oct <num>           → Convert integer to octal.

TEXT & STRING COMMANDS:
 reverse <text>      → Reverse the provided text.
 echo <text>         → Print text to the terminal.
 sleep <seconds>     → Pause program for given seconds.
 random <min> <max>  → Generate a random integer in range.

FUN COMMANDS:
 fortune             → Show a random inspirational quote.
 joke                → Display a random joke.
 textgui             → Open TextGUI fake window interface.
 install <pkg>       → Simulate installing a package.
 haxs                → Spam random characters for fun.

CUSTOM COMMANDS:
 creatordev          → Create custom Python commands available here.
<Any custom commands you make appear automatically.>

============================================================
""")

        # ---------- REST OF SYSTEM COMMANDS ----------
        elif cmd.lower() == "info":
            typewrite(f"Pybian Terminal Emulator\nPython version: {sys.version.split()[0]}", speed=0.01)
        elif cmd.lower() == "whoami":
            typewrite(f"Current user: {SETTINGS['USERNAME']}", speed=0.01)
        elif cmd.lower() == "who":
            typewrite(f"{SETTINGS['USERNAME']} is logged into the system.", speed=0.01)
        elif cmd.lower() == "uptime":
            uptime = time.time() - START_TIME
            typewrite(f"Uptime: {int(uptime)} seconds", speed=0.01)
        elif cmd.lower() == "uptimefull":
            uptime = time.time() - START_TIME
            mins, secs = divmod(int(uptime), 60)
            hours, mins = divmod(mins, 60)
            typewrite(f"Uptime: {hours}h {mins}m {secs}s", speed=0.01)
        elif cmd.lower() == "version":
            typewrite("Pybian Emulator v5.1", speed=0.01)
        elif cmd.lower() == "time":
            typewrite(time.strftime("%H:%M:%S"), speed=0.01)
        elif cmd.lower() == "date":
            typewrite(time.strftime("%Y-%m-%d %H:%M:%S"), speed=0.01)
        elif cmd.lower().startswith("ping "):
            host = cmd[5:]
            typewrite(f"Pinging {host}...", speed=0.01)
            time.sleep(1)
            typewrite(f"Reply from {host}: time={random.randint(1,200)}ms", speed=0.01)
        elif cmd.lower().startswith("name "):
            newname = cmd[5:].strip()
            if newname:
                SETTINGS["USERNAME"] = newname
                typewrite(f"Username changed to {newname}", speed=0.01)
            else:
                typewrite("Usage: name <new_name>", speed=0.01)
        elif cmd.lower().startswith("typespeed "):
            try:
                SETTINGS["TYPE_SPEED"] = float(cmd.split()[1])
                typewrite(f"Typing speed set to {SETTINGS['TYPE_SPEED']}", speed=0.01)
            except:
                typewrite("Usage: typespeed <number>", speed=0.01)
        elif cmd.lower() == "helpme":
            typewrite("Use 'help' to view all available commands.", speed=0.01)
        elif cmd.lower() == "dex":
            fake_file_explorer()
        elif cmd.lower() == "textgui":
            textgui_window()
        elif cmd.lower() == "restart":
            typewrite("Restarting terminal...", speed=0.01)
            time.sleep(1)
            terminal_loop()
        elif cmd.lower() == "exit":
            typewrite("Shutting down Pybian Terminal Emulator...", speed=0.01)
            break
        elif cmd.lower().startswith("echo "):
            parts = cmd.split()
            if len(parts) >= 2:
                text = " ".join(parts[1:])
                typewrite(text, speed=0.01)
            else:
                typewrite("Usage: echo <text>", speed=0.01)
        elif cmd.lower() == "fortune":
            fortunes = [
                "The only limit to our realization of tomorrow is our doubts of today.",
                "Courage is resistance to fear, mastery of fear – not absence of fear.",
                "In the middle of every difficulty lies opportunity.",
                "The secret of getting ahead is getting started."
            ]
            typewrite(random.choice(fortunes), speed=0.01)
        elif cmd.lower() == "joke":
            jokes = [
                "Why did the programmer quit his job? Because he didn't get arrays!",
                "I told my computer I needed a break, and it said: 'You seem stressed, take 5 bytes!'",
                "There are only 10 types of people: those who understand binary and those who don’t.",
                "Why do Java developers wear glasses? Because they don't C#!"
            ]
            typewrite(random.choice(jokes), speed=0.01)
        elif cmd.lower().startswith("calc "):
            expr = cmd[5:].strip()
            try:
                result = eval(expr, {"__builtins__": None}, math.__dict__)
                typewrite(f"Result: {result}", speed=0.01)
            except Exception as e:
                typewrite(f"Error: {e}", speed=0.01)
        elif cmd.lower().startswith("random "):
            try:
                _, a, b = cmd.split()
                num = random.randint(int(a), int(b))
                typewrite(f"Random number: {num}", speed=0.01)
            except:
                typewrite("Usage: random <min> <max>", speed=0.01)
        elif cmd.lower() == "haxs":
            for i in range(50):
                print(''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(500)))
                time.sleep(0.005)
        else:
            typewrite(f"Unknown command: {cmd}", speed=0.01)

# ---------- MAIN ----------
if __name__ == "__main__":
    if not SETTINGS["QUICK_START"]:
        setup()
    terminal_loop()
