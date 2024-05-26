# bookabo
Bookabo project for Vention internship 

# Django REST Framework Project

This is a Django project built using Django REST Framework (DRF) with PostgreSQL database.

## Setup

Follow these instructions to set up the project locally.

### Prerequisites

Make sure you have the following installed:

- Python (>= 3.6)
- pip (Python package installer)
- PostgreSQL (>= 9.5)

### Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd project-directory/

   
2. **Create a virtual environment**
   
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install dependencies**
   
   ```bash
   pip install -r requirements.txt
   
4. **Update the create_postgres_db.py according to your needs to create a db to connect and then run**
   
   ```bash
   python create_postgres_db.py


5.  **Create .env file with db credentials or change the DATABASE setting in settings.py**

6.  **And you are good to go!**
   
  ```bash
  python manage.py runserver

