from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.contenttypes.fields import GenericRelation
from django.db.models.signals import pre_save
from django.db import models
from comments.models import Comment


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    comment = GenericRelation(Comment)
    slug = models.SlugField(unique=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def get_absolute_url(self):
        return reverse("posts:retrieve_post", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


def slug_generator(instance, **kwargs):
    if instance.slug:
        pass
    else:
        instance.slug = slugify(instance.title)
        while True:
            try:
                check = Post.objects.get(slug=instance.slug)
            except:
                break
            else:
                instance.slug = (
                    instance.slug + "-" + str(Post.objects.all().last().id + 1)
                )
    return instance.slug


pre_save.connect(slug_generator, sender=Post)
