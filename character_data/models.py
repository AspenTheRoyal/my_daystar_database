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
musePossibilities = {
    1: "Red",
    2: "Orange",
    3: "Yellow",
    4: "Green",
    5: "Blue",
}
class Character(models.Model):
    fullname = models.CharField(max_length=255)
    role = models.CharField(choices=rolePossibilities,max_length=255)
    age = models.IntegerField()
    subjectNumber = models.IntegerField()
    gender = models.CharField(choices=genderPossibilities,max_length=255)
    specificRole = models.CharField(choices=specificRolePossibilities,max_length=255)
    orientation = models.CharField(max_length=255)
    allosexual = models.BooleanField(null=True)
    species = models.CharField(max_length=255)
    documentLink = models.CharField(max_length=255,null=True)
    submitted = models.BooleanField(null=True)
    muse = models.IntegerField(choices=musePossibilities,null=True)
    def __str__(self):
        return self.fullname


# Create your models here.
