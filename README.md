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
$ sudo pip install virtualenv 
$ virtualenv env 
$ source env/bin/activate
```

2. Installing requirements
```
$ pip install -r requirement.txt
```

3. Change directory to book_room
```
$ cd book_room
$ python manage.py makemigrations accounts
$ python manage.py makemigrations manager
$ python manage.py makemigrations customer
$ python manage.py migrate
```

4.  Running
Run the application, running on localhost.
```
$ python manage.py runserver
```
open [localhost](http://127.0.0.1:8000/) in browser.

5. Testing Reset Password feature using Django Email Server
* Starting the email server in another terminal
```
python -m smtpd -n -c DebuggingServer localhost:1025
```
* open [Reset Password](http://127.0.0.1:8000/accounts/password_reset/) in browser
* Enter email address to reset password
* open terminal to check for email.

### Running the tests
```
$ python manage.py test
```
