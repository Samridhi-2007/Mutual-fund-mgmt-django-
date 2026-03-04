# Mutual Fund Awareness Platform

Django web application for mutual fund comparison, investment education, and advisor guidance.

## Roles
- `ADMIN`: manages fund data and advisor records.
- `ADVISOR`: provides guidance and manages educational articles.
- `INVESTOR`: explores funds, comparison, and education content (read-only).

## Local Setup
1. Create and activate virtual environment.
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Run migrations:
   - `python manage.py migrate`
4. Start server:
   - `python manage.py runserver`

## MySQL Configuration
The project uses SQLite by default. To switch to MySQL, set environment variables:

- `USE_MYSQL=true`
- `MYSQL_NAME=mutualfund_platform`
- `MYSQL_USER=root`
- `MYSQL_PASSWORD=your_password`
- `MYSQL_HOST=localhost`
- `MYSQL_PORT=3306`

Then run:
- `python manage.py migrate`

## Default URLs
- `/` home
- `/funds/` funds and comparison
- `/education/` educational articles
- `/advisors/` advisors
- `/register/`, `/login/`, `/dashboard/`
