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

- **Frontend:** Responsive HTML/CSS/JS interfaces for users and admins.
- **Backend:** Python Flask app processes images, handles logic, and communicates with Firebase.
- **Face Recognition:** Uses `face_recognition` (built on dlib) for feature extraction and matching.
- **Cloud Services:** Firebase Firestore (user data & logs) and Firebase Storage (face images).

---

## Screenshots

> *Admin Login Interface
A secure login interface for administrators, allowing the system administrator to access the central control panel by entering only the secret password.*
> <img width="919" height="424" alt="image" src="https://github.com/user-attachments/assets/095193a7-ef4c-48c5-b7ba-852f0c1d804d" />

> *Admin-Add New User Interface
A dedicated interface for the administrator to add a new user to the system, where the user ID, name, email are entered, and the user's face image is uploaded for biometric verification.*
> <img width="919" height="490" alt="image" src="https://github.com/user-attachments/assets/badb44c2-312d-4edf-ac1f-cc5fcdea0fa1" />

> *Admin-Add New User Interface – Success & Firestore Integration
When all fields are completed correctly and a face image is uploaded, a green success message ("User was added successfully") appears, enhancing the administrator experience and confirming that all steps were completed correctly.
The interface automatically integrates with the Firebase Firestore database, creating a new document named UserID containing all user data:*
> <img width="919" height="483" alt="image" src="https://github.com/user-attachments/assets/f0d191ab-4bd2-4ddd-a1d7-a7ae2e145a94" />
> <img width="915" height="347" alt="image" src="https://github.com/user-attachments/assets/cc1f062e-a36a-4c59-8499-015a4a496043" />


> *Admin-Statistics Dashboard - After adding a new user
An interactive, colorful dashboard allows management to monitor the system's security status and the number of active users in real time. After adding a new user, the increase in the number of users is immediately visible, giving managers confidence that administrative processes are being reflected directly in the database and in performance indicators.A "Refresh Statistics" button is available to instantly access the latest data, highlighting security alerts or significant changes in statistics without the need to navigate between pages or manually refresh the page.*
> <img width="919" height="503" alt="image" src="https://github.com/user-attachments/assets/27163301-af6d-406b-8574-9ed5aafbfe14" />

> *User Portal – Secure Facial Login
A user-friendly interface allows secure login via facial recognition technology, without the need for a traditional password.
The interface includes two flexible options for entering a face image:
•	Directly open the camera to take a live photo (Open Camera)
•	Upload a photo from the device (Choose File)
After selecting or capturing the image, the user can send it for verification (Send for Verification) with the click of a button.*
> <img width="919" height="417" alt="image" src="https://github.com/user-attachments/assets/c9995687-38f3-4ede-82eb-ec0aa9ff3870" />

> *User Portal – Face Detection Failure
When a photo is submitted for verification and the system fails to detect a face (such as uploading a blurry photo or one that doesn't contain a face at all), a clear red error message appears. The message directs the user to the source of the problem and prompts them to try again more clearly, reducing frustration and improving the quality of the entered verification data.*
> <img width="919" height="439" alt="image" src="https://github.com/user-attachments/assets/9aa51752-72b8-405b-8995-39760b75cd76" />

> *User Portal – Network Error
When attempting to send a facial image for verification and experiencing a problem connecting to the server or the internet, a red warning message appears.
This message prevents the user from thinking there is a problem with their image or data, and explains that the cause is beyond their control and that they should try again when they connect to the server and the network is stable.*
> <img width="919" height="460" alt="image" src="https://github.com/user-attachments/assets/8ce1224d-9fd0-44c8-ba9a-bfb169333943" />

> *User Portal – Access Denied
After submitting a face image for verification, if it does not match the authorized user data, the user will see a clear red alert.
The message indicates that the system did not recognize the image as a face registered in the database or that it did not match sufficiently, prompting the user to try again.
This interface is essential to protect the system from unauthorized access.*
> <img width="919" height="628" alt="image" src="https://github.com/user-attachments/assets/5c0b9400-1990-41e5-91a2-b00c41f8bcef" />

> *User Portal – Login Successful
After the facial image is successfully matched with the user's data in the system, a green congratulatory message appears.
The user feels confident and reassured that they have been successfully identified and can now access protected services or data.
This interface is the culmination of all the verification steps and a smooth and secure login experience.*
> <img width="919" height="788" alt="image" src="https://github.com/user-attachments/assets/87601398-c208-4f35-9e43-aa6c42a6fb14" />

> *User Portal – Upload Lowlighted Image, Login Successful
The system demonstrates high flexibility, successfully verifying a user's identity even when uploading a photo in dim or dark lighting, as long as the facial features are clear and recognizable.
After submission, the usual success message ("Login successful. Welcome, User") appears, enhancing the user experience and demonstrating the robustness of the biometric algorithms in handling photos of varying quality and lighting.*
> <img width="919" height="669" alt="image" src="https://github.com/user-attachments/assets/9ea335a3-fce3-41c0-a12e-a6d6d9461fce" />

> *User Portal – Upload Highlighted Image, Login Successful
The system demonstrates high flexibility, successfully verifying a user's identity even when uploading a photo in bright or high-light conditions, as long as the facial features are clear and recognizable.
After submission, the usual success message ("Login successful. Welcome, User") appears, enhancing the user experience and demonstrating the robustness of the biometric algorithms in handling photos of varying quality and lighting.*
> <img width="919" height="715" alt="image" src="https://github.com/user-attachments/assets/7a9ea020-c6ca-4d46-92a5-8736a1e74ffb" />

> *User Portal – Multiple Faces Image, Login Successful
The system demonstrates its ability to process an image containing multiple faces. When a group photo is uploaded, the system analyzes all faces, and if one is recognized as an authorized user, it allows access and displays the usual success message ("Login successful. Welcome, User").
This case demonstrates the algorithm's ability to detect and match the correct face from among multiple faces, making the system practical even in real-world scenarios where images may contain more than one person.*
> <img width="919" height="719" alt="image" src="https://github.com/user-attachments/assets/98a4e8e7-7d7d-41b6-8a1f-ed14697b54d5" />

> *Admin - Audit Logs Interface
In this audit logs interface, it appears that five different images were uploaded unsuccessfully, and on the fifth attempt, the authorized user was permanently blocked. The lock appears in the "Audit Logs" interface, and the administrator can unlock it according to specific policies.*
> <img width="919" height="611" alt="image" src="https://github.com/user-attachments/assets/d7142f40-5824-4280-baaa-88b9f462a9cc" />

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
