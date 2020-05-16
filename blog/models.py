from django.db import models
from organiser.models import Startup,Tag
from django.urls import reverse

''' --------------------------- Post ---------------------------'''
 
class Post(models.Model):
    title = models.CharField(max_length = 63)
    slug = models.SlugField(max_length = 63,
                            help_text = "A label for URL",
                            unique_for_month = 'pub_date')
    text = models.TextField()
    pub_date = models.DateField('date published', auto_now_add = True) # auto_now_add-  set the date when the object is first created.                    
    tags = models.ManyToManyField(Tag, related_name = "blog_post")
    startups = models.ManyToManyField(Startup)

    def __str__(self):
        return "{} on {}".format(self.title, self.pub_date.strftime('%Y-%m-%d'))
    
    def get_absolute_url(self):
        return reverse("blog_post_detail", kwargs={"year": self.pub_date.year,
                                                    "month": self.pub_date.month,
                                                    "slug": self.slug}) 
        '''return the value to the url name's view. specific url can call a reverse functions with correct keyword parameters'''

    def get_update_url(self):
        return reverse("blog_post_update",kwargs={"year": self.pub_date.year,
                                                    "month": self.pub_date.month,
                                                    "slug": self.slug} )



    class Meta():
        verbose_name = 'blog post'
        ordering = ['pub_date','title']
        get_latest_by = 'pub_date'