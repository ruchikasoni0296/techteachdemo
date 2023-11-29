from django.db import models
import random

r1 = random.randint(1000, 4999)
r2 = random.randint(100, 500)
r3 = random.randint(5000, 9999)
r4 = random.randint(50, 100)
r5 = random.randint(10000, 99999)


class Student(models.Model):
    student_id = "STD" + str(r1)
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        db_table = 'student'


class Courses(models.Model):
    course_id = "CR" + str(r2)
    course_name = models.CharField(max_length=45)
    course_desc = models.CharField(max_length=45)

    class Meta:
        db_table = 'courses'


class Packages(models.Model):
    package_id = "PKG" + str(r4)
    package_name = models.CharField(max_length=45)

    class Meta:
        db_table = 'packages'


class Registration(models.Model):
    registration_id = "RG" + str(r3)
    student_id = "STD" + str(r1)
    package_id = "PKG" + str(r4)
    course_id = "CR" + str(r2)
    enrollment_date = models.CharField(max_length=45)
    payment_id = "PAY" + str(r5)

    class Meta:
        db_table = 'registration'


class Payment(models.Model):
    payment_id = "PAY" + str(r5)
    payment_mode = models.CharField(max_length=45)
    payment_date = models.CharField(max_length=45)
    amount = models.CharField(max_length=45)
    payment_status = models.CharField(max_length=45)

    class Meta:
        db_table = 'payment'


class Courses_Packages(models.Model):
    packages_package_id = "PKG" + str(r4)
    courses_course_id = "CR" + str(r2)

    class Meta:
        db_table = 'courses_has_packages'
