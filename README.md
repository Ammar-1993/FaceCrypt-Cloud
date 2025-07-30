# FaceCrypt-Cloud

A **Smart Cloud-based Facial Recognition Authentication System**\
*Secure. Scalable. Seamless.*

---

## Table of Contents

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Screenshots](#screenshots)
- [Technology Stack](#technology-stack)
- [Database Design](#database-design)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Security & Privacy](#security--privacy)
- [Challenges & Solutions](#challenges--solutions)
- [Future Work](#future-work)
- [Contributors](#contributors)
- [License](#license)

---

## Project Overview

**FaceCrypt-Cloud** is an advanced web-based authentication system that replaces traditional password logins with secure, user-friendly biometric facial recognition. It leverages artificial intelligence for facial encoding, a Flask-based backend, and Google Firebase for cloud storage and real-time user management.

The system is designed for organizations and websites seeking to modernize their security, eliminate password-related vulnerabilities, and provide a frictionless login experience for end-users.

---

## Key Features

- **Biometric Authentication:** Secure, passwordless login using state-of-the-art facial recognition.
- **Admin Dashboard:** Powerful admin interface for managing users, monitoring access, and reviewing security logs.
- **Audit Logging:** Comprehensive logging of every login attempt (success/failure), timestamp, and IP address.
- **Cloud Integration:** Centralized storage and management of user data, face encodings, and audit logs via Firebase Firestore & Storage.
- **Blocking & Security Controls:** Automatic account blocking after multiple failed attempts, with support for temporary and permanent blocks.
- **Responsive Web Interfaces:** Modern, intuitive UI for both admins and users, supporting camera capture and file uploads.
- **Scalable & Modular:** Built with maintainability and extensibility in mind, ready for integration with other biometric methods or security features.

---

## System Architecture

```
[User] <---(Web Browser)---> [Flask Backend API] <---(Python ML & Auth Logic)---> [Firebase (Firestore & Storage)]
                                                                                   ^
[Admin] <---(Admin Portal)---------------------------------------------------------|
```

- **Frontend:** Responsive HTML/CSS/JS interfaces for users and admins.
- **Backend:** Python Flask app processes images, handles logic, and communicates with Firebase.
- **Face Recognition:** Uses `face_recognition` (built on dlib) for feature extraction and matching.
- **Cloud Services:** Firebase Firestore (user data & logs) and Firebase Storage (face images).

---

## Screenshots

> *Admin Login Interface
A secure login interface for administrators, allowing the system administrator to access the central control panel by entering only the secret password.*
> <img width="919" height="424" alt="image" src="https://github.com/user-attachments/assets/095193a7-ef4c-48c5-b7ba-852f0c1d804d" />



---

## Technology Stack

- **Backend:** Python 3.10, Flask, face\_recognition, dlib, OpenCV, Pillow
- **Frontend:** HTML5, CSS3, Bootstrap, JavaScript
- **Database & Cloud:** Google Firebase Firestore (NoSQL), Firebase Storage
- **Other:** dotenv (.env), pytest (for testing)

---

## Database Design

### Firestore Collections

- **Users**
  - `user_id` (string, PK)
  - `name`, `email`
  - `face_encoding` (biometric data)
  - `failed_attempts` (int)
  - `blocked` (bool), `soft_block` (bool), `soft_block_time` (timestamp)
- **Admins**
  - `adminID` (string, PK)
  - `passwordHash` (hashed, never stored as plain text)
- **AuditLogs**
  - `log_id` (string, PK)
  - `event`, `status`, `ip_address`, `timestamp`, `user_id`
- **Uploads**
  - `upload_id` (string, PK)
  - `url` (Firebase Storage link), `user_id`

---

## Setup & Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/facecrypt-cloud.git
   cd facecrypt-cloud
   ```

2. **Install Dependencies**

   - Make sure you have Python 3.10+ installed.
   - Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   - Install dlib (if not already present):

   ```bash
   pip install ./dlib-19.22.99-cp310-cp310-win_amd64.whl
   ```

3. **Configure Firebase**

   - Place your `serviceAccountKey.json` file in the `firebase/` directory.
   - Set up your `.env` file (see `.env.example`) for environment variables such as admin password, Firebase config, etc.

4. **Run the Application**

   ```bash
   python app.py
   ```

   - Visit [http://127.0.0.1:8080](http://127.0.0.1:8080) in your browser.

---

## Usage

- **Admin Portal:** Login as admin to add/delete users, review statistics, and audit logs.
- **User Portal:** Users login with facial recognition by capturing or uploading their photo.
- **Audit Log:** Every access attempt is recorded and can be reviewed by admins.

---

## Security & Privacy

- **No plain-text passwords:** Only secure hashes and face encodings are stored.
- **All facial data and sensitive information are encrypted and access-controlled via Firebase security rules.**
- **Sensitive credentials are stored in environment variables (**``**) and never hardcoded.**
- **Audit logging for traceability and incident analysis.**
- **Temporary and permanent blocking mechanisms to prevent brute-force attacks.**
- **Compliance with privacy guidelines: User consent required for storing biometric data.**

---

## Challenges & Solutions

- **Lighting and Image Quality:** The system includes handling for varied lighting and supports user guidance for better recognition.
- **Privacy Concerns:** All face data is encrypted; only encodings (not raw images) are used for authentication.
- **Blocking & Abuse Prevention:** Automatic temporary/permanent blocks on multiple failed attempts.
- **Extensibility:** Modular design enables future addition of multi-factor authentication or other biometric methods (voice, fingerprint).

---

## Future Work

- Support for additional biometric modalities (voice, fingerprint).
- Multi-factor authentication (MFA).
- Improved facial detection in low light or with occlusions.
- API endpoints for third-party integrations.
- Advanced admin analytics.

---

## Contributors

- Mohammed Harmal Alqahtani
- Mohammed Alelyani
- Waleed Abdullah Al-Attaf
- Haitham Hamad Al-Alyani
- Faris Jamaan Al-Shahrani
- Rakan Nayef Fahad Al-Quraishi
- Mohammed Abdurrahman Alshahrani

*Supervised by: Dr. Ali Yasser Al-Qarni (University of Bisha)*

---

## License

This project is for academic and non-commercial use. Please refer to the LICENSE file for more information.

---
