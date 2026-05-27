# Healthcare Management System (Novena Hospital) - Project Synopsis

## Project Overview
This is a comprehensive Django-based healthcare management system designed for a hospital named "Novena Hospital". The application enables patients to explore medical departments, view doctor profiles, book appointments, and submit health-related queries. It also provides hospital administrators with tools to manage departments, doctors, and patient appointments through a Django admin interface.

## Technology Stack
- **Backend Framework**: Django 5.2.7
- **Database**: SQLite (db.sqlite3) / MySQL compatible
- **Frontend**: HTML5, CSS3 (with SCSS), JavaScript
- **Image Processing**: Pillow 12.0.0
- **Email Service**: Built-in Django mail functionality
- **File Upload**: Django ImageField
- **Additional Tools**: Bootstrap framework, jQuery, Slick carousel, Counter-up plugin

## Project Structure

### Django Application Layout
```
health_care_1/ (Main project folder)
├── health/ (Main Django app)
│   ├── models.py (Database models)
│   ├── views.py (Business logic & request handling)
│   ├── urls.py (URL routing)
│   ├── admin.py (Admin interface configuration)
│   ├── apps.py (App configuration)
│   └── migrations/ (Database schema versions)
├── health_care_1/ (Project settings)
│   ├── settings.py (Project configuration)
│   ├── urls.py (Main URL dispatcher)
│   ├── asgi.py (ASGI config)
│   └── wsgi.py (WSGI config)
├── templates/ (HTML templates)
├── static/ (CSS, JavaScript, Images)
└── media/ (User-uploaded files)
```

## Database Models

### 1. Department Model
Represents hospital departments with:
- department_name (CharField, max 150 chars)
- department_description (TextField)
- department_image (ImageField - stored in media/department/)

### 2. DoctorDetail Model
Stores doctor information with:
- doctor_full_name, gender, age, education_status, work_experience
- department_name (ForeignKey to Department)
- email, mobile_number, doctor_description
- available_work_hours, state, city
- doctor_image (ImageField - stored in media/doctor/)

### 3. AppointmentDetails Model
Records patient appointments with:
- doctor_name, patient_name, patient_email, patient_mobile_number
- appointment_date, appointment_time
- prescription (ImageField - optional, stored in media/prescription/)
- message (Patient notes/message)

### 4. Queries Model
Stores patient inquiries with:
- name, email, subject, phone, message

Database uses 8 migration files tracking schema evolution from initial setup through adding appointments and queries.

## Core Features & Functionality

### 1. Home Page (index view)
- Displays all hospital departments
- Features appointment booking form integrated on homepage
- Processes appointment form submissions
- Redirects to confirmation page after successful booking

### 2. Department Management
- Browse all hospital departments
- View department descriptions and images
- Filter doctors by department

### 3. Doctor Management
- View all doctors with full profiles
- Single doctor detail page with complete information
- Doctor profiles include: qualifications, experience, location, contact info
- Doctor images and department associations
- AJAX functionality to dynamically fetch doctors by department

### 4. Appointment Booking System
- Form to book appointments with specific doctors
- Automatic email notifications:
  - Confirmation email sent to patient
  - Appointment notification sent to assigned doctor
- Appointment date & time validation via JavaScript
- File upload for prescription/medical documents
- Session-based appointment tracking (stores appointment ID in session)
- Confirmation page displayed after successful booking

### 5. Contact & Queries
- Contact form for patient inquiries
- Query submission with name, email, subject, phone, message
- Queries stored in database for administrative review

### 6. About Page
- Displays list of all hospital doctors with their details

### 7. Service Page
- Hospital services information

## URL Endpoints

| URL | View | Purpose |
|-----|------|---------|
| / | index | Homepage with departments & appointments |
| /about-us/ | about | About hospital & doctor listings |
| /contact-us/ | contact | Contact form & queries |
| /service/ | service | Hospital services description |
| /all-doctor/<id> | all_doctors | List doctors in department |
| /doctor-single/<id> | single_doctor_details | Individual doctor profile |
| /appointment | appointment_book | General appointment booking |
| /appointment/<id> | appointment_book | Doctor-specific appointment |
| /confirmation | confirmation | Appointment confirmation page |
| /subscribe/ | subscribe_newsletter | Newsletter subscription |
| /get-doctor-department-name-ajax/ | get_doctors | AJAX endpoint for department filtering |

## Frontend Components

### Templates
- base.html: Base layout template with navigation & footer
- index.html: Homepage with department showcase
- about.html: About page with team/doctor listings
- contact.html: Contact form
- service.html: Services offered
- appointment.html: Appointment booking form
- doctor_single_details.html: Individual doctor profile
- all_doctors.html: Filtered doctor listing
- confirmation.html: Appointment confirmation page
- header.html & footer.html: Reusable components

### Static Files
- **CSS**: SCSS-based styling with Bootstrap integration
- **JavaScript**: 
  - date_time_restriction.js: Validates appointment dates/times
  - contact.js: Contact form handling
  - script.js: General functionality & AJAX calls
- **Images**: department, doctor, blog, service, team, backgrounds
- **Plugins**: Bootstrap, jQuery, Slick carousel, Counter-up, Font icons

## Key Features in Implementation

### Email Notifications
- SMTP configured via Django settings (EMAIL_HOST_USER)
- Automatic confirmation emails to patients
- Doctor notification emails
- Error handling for email failures (displays warning messages)

### Form Processing
- POST request handling for appointments, contacts, queries
- Form validation and error messages
- File upload handling for prescriptions
- Success/error message display using Django messages framework

### AJAX Functionality
- Dynamic doctor filtering based on selected department
- Asynchronous data retrieval without page reload
- JSON response format for data exchange

### Data Validation
- Date/time restrictions for future appointments only
- Mobile number validation
- Email format validation
- Required field validation

## Admin Interface
Django admin configured via admin.py:
- Manage Departments (add/edit/delete)
- Manage Doctor Details (complete profiles)
- Manage Appointments (view/edit patient bookings)
- Manage Queries (view patient inquiries)

## File Storage
- **Media**: Uploaded images stored in media/ folder
  - department/ - Department images
  - doctor/ - Doctor profile pictures
  - prescription/ - Patient prescription uploads
- **Static**: CSS, JS, images stored in static/ folder (organized by type)

## Database Persistence
- SQLite database (db.sqlite3) for development
- MySQL compatibility for production deployment
- 8 migration versions tracking evolving schema

## Security & Best Practices
- Django ORM for SQL injection prevention
- CSRF token protection on forms
- Session management for appointment tracking
- Email error handling prevents application crashes
- ImageField for secure media uploads

## Project Status
This is a functional healthcare management system with core features implemented and ready for deployment. The system successfully handles patient appointments, doctor management, and hospital information dissemination through a user-friendly web interface with administrative backend.

## Dependencies Summary
Key Python packages: Django, Pillow, PyMySQL, FastAPI, Pydantic, Jinja2, html5lib, libsass

---
**Project Type**: Educational Healthcare Management System
**Framework**: Django MVT (Model-View-Template)
**Created For**: Semester 6 Training Project
