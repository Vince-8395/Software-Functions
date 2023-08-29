from django.db import models

class Professor(models.model):
    name = models.username(max_length=100)
    email = models.useremail(maxelength=100)

    def __str__(self):
        return self.name

class Authors(models.model):
    name = models.username(max_length=100)
    email = models.useremail(maxelength=100)

    def __str__(self):
        return self.name
    
class ResearchTitles(models.model):
    title = models.ResearchTitle(max_length=100)
    contents = models.TextField()
    publish_date = models.publishingdate(blank=True, null=True)
    Authors = models.AuthorsName(Authors, related_name="posts")
    CoAuthors = models.CoAuthorsName(CoAuthors, related_name="posts")
    
    def __str__(self):
        return self.researchtitles