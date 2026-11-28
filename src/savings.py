# Savings Tracker
# Stores members as a list of dictionaries.

import json
import os


DATA_FILE = os.path.join(os.path.dirname(__file__), "savings_data.json")
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

# json
def save_data():
    """write all members to the json file."""
    with open(DATA_FILE, "w") as file:
        json.dump(members, file, indent=2)

def load_data():
    """Read mebers from the file if it exists."""
    if not os.path.exists(DATA_FILE):
        return
    try:
        with open(DATA_FILE) as file:
            saved = json.load(file)
            members.extend(saved)
            for member in saved:
                member_ids.add(member["id"]) #rebuild the set
    except (json.JSONDecodeError, KeyError):
        print("Could not read saved data. Starting empty.")       


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


#  Group total and average function placeholder 
def calculate_summary():  
    """Show total savings, average per member, and total loans."""
    if not members:
        print("No members yet, nothing to calculate.")
        return

    total_savings = 0.0
    total_loans = 0.0
    for member in members:
        total_savings += member["contributions"]
        total_loans += member["loan"]
    average = total_savings / len(members)
    print(f"Members: {len(members)}")
    print(f"Total savings: {total_savings:.2f}")
    print(f"Average savings per member: {average:.2f}")
    print(f"Total loans: {total_loans:.2f}")


# Highest or lowest contributor function placeholder 
def find_extreme():
    """Find the member with the highest or lowest contribution."""
    if not members:
        print("No members yet.")
        return

    print("1. Find highest contributor")
    print("2. Find lowest contributor")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        #key tellls max() to use the contributions value for comparison
        highest_member = max(members, key=lambda m: m["contributions"])
        print(f"Highest contributor: {highest_member['name']} "
              f"with {highest_member['contributions']:.2f}")
    elif choice == "2":
        lowest_member = min(members, key=lambda m: m["contributions"])
        print(f"Lowest contributor: {lowest_member['name']} "
              f"with {lowest_member['contributions']:.2f}")
    else:
        print("Invalid choice. Please select 1 or 2.")


# Remove member function placeholder 
def remove_member():
    """Remove member from both the list and ID set."""
    if not members:
        print("No members yet.")
        return

    member_id = input("Enter member ID to remove: ").strip()
    member = find_member_by_id(member_id)
    if member is None:
        print("Member not found.")
        return

    members.remove(member)
    member_ids.remove(member_id)
    print(f"Member {member['name']} removed successfully.")

# loan repayment
def repay_loan():
    """Reduce a members loan balance.""" 
    if not members:
        print("No members yet.")
        return

    member_id = input("Enter member ID:").strip()
    member = find_member_by_id(member_id)


    if member is None:
        print("Member not found.")
    elif member["loan"] == 0:
        print(f"{member['name']} has no outstanding loan.")
    else: 
        print(f"{member['name']} has an outstanding loan of {member['loan']:.2f}.") 
        amount= get_positive_number("Enter repayment amount (ksh): ")
        if amount > member["loan"]:
            print(f"Repayment exceeds outstanding loan. Reducing loan to 0.")
            member["loan"] = 0
        else:
            member["loan"] -= amount
            print(f"Repayment of {amount:.2f} recorded for {member['name']}. "
                  f"Remaining loan: {member['loan']:.2f}")    

def show_menu():
    print("\n--- Savings Tracker ---")
    print("1. Add a member")
    print("2. Record a contribution or loan")
    print("3. View one member")
    print("4. View all members")
    print("5. Calculate group total and average")
    print("6. Find highest or lowest contributor")
    print("7. Remove a member")
    print("8. Repay a loan")
    print("9. Exit")


def main():
    load_data()  # restore saved members at startup
    while True:
        show_menu()
        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            add_member()
        elif choice == "2":
            record_transaction()
        elif choice == "3":
            view_one_member()
        elif choice == "4":
            view_all_members()
        elif choice == "5":
            calculate_summary()
        elif choice == "6":
            find_extreme()
        elif choice == "7":
            remove_member()
        elif choice == "8":
            repay_loan()
        elif choice == "9":
            save_data()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 9.")
            continue

        save_data()  # save after every action


if __name__ == "__main__":
    main()

