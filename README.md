# Tornado Boilerplate Application

- Async HTTP Client: http://localhost:8888/async_fetch?url=http://www.cnn.com

# Set up
- alembic init alembic

CREATE DATABASE tornado_app;
# one of following sets the password
CREATE USER 'tornado_user'@'localhost' IDENTIFIED BY 'qwerty123!';
set password for tornado_user@localhost = password('qwerty123!');
GRANT ALL PRIVILEGES ON tornado_app.* TO 'tornado_user'@'localhost';
