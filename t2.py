codename = input("Enter your codename: ")
age = int(input("Enter your age: "))
goal = input("What’s your ultimate goal?: ")
elite = input("Are you elite,(yes/no): ").strip().lower()

years_left = 30 - age

status = True if elite=="yes" else False
print("\n Generating Report...\n")
print(f"Commander {codename}, at just {age} years old, you're already on the path to {goal}.")
print(f"\n Elite Status: {'Good job coming this far soldier' if status else 'Work hard'}")
print(f"\nYou’ve got {years_left} years to sharpen your skills before you hit 30. Stay sharp. Stay lethal.")
print(f" \nYears till 30: {years_left}")
print("\nStay lethal. Stay sharp. Cobra out.")