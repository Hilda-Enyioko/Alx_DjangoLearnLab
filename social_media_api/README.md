# Social Media API — Authentication Module (Progress Summary)

This section documents the work completed across the last four tasks of the authentication module for the **Social Media API** project. The goal was to set up a functional user authentication system using Django REST Framework and Token Authentication.

---

## 🔹 **Task 1: Implement User Registration Serializer**

### **Goal**
Create a serializer that handles user sign-up, validates passwords, and safely creates new user accounts.

### **What Was Achieved**
- Built `UserRegistrationSerializer` using `ModelSerializer`.
- Added password strength validation using Django’s built-in validators.
- Added password confirmation (`password2`).
- Implemented a secure `create()` method that uses `create_user()`.

### **How It Was Done**
- Imported `get_user_model()` and `validate_password`.
- Declared fields for username, email, password, and password confirmation.
- Wrote a custom `validate()` method to ensure both passwords match.
- Used Django’s user manager to securely create new users.

---

## 🔹 **Task 2: Implement User Login Serializer**

### **Goal**
Prepare a serializer that accepts login credentials in a clean and simple structure.

### **What Was Achieved**
- Created `UserLoginSerializer` to accept only `username` and `password`.
- Ensured that login input is correctly validated for required fields.

### **How It Was Done**
- Defined the serializer as a simple `Serializer` (not a ModelSerializer).
- Added required CharFields for username and password.
- Allowed the view to handle authentication logic.

---

## 🔹 **Task 3: Create Registration and Login Views**

### **Goal**
Build API endpoints for registering new users and logging into existing accounts.

### **What Was Achieved**
- Built `RegisterView` using DRF’s `CreateAPIView`.
- Built `LoginView` using `APIView` for flexible control.
- Added token generation using DRF’s built-in `Token` model.
- Returned useful response data such as the token, user ID, and username.

### **How It Was Done**
- Implemented POST logic to validate login data.
- Used Django’s `authenticate()` to verify credentials.
- Generated or retrieved authentication tokens with `Token.objects.get_or_create()`.
- Handled incorrect login attempts with a 400 error response.

---

## 🔹 **Task 4: Testing and Initial Launch**

### **Goal**
Test the authentication system and ensure the project launches correctly.

### **What Was Achieved**
- Successfully started the Django development server.
- Confirmed that registration and login endpoints function correctly.
- Verified token generation and returned responses using Postman.

### **How It Was Done**
1. Ran the server using  
   ```bash
   python manage.py runserver
   ```

2. Used Postman to test:
    ```POST /api/register/```
    ```POST /api/login/```
3. Confirmed that:
    - Users are created successfully
    - Login works with correct credentials
    - Tokens are returned and can be reused for authenticated requests