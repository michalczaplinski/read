from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from allauth.account.views import login
from main.models import Bookmark
from django.http import Http404
import json, datetime, tldextract


def redirect_if_logged_in(f):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('/bookmarks/', permanent=True)
        else:
            return f(request)
    return wrapper


@redirect_if_logged_in
def index(request):
    return render(request, 'main/index.html')


def bookmark_list(request):
    user = request.user
    try:
        bookmarks = Bookmark.objects.filter(owner=user)
    except Exception:
        # the user is not loged in or signed up
        return redirect('/')
    context = {'bookmarks': bookmarks}
    return render(request, 'main/bookmark_list.html', context)


@redirect_if_logged_in
def custom_login(request, **kwargs):
    return login(request)


def delete_bookmark(request, id=id):
    bookmark = Bookmark.objects.get(pk = id)
    bookmark.delete()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')


@csrf_exempt
def add_bookmark(request):

    if request.user.is_authenticated():
        user = request.user

        url = request.POST['url']
        title = request.POST['title']

        timestamp = request.POST['datetime']
        # timezone = request.POST['timezone']

        date = datetime.datetime.fromtimestamp(float(timestamp))

        date_created = date
        date_updated = date

        ext = tldextract.extract(url)
        domain = '.'.join(ext[:2])

        bookmark = Bookmark( url = url,
                             title = title,
                             owner = user,
                             date_created = date_created,
                             date_updated = date_updated,
                             domain = domain)
        bookmark.save()

    else:
        redirect('/accounts/login/', permanent=True)

    return HttpResponse(request)


