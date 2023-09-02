from django.db import models


class Professors(models.Model):
      Professor_FirstName = models.Charfield(max_length=30) 
      Professor_LastName = models.Charfield(max_length=30)               
      Professor_EmailAddress = models.Charfield(max_length=30)

        def __str__(self):
            return self.Professors

class Titles(models.Model):
        authors = models.ForeignKey(Professors, on_delete = models.CASCADE)
        Coauthors = models.ForeignKey(Professors, Students, on_delete = models.CASCADE)
        name = models.CharField(max_length=100)
        released_date = models.DateField()

               def __str__(self):
                    return self.titles

         
            






        

