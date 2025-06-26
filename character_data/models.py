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
    role = models.CharField(choices=rolePossibilities)
    age = models.IntegerField()
    subjectNumber = models.IntegerField()
    gender = models.CharField(choices=genderPossibilities)
    specificRole = models.CharField(choices=specificRolePossibilities)
    orientation = models.CharField()
    allosexual = models.BooleanField(null=True)
    species = models.CharField()

    def __str__(self):
        return self.fullname


# Create your models here.
