# alu-back-end
This Python script uses a REST API to display the TODO list progress of a given employee.

## Description

The script connects to the public API at jsonplaceholder.typicode.com and does the following:

- Asks the user for an employee ID (an integer from 1 to 10).
- Fetches the employee’s name.
- Fetches all the tasks (TODOs) assigned to that employee.
- Counts how many tasks are completed.
- Prints a progress summary and the titles of the completed tasks, formatted nicely.

## How to Run the Script

1. Make sure you have Python 3 installed.
2. Make sure the `requests` module is installed:
   pip install requests

3. Save the script as `todo_progress.py` (already done by this setup).
4. Run it in your terminal:
   python3 todo_progress.py

5. When prompted, enter an employee ID between 1 and 10.

## Example Output

Enter the employee ID: 2  
Employee Ervin Howell is done with tasks(8/20):  
     distinctio vitae autem nihil ut molestias quo  
     voluptas quo tenetur perspiciatis explicabo natus  
     aliquam aut quasi  
     veritatis pariatur delectus  
     nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis  
     repellendus veritatis molestias dicta incidunt  
     excepturi deleniti adipisci voluptatem et neque optio illum ad  
     totam atque quo nesciunt  

## Notes

- Employee IDs range from 1 to 10 on this demo API.
- This script is for educational purposes and works with a mock API (no real data).
- Make sure to have an internet connection when running the script.

## API Used

- https://jsonplaceholder.typicode.com/users/{id}
- https://jsonplaceholder.typicode.com/todos?userId={id}
EOF
