# VersaToolbox

Welcome to VersaToolbox, your versatile and dynamic toolbox of small yet powerful utilities. This Django-based project is designed to streamline everyday tasks and enhance productivity. If you're a technology enthusiast and interested in collaborating on this project, I'm thrilled to invite you to join me.

## Project Overview

VersaToolbox offers a range of functionalities:

- **QR Code Scanner and Generator**
- **Youtube Video Downloader**
- **File Converter**
- **Zodiac Sign Calculator**
- **Cricket Live Score**
- **Phone Number Details**
- **Data Extraction from Image/PDF**
- **Plagarism Detector**
- **Fake Address Generator**
- **Quote Generator**
- **Recipe Generator**
- **Quiz**
- **Expense Tracker**
- **And More**

## Live Demo

You can access the live demo of VersaToolbox [here](https://versatoolbox.onrender.com/)

**Note**: Please be aware that the hosted version is running on the free version of PythonAnywhere. Due to infrequent code updates and limited third-party access, some features may not work as expected. For example, the YouTube video downloader may not function in the hosted link, but it works in the local environment. In the future, I will explore alternative hosting options to improve functionality and access.


Each utility is crafted to be user-friendly and efficient, making complex tasks simple. The project is continually evolving, and your expertise could be instrumental in taking VersaToolbox to new heights.


## Technologies Used

- Django
- Python
- Pandas
- NumPy
- Pytube
- Urlib


## Collaboration Invitation

I understand that time constraints can limit individual contributions. That's why I'm excited about the prospect of collaboration. Together, we can expand the capabilities of VersaToolbox and make it even more valuable to the community.

Feel free to reach out if you'd like to collaborate, contribute, or have innovative ideas to share. Your creativity and skills are highly welcome here.

The project is not just about utility but also about community and collaboration. Let's explore the endless possibilities together.

Don't hesitate to ping me if you're interested in joining this exciting journey!


## How to run

### 1. Clone the Repository

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/satheesh22g/VersaToolbox.git
cd VersaToolbox
```
### 2. Install Poetry (if not already installed)

If Poetry is not installed, follow the official installation guide:

[Poetry Installation Guide](https://python-poetry.org/docs/#installation)

For most systems (recommended), run:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```
### 3. Install Dependencies

Once Poetry is installed, use it to install the project dependencies:

```bash
poetry install
```

### 4. Apply Database Migrations

After installing the dependencies, run the following command to apply the database migrations:

```bash
poetry run python manage.py migrate
```

### 5. (Optional) Create a Superuser

If you need to access the Django Admin Panel, you can create a superuser by running the following command:

```bash
poetry run python manage.py createsuperuser

```
You will be prompted to enter the following details for the superuser:

- **Username**: The username you want to use for the admin account.
- **Email address**: The email address for the superuser.
- **Password**: The password for the superuser (you will need to enter it twice for confirmation).

### 6. Run the Development Server

To start the Django development server, use the following command:

```bash
poetry run python manage.py runserver
```

### 7. Open the App in Your Browser

Now that the server is running, open your web browser and visit:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

You should see the VersaToolbox app in your browser.

### 8. Access the Django Admin Panel (Optional)

If you created a superuser, you can log in to the Django Admin Panel by visiting:

[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

Use the superuser credentials you created to log in and manage the application.

---

