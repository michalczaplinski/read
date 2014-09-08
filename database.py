from main import models
from django.contrib.auth.models import User

czapla = User.objects.get(username='czapla')

bk1 = models.Bookmark
bk2 = models.Bookmark
bk3 = models.Bookmark
bk4 = models.Bookmark

bk1.title = 'michnik chuj'
bk2.title = 'django docs'
bk3.title = 'fejsbook'
bk4.title = 'blablablabla balbalbla balb balba '

bk1.url = 'http://www.gazeta.pl'
bk2.url = 'https://docs.djangoproject.com/en/dev/ref/request-response/'
bk3.url = 'http://www.facebook.com'
bk4.url = 'https://github.com/carhartl/jquery-cookie'


for bookmark in [bk1, bk2, bk3, bk4]:
    bookmark.owner = czapla
    bookmark.owner_id = 1
    bookmark.save()
