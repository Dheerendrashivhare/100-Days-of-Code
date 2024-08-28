from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import List, Optional
import re


class Signup(BaseModel):
  eml: EmailStr
  mobile: mobile_validator
  Username: str
  Password: str
  Age: int
  Gender: str
  Address: str


class Login(BaseModel):
  Email: Optional[str]
  Mobile: Optional[str]
  Password: str


class varify_regex:
  def verify_mobile(self, mobile):
    regex = r'^[6-9]\d{9}$'
    if re.fullmatch(regex, mobile):
      return True
    else:
      return False

