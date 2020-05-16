from django.db import models
from django.urls import reverse #to import reverse function 


''' --------------------------- Tag ---------------------------'''
class Tag (models.Model):    
    
    name = models.CharField(max_length = 31, unique = True)
    slug = models.SlugField(max_length = 31, unique = True, help_text = "A label for URL")
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("organiser_tag_detail", kwargs = {"slug": self.slug})
    
    
    class Meta():
        ordering = ['name']


''' --------------------------- Startup ---------------------------'''
    
class Startup (models.Model):
    name = models.CharField(max_length = 31, db_index = True)
    slug = models.SlugField(max_length = 31, unique= True,
                    help_text = "A label for URL")
    description =  models.TextField()    
    founded_date = models.DateField('date founded')
    contact = models.EmailField()
    website = models.URLField(max_length = 255)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("organiser_startup_detail", kwargs={"slug": self.slug})
    
   
    
    
    class Meta():
        ordering = ['name']
        get_latest_by = 'founded_date'

        ''' --------------------------- NewsLink --------------'''

class Newslink (models.Model):
    title = models.CharField(max_length=63)
    link = models.URLField()
    pub_date = models.DateField('date published')
    startup = models.ForeignKey(Startup, on_delete = models.CASCADE)   

    def get_absolute_url(self):
        return self.startup.get_absolute_url()
    
    
    def __str__(self):
        return "{}:{}" .format(self.startup , self.title)
    
    class Meta():
        verbose_name = 'news article'
        ordering = ["-pub_date"]
        get_latest_by = 'pub_date'
