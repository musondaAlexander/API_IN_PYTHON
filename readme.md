This project is about a simple social media web Api for:
Note : I am developing this API for Educational purposes only Feel free to clone this repo  and made modifications that suits your business Need.

1. Adding a post to the databse
2. Retrieving a post from The databases or messages
3. Updating a post
4. Deleting a post from the database.
5. Rate a Post 
6. Add a user HWo can log in and generate a Token to use for accessing the API.
   It supports the basic CRUD Operations
   which are performed using HTTP methods.
   it is written in Python using simple API. The database am using for this API is postgress. The version of python is 3.10,      testing of the API is through a web browser as Simple API provides Documentation for your API and also Postman desktop.
   I am yet to publish the url once the project is fully complete which can used By anyone that finds it useful.

   ===============================================================================
   # Path: API_IN_PYTHON\requirements.txt contains the following:
   package==version

   ===============================================================================
   # Path: API_IN_PYTHON\practice contains the following:
   code that is written using raw SQL and python to practice the basic crud functionalities.

   ===============================================================================
   # Path: API_IN_PYTHON\ormcode contains the following:
   code that is written using ORM and python to practice the basic crud functionalities.
   ===============================================================================
   # Path: API_IN_PYTHON\mymodels\utils.py contains the following:
   contains te function that is used for Hashing the password.
   ===============================================================================
   # Path: API_IN_PYTHON\mymodels\user.py contains the following:
   contains the user model that is used for creating the user table in the database.
   ===============================================================================
   # Path: API_IN_PYTHON\ormcode\routers\post.py contains the following:
   conatins the code that is used for making post and get request to the database.
   about the post that the user has made.
   ===============================================================================
   # Path: API_IN_PYTHON\ormcode\auth2.py contains the following:
   contains the code that is used for gerating a token for the user.
   ===============================================================================
   # Path: API_IN_PYTHON\ormcode\routers\mainmodels.py contains the following:
   contains the code that is used to call the two routers that is post and user.
   this is the main file that is used to run the code.
   ===============================================================================
   # Path: API_IN_PYTHON\ormcode\routers\user.py contains the following:
   conatins the code that is used for making post and get request to the database.
   to retrieve the user details.
   ===============================================================================
   # To run the code in the api folder: API_IN_PYTHON\ormcode\
   1. Open the terminal
   2. cd to the folder
   3. run the command: uvicorn mainmodels:app --reload

   ===============================================================================
   # To run the code in the api folder: API_IN_PYTHON\practice\
   1. Open the terminal
   2. cd to the folder
   3. run the command: uvicorn main:app --reload
   ================================================================================
   Make sure you have the following installed:
   1. Python
   2. Postgress
   3. Postman
   4. Uvicorn
   5. Fastapi
   6. SQLAlchemy
   7. Pydantic
   8. bcrypt
   9. passlib
   10. psycopg2
   11. python-dotenv
   12. python-multipart
   13. requests
   14. uvicorn
   15. jinja2
   16. starlette 
   17. or
   you can install all the above using the command: pip install -r requirements.txt
   this will install all the above packages and many more.
   ================================================================================





