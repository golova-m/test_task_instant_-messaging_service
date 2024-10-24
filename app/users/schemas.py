import re
from pydantic import BaseModel, Field, EmailStr, ConfigDict, validator


class SUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    phone_number: str = Field(..., description='Номер телефона в международном формате, начинающийся с "+"')
    name: str = Field(..., min_length=1, max_length=50, description="Имя пользователя, от 1 до 50 символов")
    email: EmailStr = Field(..., description="Электронная почта пользователя")


    @validator('phone_number')
    def validate_phone_number(cls, value):
        if not re.match(r'^\+\d{1,15}$', value):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать от 1 до 15 цифр')
        return value