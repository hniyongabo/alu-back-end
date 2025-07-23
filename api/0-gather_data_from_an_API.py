import requests

employee_id = int(input("Enter your employee ID: "))
#error handling
#if employee_id == invalid:
#  print("Invalid ID, please try again")
#else :
#  continue
url_users = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
response_user = requests.get(url_users)
data_user = response_user.json()
employee_name = data_user.get("name")

todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
todo_response = requests.get(todo_url)
todo_data = todo_response.json()

done_tasks = [task for task in todo_data if task["completed"] is True]

print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{len(todo_data)}):")
for task in done_tasks:
    print(f"\t {task['title']}")