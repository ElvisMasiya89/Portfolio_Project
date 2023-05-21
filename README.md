# Portfolio_Project
Portfolio_Project

# Django User Profiles Project

The Django User Profiles Project is a web application that allows users to create profiles, update their information, and view their own profile on a map. It includes features such as registration, login, profile editing, and a map view with user locations.

## Features

- User registration and login
- User profile creation and editing
- Map view displaying user locations
- Popup displaying user profile details on map marker click
- Access control: Users can only view and edit their own profile

## Technologies Used

- Django: a high-level Python web framework
- Django REST Framework: a powerful and flexible toolkit for building Web APIs
- PostgreSQL: an open-source relational database management system
- PostGIS: a spatial database extender for PostgreSQL
- Leaflet: an open-source JavaScript library for interactive maps
- GDAL: a translator library for raster and vector geospatial data formats
- PROJ: a library for cartographic projections and coordinate transformations
- HTML/CSS: for front-end design and styling

## Installation

1. Clone the repository:


2. Install the project dependencies:
   pip install -r requirements.txt
   

3. Set up the database with PostGIS:

- Install PostgreSQL and PostGIS using stackbuilder on your system following the relevant documentation for your operating system.
- Create a new PostgreSQL database for the project.


4. Create a `.env` file in the `portfolio_app` project folder with the following contents:

```plaintext
# .env file

# Database configuration
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=your_database_port


5. Install GDAL Python wheel:

- Visit the GDAL Python wheels repository at https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal
- Download the appropriate GDAL wheel file for your system (e.g., `GDAL-<version>-cp<python_version>-cp<python_version>-win_amd64.whl` for Windows).
- Install the GDAL wheel using pip:

  pip install path/to/GDAL-<version>-cp<python_version>-cp<python_version>-win_amd64.whl

6. Install PROJ Python wheel:

- Visit the PROJ Python wheels repository at https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyproj
- Download the appropriate PROJ wheel file for your system (e.g., `pyproj-<version>-cp<python_version>-cp<python_version>-win_amd64.whl` for Windows).
- Install the PROJ wheel using pip:
  
7. Run database migrations:
  -python manage.py makemigrations
  -python manage.py migrate
  
8. Create a superuser: 
   -python manage.py createsuperuser
  
9. Start the development server:  
   -python manage.py runserver
  

10. Access the Django admin site to create user profiles:

   - Open your web browser and go to `http://localhost:8000/admin`
   - Log in using the superuser credentials created in step 8.
   - Create user profiles by clicking on "User Profiles" and then "Add User Profile".
   - Enter the necessary information for each user and save the profiles.

11. Access the application at `http://localhost:8000` in your web browser.

## Configuration

The project includes a `.env` file where you can modify various settings such as database configuration, Make sure to update these settings according to your environment and preferences.

## Usage

- Registration: Users can create an account by providing their username, email, and password.
- Login: Registered users can log in using their username and password.
- Profile Editing: Once logged in, users can edit their profile information, including home address, phone number, and location coordinates.
- Map View: Users can view a map that shows the locations of all registered users. Clicking on a user's icon displays their profile in a popup.
- Accessing the Admin Site: To create and manage user profiles, access the Django admin site by going to `http://localhost:8000/admin` and logging in with superuser credentials.
- Initial Template: The initial template loaded is the login page. To create users and access the application, go to the admin URL mentioned above.
  


  
  

  





