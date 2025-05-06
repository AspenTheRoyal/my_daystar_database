from django.db import models
genderPossibilities = {
    "Female": "Female",
    "Male": "Male",
    "Non-binary": "Non-binary",
    "Other": "Other",
    "Feminine-aligned": "Feminine-aligned",
    "Masculine-aligned": "Masculine-aligned",
}
rolePossibilities = {
    "Staff": "Staff",
    "Subject": "Subject",
}
specificRolePossibilities = {
    "Docile": "Docile",
    "Lahde": "Lahde",
    "Cronus": "Cronus",
    "Halcyon": "Halcyon",
    "Nonviable": "Nonviable",
    "Scientist": "Scientist",
    "Medical Staff": "Medical Staff",
    "Intern": "Intern",
}
class Character(models.Model):
    fullname = models.CharField(max_length=255)
    role = models.CharField(choices=rolePossibilities,null=True)
    age = models.IntegerField(null=True)
    subjectNumber = models.IntegerField(null=True)
    gender = models.CharField(choices=genderPossibilities,null=True)
    specificRole = models.CharField(choices=specificRolePossibilities,null=True)
    orientation = models.CharField(null=True)
    allosexual = models.BooleanField(null=True)
    species = models.CharField(null=True)


# Create your models here.
