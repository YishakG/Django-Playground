1. AbstractUser => Base Class provided by Django used to create a custom User model while keeping the built-in Auth System
2. Already Includes => username, first_name, last_name, email, password, is_staff, is_active, is_superuser, groups, user_permissions, authentication logic,
3. Use it when you want to add extra feild to the User and still use Django;s default authentication behaviour

4. Then in settings.py 
AUTH_USER_MODEL = 'yourapp.User'

5. Run Migrations 
