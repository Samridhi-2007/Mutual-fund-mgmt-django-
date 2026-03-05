# Mutual Fund Awareness & Investment Platform

### PFSD Course Project

This project is being developed as part of the **PFSD (Full Stack Development) course**. The objective of this project is to build a **Mutual Fund Awareness and Investment Platform** that helps users learn about mutual funds, compare investment options, and receive guidance from financial advisors.

The platform aims to improve financial literacy and assist investors in making informed decisions through educational resources and fund comparison tools.

---

## Mutual Fund Awareness Platform

Django web application for mutual fund comparison, investment education, and advisor guidance.

## Roles

* **ADMIN**: manages fund data and advisor records.
* **ADVISOR**: provides guidance and manages educational articles.
* **INVESTOR**: explores funds, comparison, and education content (read-only).

## Local Setup

1. Create and activate virtual environment.
2. Install dependencies:

   * `pip install -r requirements.txt`
3. Run migrations:

   * `python manage.py migrate`
4. Start server:

   * `python manage.py runserver`

## MySQL Configuration

The project uses SQLite by default. To switch to MySQL, set environment variables:

* `USE_MYSQL=true`
* `MYSQL_NAME=mutualfund_platform`
* `MYSQL_USER=root`
* `MYSQL_PASSWORD=your_password`
* `MYSQL_HOST=localhost`
* `MYSQL_PORT=3306`

Then run:

* `python manage.py migrate`

## Default URLs

* `/` home
* `/funds/` funds and comparison
* `/education/` educational articles
* `/advisors/` advisors
* `/register/`, `/login/`, `/dashboard/`
