from django.db import models


# inheritance
class Blog(models.Model):
    title = models.CharField(max_length=255)
    publication_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')


# ------------Road Map-----------------
# 1. create a blog models
# title
# publication_date
# body
# image
# 2. add blog apps to the settings
# 3. create migration
# 4. migrate
# 5. add to the admin
