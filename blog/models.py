from django.db import models


# create a blog models
# title
# publication_date
# body
# image
'''
class Blog(models.Model):
    title = models.CharField(max_lengh=255)
    publication_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

'''
# add blog apps to the settings

# create migration

# migrate

# add to the admin
