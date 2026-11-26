# Savings Tracker

## Purpose
A command-line app that helps a small savings group (chama) keep track of
its members, their contributions and their loans.

## What the program does
- Add a member (name and unique ID)
- Record a contribution or a loan for a member
- View one member or all members
- Calculate the group's total savings, average and total loans
- Find the highest or lowest contributor
- Remove a member
- Handles empty data, missing members and invalid input

## Setup
1. Install Python 3 from python.org.
2. Clone this repository:
   `git clone https://github.com/[your-username]/[repo-name].git`
3. Open the folder: `cd [repo-name]`

## How to run
`python src/savings.py`

## Example input and output
```
--- Savings Tracker ---
1. Add a member
...
Enter your choice (1-8): 1
Enter member name: Amina
Enter member ID: 101
Amina added successfully.

Enter your choice (1-8): 2
Enter member ID: 101
1. Contribution
2. Loan
Choose 1 or 2: 1
Contribution amount (KSh): 500
Recorded 500.00 for Amina.

Enter your choice (1-8): 5
Members: 1
Total savings: 500.00
Average per member: 500.00
Total loans: 0.00
```

## Data structures
- `members`: a list of dictionaries, one per member
  (`id`, `name`, `contributions`, `loan`)
- `member_ids`: a set used to stop duplicate IDs

## Manual testing
| Test case | Input | Expected result | Result |
|---|---|---|---|
| Empty collection | Option 4 with no members | "No members yet." | [Pass/Fail] |
| Add valid member | ID 101, name Amina | Added successfully | [Pass/Fail] |
| Add duplicate ID | ID 101 again | "ID already exists" | [Pass/Fail] |
| Invalid amount | "abc" | Asked again | [Pass/Fail] |
| Search existing | Option 3, ID 101 | Details shown | [Pass/Fail] |
| Search missing | Option 3, ID 999 | "Member not found." | [Pass/Fail] |
| Update member | Add 500 contribution | Savings becomes 500.00 | [Pass/Fail] |
| Total and average | Option 5 | Correct values | [Pass/Fail] |
| Highest value | Option 6, choice 1 | Correct member | [Pass/Fail] |
| Lowest value | Option 6, choice 2 | Correct member | [Pass/Fail] |
| Remove member | Option 7, ID 102 | Member removed | [Pass/Fail] |
| Invalid menu choice | "9" | Error message | [Pass/Fail] |
| Exit | Option 8 | "Goodbye!" and program ends | [Pass/Fail] |

## Learning goals
- Organize a project with folders and Git
- Use functions, loops and if/elif/else
- Store and process data with lists, dictionaries and sets

## Reflection
[Write 4-5 sentences in your own words: what you learned, what was
difficult, and what you would improve.]

