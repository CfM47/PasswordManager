# Password Manager

Password Manager is a command-line application for securely managing accounts and cards. A fun project to test and implement diferent simple encrypting algorithms. It uses MongoDB to store data and provides functionalities to create, read, delete, and list entries.

## Installation

### Requirements

- Python 3.x
- MongoDB

### Clone the repository

```sh
git clone https://github.com/CfM47/password-manager.git
cd password-manager
```

### Create a virtual environment

```sh
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate  # On Windows
```

### Install dependencies

```sh
pip install rich pymongo tkinter
```

### Configure the database

Make sure MongoDB is running and properly configured. You can start MongoDB with the following command:

```sh
mongod --dbpath /path/to/your/db
```

### Set up the database

Run the database configuration script:

```sh
python config.py
```

This script will connect to MongoDB at `localhost:27017` and set up the necessary collections and user credentials.

## Overview

Password Manager allows you to securely manage accounts and cards. The functionalities include:

- Create new accounts and cards.
- Read details of accounts and cards.
- Delete accounts and cards.
- List names of accounts and cards.
- List full details of accounts and cards.

## Help

To get help on how to use the application, you can run the following command:

```sh
python main.py -h
```

## Instructions

### Create an entry

To create a new account or card, use the following command:

```sh
python main.py create account -n <account_name>
python main.py create card -n <card_name>
```

### Read an entry

To read the details of an account or card, use the following command:

```sh
python main.py read account -n <account_name>
python main.py read card -n <card_name>
```

### Delete an entry

To delete an account or card, use the following command:

```sh
python main.py delete account -n <account_name>
python main.py delete card -n <card_name>
```

### List entry names

To list the names of all accounts or cards, use the following command:

```sh
python main.py list account
python main.py list card
python main.py list all
```

### List full details of entries

To list the full details of all accounts or cards, use the following command:

```sh
python main.py list-details account
python main.py list-details card
python main.py list-details all
```

---

If you have any questions or suggestions, feel free to open an issue in the repository.
