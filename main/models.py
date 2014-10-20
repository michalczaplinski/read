from django.contrib.auth.models import User
from django.db import models
from allauth.account.models import EmailAddress
# from allauth.socialaccount.models import SocialAccount
from django.utils.timezone import now
import hashlib


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')

    def __unicode__(self):
        return "{}'s profile".format(self.user.username)

    # class Meta:
    #     db_table = 'user_profile'

    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False

    # def profile_image_url(self):
    #     fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')

    #     if len(fb_uid):
    #         return "http://graph.facebook.com/{}/picture?width=40&height=40".format(fb_uid[0].uid)

    #     return "http://www.gravatar.com/avatar/{}?s=40".format(hashlib.md5(self.user.email).hexdigest())

    User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Bookmark(models.Model):
    url = models.URLField()
    title = models.CharField('title', max_length=255)
    description = models.TextField('description', blank=True)
    date_created = models.DateTimeField('date created')
    date_updated = models.DateTimeField('date updated')
    owner = models.ForeignKey(User, related_name='bookmarks')
    tags = models.ManyToManyField(Tag, blank=True)
    # like on reddit, eg. 'github.com'
    domain = models.CharField('domain', max_length=80, blank=True)

    class Meta:
        verbose_name = 'bookmark'
        verbose_name_plural = 'bookmarks'
        ordering = ['-date_created']

    def __unicode__(self):
        return '%s (%s)' % (self.title, self.url)


### CURRENTLY COMMENTED OUT BECAUSE WE WILL ORDINARILY
### GET DATE AND TIME IN THE AJAX REQUEST FROM THE USER.
    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.date_created = now()
    #     self.date_updated = now()
    #     super(Bookmark, self).save(*args, **kwargs)



