from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
#import bcrypt
import re
import datetime
#from dateutil.parser import parse as parse_date

EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate(self, postData):
        errors=[]
        date = datetime.datetime.strptime(postData["date_hired"], "%Y-%d-%m")
        if len(postData["date_hired"]) > 0:
            if date < datetime.datetime.now():
                errors.append("Please enter valid date")
        if len(date) > 0:
                errors.append("Please enter valid date")
        if not postData.get("date_hired"):
            errors.append("Please enter date")
        if len(postData["date_hired"]) < 0:
            errors.append("Please enter valid date")
        if len(postData["first_name"]) < 2:
            errors.append("Sorry, not long enough")
        if len(postData["last_name"]) < 2:
            errors.append("Nope, not long enough")
        if not EMAIL_REGEX.match(postData['email']):
            errors.append("Email is not a valid email!")
        if len(postData['password']) < 7:
            errors.append("Password is not long enough.")
        if (postData['password']) != (postData['confirm_password']):
            errors.append("Password match not confirmed.")
        if User.objects.filter(email = ['email']):
			errors.append("This email already exists in our database.")
        if len(postData["email"]) < 0:
            errors.append("Please sign in")
        
        return errors

    def UserExistsLogin(self, email, entered_pw):
        l_fields=[]
        try:
            user = User.objects.get(email=email)
            if user.pw_hash == bcrypt.hashpw(entered_pw.encode(), user.pw_hash.encode()):
                l_fields.append("success!")
                return user
        except:
            l_fields.append("Email does not match our records")
            l_fields.append("Incorrect password")
        return l_fields

class ItemManager(models.Manager):
    def validate(self, postData):
        errors=[]
        if not postData.get("product"):
            errors.append("Please enter product")
        return errors

    def join(self, id, item_id):
        if len(Trip.objects.filter(id=item_id).filter(join_id=id))>0:
            return {"You've already added this to your wishlist"}
        else:
            joiner= User.objects.get(id=id)
            action= self.get(id= item_id)
            action.join.add(joiner)
            return {}


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    date_hired = models.DateField(null = True, blank = True)
    objects = UserManager()

class Item(models.Model):
    product = models.CharField(max_length=200, null = True, blank = True)
    date_added = models.DateField(auto_now_add = True)
    added_by = models.CharField(max_length=200, null = True, blank = True)
    creator = models.ForeignKey(User, related_name="product_added")
    objects = ItemManager()
