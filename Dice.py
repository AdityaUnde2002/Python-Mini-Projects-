import random  # Generates random values for variables.

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518 ")  # ASCII arts
# ● ┌ ─ ┐ │ └ ┘
"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"
#choice
choice=input("Press 'R' to roll the 🎲 : ")
choice=choice.lower()

while choice=="r":

    dice_art = {
        1: ("┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"),
        2: ("┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘"),
        3: ("┌─────────┐",
            "│ ●       │",
            "│    ●    │",
            "│       ● │",
            "└─────────┘"),
        4: ("┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘"),
        5: ("┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘"),
        6: ("┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘"),
    }

    #Variables
    dice = []
    total = 0
    no_of_dices = int(input("Enter number of dice : "))

    # Roll the dice and store their results
    for _ in range(no_of_dices):
        dice.append(random.randint(1, 6))

    # Print the dice ASCII art
    for i in range(5):  # Each die art has 5 lines
        for die in dice:
            print(dice_art[die][i], end="  ")  # Print each line side by side
        print()  # New line after each row of dice

    # Calculate and print the total
    total = sum(dice)
    print(f"Dice values: {dice}")
    print(f"Total: {total}")

    #Stop
    choice=input("\nPress 'R' to roll 🎲 again OR Press 'Exit' to stop 🛑 : ")
    choice=choice.lower()
    if choice=="exit":
        print("Thanks for playing!!")
        break
