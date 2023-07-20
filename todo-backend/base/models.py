from django.db import models
from django.utils.text import slugify

# Create your models here.


class Todo(models.Model):
    todo = models.CharField(max_length=250, blank=False, null=False)
    completed = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.todo


    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.todo)

            has_slug = Todo.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.todo) + "-" + str(count)
                has_slug = Todo.objects.filter(slug=slug).exists()

            self.slug = slug

        super().save(*args, **kwargs)
