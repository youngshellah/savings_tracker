# Savings Tracker
# Stores members as a list of dictionaries.

from re import search


members = []          # list of dictionaries, one per member
member_ids = set()    # set of IDs, used to prevent duplicates


def get_positive_number(prompt):
    """Keep asking until the user enters a number greater than 0."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Amount must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")


def add_member():
    """Add a new member if the ID is not already used."""
    name = input("Enter member name: ").strip()
    member_id = input("Enter member ID: ").strip()

    if name == "" or member_id == "":
        print("Name and ID cannot be empty.")
    elif member_id in member_ids:
        print("A member with that ID already exists.")
    else:
        members.append({
            "id": member_id,
            "name": name,
            "contributions": 0.0,
            "loan": 0.0,
        })
        member_ids.add(member_id)
        print(f"{name} added successfully.")


def view_all_members():
    """Display every member, or a message if there are none."""
    if not members:
        print("No members yet.")
        return
    for member in members:
        print(f"ID: {member['id']} | {member['name']} | "
              f"Savings: {member['contributions']:.2f} | "
              f"Loan: {member['loan']:.2f}")

# Search helper function to find a member by ID
def find_member_by_id(member_id):
    """Return the member dictionary with the given ID, or None if not found."""
    for member in members:
        if member["id"] == member_id:
            return member
    return None


record_contribution_or_loan = None  # Placeholder for future implementation
def record_transaction(): 
    """Add a contribution or a loan to an existing member."""
    if not members:
        print("No members yet. Please add a member first.")
        return

    member_id = input("Enter member ID: ").strip()
    member = find_member_by_id(member_id)
    if member is None:
        print("Member not found.")
        return

    print("1. Record a contribution")
    print("2. Record a loan")
    choice = input("Enter your choice (1 or 2): ").strip()
    if choice == "1":
        amount = get_positive_number("Enter contribution amount (ksh): ")
        member["contributions"] += amount
        print(f"Contribution of {amount:.2f} recorded for {member['name']}.")
    elif choice == "2":
        amount = get_positive_number("Enter loan amount (ksh): ")
        member["loan"] += amount
        print(f"Loan of {amount:.2f} recorded for {member['name']}.")

    else:
        print("Invalid choice. Please select 1 or 2.")
        
# view one member 
def view_one_member():
    """Search by ID and display one member."""
    member_id = input("Enter member ID").strip()
    member = find_member_by_id(member_id)

    if member is None:
        print("Member not found.")
    else:
        print(f"ID: {member['id']} | {member['name']} | "
              f"Savings: {member['contributions']:.2f} | "
              f"Loan: {member['loan']:.2f}")

def show_menu():
    print("\n--- Savings Tracker ---")
    print("1. Add a member")
    print("2. Record a contribution or loan")
    print("3. View one member")
    print("4. View all members")
    print("5. Calculate group total and average")
    print("6. Find highest or lowest contributor")
    print("7. Remove a member")
    print("8. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_member()
        elif choice == "3":
            member_id = input("Enter member ID: ").strip()
            member = find_member_by_id(member_id)
            if member:
                print(f"ID: {member['id']} | {member['name']} | "
                      f"Savings: {member['contributions']:.2f} | "
                      f"Loan: {member['loan']:.2f}")
            else:
                print("Member not found.")
        elif choice == "4":
            view_all_members()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Not built yet or invalid choice.")


main()
