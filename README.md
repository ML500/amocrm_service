## Amocrm service
### Testing task:
Need to develop a backend for the service to work with the AmoCRM API

#### Requirement:
Implement a method that accepts a GET request with required parameters:
  - name **TEXT** - Full Name
  - email **TEXT** - Email 
  - phone **TEXT** - Phone number

Using this data, you need to find a contact in AmoCRM with this mail and (or) phone number. If not, create a new one by filling in the name, phone number and mail. If found, update it with incoming data. After that, create a deal for this contact in the first status of the funnel.

**Can be used:**

- Django framework
- Docker

**Can not use:**

- Libraries for AmoCRM

### The project used
- Django==3.2.9
- djangorestframework==3.12.4
- requests==2.26.0

### Installation
1. Create and go to the folder where you will deploy the application
2. Clone the application from
  - https://github.com/ML500/amocrm_service
3. Create a virtual environment
  - python3 -m virtualenv -p python3 venv
4. Activate the virtual environment
  -. venv / bin / activate
5. Install dependencies
  - pip install -r requirements.txt
6. Need to install ngrok for delivery to remote server
  - https://ngrok.com/
7. Start ngrok server in terminal
  - ngrok http http://127.0.0.1:8000/
