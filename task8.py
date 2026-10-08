from pydantic import BaseModel, EmailStr, ValidationError

class UserMail(BaseModel):
    email: EmailStr

users_email = input("Введите ваш Email: ")
# Пример корректных данных
try:
    user = UserMail(email= users_email)
    print("Ваш Email корректен")
except ValidationError:
      print('Невалидные данные')
