from django.db import models


# inheritance
class Blog(models.Model):
    title = models.CharField(max_length=255)
    publication_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    # this is for admin page // show title instead of object
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]


    def pub_date_pretty(self):
        return self.publication_date.strftime('%A %b %d %Y  %r')

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
