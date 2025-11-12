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
    role = models.CharField(choices=rolePossibilities,max_length=50)
    age = models.IntegerField()
    subjectNumber = models.IntegerField()
    gender = models.CharField(choices=genderPossibilities,max_length=50)
    specificRole = models.CharField(choices=specificRolePossibilities,max_length=50)
    orientation = models.CharField(max_length=50)
    allosexual = models.BooleanField()
    species = models.CharField(max_length=50)
    documentLink = models.CharField(max_length=150)
    submitted = models.BooleanField()
    muse = models.IntegerField(choices=musePossibilities)
    def __str__(self):
        return self.fullname
