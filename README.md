# Roomier

A simple, responsive  website developed to help the customer for booking time slot as per the requirement. It also allows the manager to provide room on rent.

### Getting Started

A customize website which helps customer to aid customer to book time slot and it also allows the manager to provide room on rent for particular time slot. 

### Features

##### Types Of User:
 - Customer
 - Manager
 - Admin
    
##### User
 - New user can create account.
 - Existing user can log in.
 - User can change password, edit profile.
 - User can reset password followed by email confirmation.
  
##### Room Manager
 - Room Manager can add, delete or change room details and Time Slots details.
 - Room Manager can view bookings and cancelled booking booked by customer.
 - By default the number of days 'x' is initialized to 15 days.
 - Room Manager can edit the number of days 'x' to book in advance.

##### Customer
 - A Customer can book Time Slot, once booked, the time slotslot cannot be booked by another Customer for the same day.
 - A Customer is restricated to book a Room 'x' days in advance.
 - A Customer can view and cancel his own bookings.
 - The customer can view all bookings as well as cancelled bookings.

### Prerequisites
```
Python 3 and higher version.
Django 2.1.7
```

### Installing
1. How to install virtualenv
```
$ pip3 install virtualenv 
$ virtualenv -p /usr/bin/python3 env
$ source env/bin/activate
```

2. Installing requirements
```
$ pip3 install -r requirement.txt
```

3. Change directory to book_room
```
$ cd book_room
$ python3 manage.py makemigrations accounts
$ python3 manage.py makemigrations manager
$ python3 manage.py makemigrations customer
$ python3 manage.py migrate
$ python3 manage.py collectstatic
```

4.  Running
Run the application, running on localhost.
```
$ python3 manage.py runserver
```
open [localhost](http://127.0.0.1:8000/) in browser.

5. Testing Reset Password feature using Django Email Server
* Starting the email server in another terminal
```
python3 -m smtpd -n -c DebuggingServer localhost:1025
```
* open [Reset Password](http://127.0.0.1:8000/accounts/password_reset/) in browser
* Enter email address to reset password
* open terminal to check for email.

### Running the tests
```
$ python3 manage.py test
```



### API Endpoints

#### 1. Accounts Endpoints

i. Create Manager
```
$ curl -X POST -H "Content-Type: application/json" -H 'Accept: application/json; indent=4' --data '{ "username":"user_username", "first_name":"user_first_name", "last_name":"user_last_name", "email":"test@gmail.comm", "phone":"1234569845", "password":"secret_pass"}' http://127.0.0.1:8000/api/accounts/create_manager/ 
{
    "username": "user_username",
    "first_name": "user_first_name",
    "last_name": "user_last_name",
    "email": "test@gmail.comm",
    "phone": "1234569845"
}
```

ii. Create Customer
```
$ curl -X POST -H "Content-Type: application/json" -H 'Accept: application/json; indent=4' --data '{ "username":"user_username1", "first_name":"user_first_name1", "last_name":"user_last_name1", "email":"test1@gmail.comm", "phone":"3453216587", "password":"secret_pass1"}' http://127.0.0.1:8000/api/accounts/create_customer/
{
    "username": "user_username1",
    "first_name": "user_first_name1",
    "last_name": "user_last_name1",
    "email": "test1@gmail.comm",
    "phone": "3453216587"
}
```

iii. Login
```
$ TOKEN=$(curl -X POST --data '{"username":"user_username", "password":"secret_pass"}' -H "Content-Type: application/json" -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/accounts/login/ | jq -r '.token')
{
  "token": "f7b5c35e19c58fcdf38567750084a8350b937f69"
}
Use this token for authorization of user and use this with ('Token '+token) format.
```

iv. Logout
```
$ curl -X POST -H 'Accept: application/json; indent=4' -H 'Authorization: Token '"$TOKEN"'' http://127.0.0.1:8000/api/accounts/logout/
{
  "result": "Successfully Logout."
}
```

v. Get User Profile
```
$ curl -X GET -H 'Accept: application/json; indent=4' -H 'Authorization: Token '"$TOKEN"'' http://127.0.0.1:8000/api/accounts/profile/
{
    "username": "user_username",
    "first_name": "user_first_name",
    "last_name": "user_last_name",
    "email": "test@gmail.com",
    "phone": "1234569845"
}
```

vi. Edit User Profile
```
$ curl -X PUT  -H "Content-Type: application/json" -H 'Accept: application/json; indent=4' -H 'Authorization: Token '"$TOKEN"''  http://127.0.0.1:8000/api/accounts/edit_profile/ --data '{ "username":"edit_username", "first_name":"edit_first_name", "last_name":"edit_last_name", "email":"edit_test@gmail.com", "phone":"1234569845"}'
{
    "first_name": "edit_first_name",
    "last_name": "edit_last_name",
    "email": "edit_test@gmail.com",
    "phone": "1234569845"
}
```

vii. Change Password
```
$ curl -X PUT --data '{"old_password":"secret_pass", "new_password":"secret_pass_edit"}' -H "Content-Type: application/json" -H 'Accept: application/json; indent=4' -H 'Authorization: Token '"$TOKEN"''  http://127.0.0.1:8000/api/accounts/edit_password/
{
    "success": "updated password."
}
Login again with new password to obtain new token.
```

2. Manager Endpoints
Execute command and store output into variable

```
$ TOKEN=$(curl -X POST -d username=user_username -d password=secret_pass -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/accounts/login/ | jq -r '.token')
check whether password is correct or not because change password api endpoint changes the password.
````
i. Create Room
```
$ curl -X POST -d room_name=new_room -H 'Accept: application/json; indent=4' -H 'Authorization: Token '"$TOKEN"'' http://127.0.0.1:8000/api/manager/room/create/
{
   "id": "51413e46-e9ad-4316-a05b-93a755433681",
   "url": "http://127.0.0.1:8000/api/manager/room/51413e46-e9ad-4316-a05b-93a755433681/",
   "room_name": "new_room"
}
```

ii. Room List
```
$ curl -X GET -H 'Authorization: Token '"$TOKEN"'' -H 'Accept: application/json; indent=4;' http://127.0.0.1:8000/api/manager/room/
[
    {
        "id": "51413e46-e9ad-4316-a05b-93a755433681",
        "url": "http://127.0.0.1:8000/api/manager/room/51413e46-e9ad-4316-a05b-93a755433681/",
        "room_name": "new_room"
    }
]
```

iii. Room Delete
```
$ curl -X DELETE -H 'Authorization: Token '"$TOKEN"'' -H 'Accept: application/json; indent=4;' http://127.0.0.1:8000/api/manager/room/51413e46-e9ad-4316-a05b-93a755433681/delete/
URL format : http://127.0.0.1:8000/api/manager/room//delete/
```

iv. Create Time Slot
```
$ curl -X POST -d start_time=12:00:00 -d end_time=03:00:00 -H 'Accept: application/json; indent4' -H 'Authorization: Token '"$TOKEN"'' http://127.0.0.1:8000/api/manager/room/51413e46-e9ad-4316-a05b-93a755433681/slot/create/
{
  "id":"49054e8d-c936-4c42-b511-3425df8644e1",
  "start_time":"12:00:00",
  "end_time":"03:00:00"
}
URL format : http://127.0.0.1:8000/api/manager/room//slot/create/
```

v. Time Slot List Corresponding to room_id
```
$ curl -X GET -H 'Authorization: Token '"$TOKEN"'' -H 'Accept: application/json; indent=4;' http://127.0.0.1:8000/api/manager/room/51413e46-e9ad-4316-a05b-93a755433681/
[
    {
        "id": "49054e8d-c936-4c42-b511-3425df8644e1",
        "start_time": "12:00:00",
        "end_time": "03:00:00"
    }
]
URL format : http://127.0.0.1:8000/api/manager/room//
```

vi. Time Slot Edit
```
$ curl -X PUT -d start_time=04:00:00 -d end_time=07:00:00 -H 'Authorization: Token '"$TOKEN"'' -H 'Accept: application/json; indent=4;' http://127.0.0.1:8000/api/manager/room/51413e46-e9ad-4316-a05b-93a755433681/slot/49054e8d-c936-4c42-b511-3425df8644e1/edit/
{
    "id": "49054e8d-c936-4c42-b511-3425df8644e1",
    "start_time": "04:00:00",
    "end_time": "07:00:00"
}
URL format : http://127.0.0.1:8000/api/manager/room/room_id/slot/slot_id/edit/
```

vii. Time Slot Delete
```
$ curl -X DELETE -H 'Authorization: Token '"$TOKEN"'' -H 'Accept: application/json; indent=4;' http://127.0.0.1:8000/api/manager/room/51413e46-e9ad-4316-a05b-93a755433681/slot/49054e8d-c936-4c42-b511-3425df8644e1/delete/
URL format : url format : http://127.0.0.1:8000/api/manager/room/room_id/slot/slot_id/edit/
```

viii. Booked Time Slot History
```
$ curl -X GET -H 'Authorization: Token '"$TOKEN"'' -H 'Accept: application/json; indent=4;' http://127.0.0.1:8000/api/manager/bookedtimeslot/
[]
```

ix. Cancelled Time Slot History
```
$ curl -X GET -H 'Authorization: Token '"$TOKEN"'' -H 'Accept: application/json; indent=4;' http://127.0.0.1:8000/api/manager/cancelledtimeslot/
[]
```

x. Edit no. of days to book in advance
```
$ curl -X POST -d no_of_days=50 -H 'Authorization: Token '"$TOKEN"'' -H 'Accept: application/json; indent=4;' http://127.0.0.1:8000/api/manager/edit_advance_days/
{
    "message": "Updated Successfully."
}
```

3. Customer Endpoints
Execute command and store output into variable
```
$ TOKEN=$(curl -X POST -d username=user_username1 -d password=secret_pass1 -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/accounts/login/ | jq -r '.token')
```

i. Search Time Slot
```
$ curl -X GET -H 'Authorization: Token '"$TOKEN"'' -H 'Accept: application/json; indent=4;' 'http://127.0.0.1:8000/api/customer/search/?date=2020-03-30&start_time=04%3A00&end_time=07%3A00'
[
    {
        "id": "e7a820f8-6632-4926-9d03-b28c5a62b168",
        "room_id": "9fc977c8-9fee-42e9-b6d9-05888fe7e095",
        "time_slot_owner": "0e57f845-1f75-403a-ba12-9a2d93c1d4cd",
        "start_time": "04:00:00",
        "end_time": "07:00:00",
        "date": "2020-03-30"
    }
]
```

ii. Book Time Slot
```
$ curl -X POST -d manager_id=0e57f845-1f75-403a-ba12-9a2d93c1d4cd -d start_time=03:00:00 -d end_time=06:00:00 -d date=2020-03-10 -d room_id=9fc977c8-9fee-42e9-b6d9-05888fe7e095 -H 'Authorization: Token '"$TOKEN"'' -H 'Accept: application/json; indent=4;' http://127.0.0.1:8000/api/customer/book/
{
    "manager_id": "0e57f845-1f75-403a-ba12-9a2d93c1d4cd",
    "date": "2020-03-10",
    "start_time": "03:00:00",
    "end_time": "06:00:00",
    "room_id": "9fc977c8-9fee-42e9-b6d9-05888fe7e095"
}
```

iii. Cancel Book Slot
```
$ curl -X POST -d manager_id=0e57f845-1f75-403a-ba12-9a2d93c1d4cd -d start_time=03:00:00 -d end_time=06:00:00 -d date=2020-03-10 -d room_id=9fc977c8-9fee-42e9-b6d9-05888fe7e095 -H 'Authorization: Token '"$TOKEN"'' -H 'Accept: application/json; indent=4;' http://127.0.0.1:8000/api/customer/cancel/
{
    "manager_id": "0e57f845-1f75-403a-ba12-9a2d93c1d4cd",
    "date": "2020-03-10",
    "room_id": "9fc977c8-9fee-42e9-b6d9-05888fe7e095",
    "start_time": "03:00:00",
    "end_time": "06:00:00"
}
```

iv. Booked Time Slot History
```
$ curl -X GET -H 'Authorization: Token '"$TOKEN"'' -H 'Accept: application/json; indent=4;' http://127.0.0.1:8000/api/customer/booked/
[
    {
        "customer_id": "e4e4c051-8e73-48c3-950f-0f264935e45e",
        "date": "2020-03-16",
        "room_id": "9fc977c8-9fee-42e9-b6d9-05888fe7e095",
        "start_time": "03:00:00",
        "end_time": "06:00:00"
    }
]
```

v. Cancelled Time Slot History
```
$ curl -X GET -H 'Authorization: Token '"$TOKEN"'' -H 'Accept: application/json; indent=4;' http://127.0.0.1:8000/api/customer/cancelled/
[
    {
        "customer_id": "e4e4c051-8e73-48c3-950f-0f264935e45e",
        "date": "2020-03-16",
        "room_id": "9fc977c8-9fee-42e9-b6d9-05888fe7e095",
        "start_time": "03:00:00",
        "end_time": "06:00:00"
    }
]
```
