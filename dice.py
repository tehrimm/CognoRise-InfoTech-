import random


def roll_dice(sides, rolls):
    results = []
    for _ in range(rolls):
        roll_result = random.randint(1, sides)
        results.append(roll_result)
    return results


def main():
    print("Welcome to the Dice Rolling Simulator!")

    # Get user input for number of sides and rolls
    sides = int(input("Enter the number of sides on the dice: "))
    rolls = int(input("Enter the number of rolls: "))

    # Roll the dice and display the results
    results = roll_dice(sides, rolls)
    print(f"\nResults of {rolls} rolls with a {sides}-sided dice:")

    for i, result in enumerate(results, start=1):
        print(f"Roll {i}: {result}")


if __name__ == "__main__":
    main()
