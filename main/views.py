from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib.auth.views import login
from django.http import HttpResponse
from allauth.account.views import login
from main.models import Bookmark
from django.http import Http404
import json

def redirect_if_logged_in(f):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('/bookmarks/')
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
        raise Http404
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

