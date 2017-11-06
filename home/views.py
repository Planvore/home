from . import forms
from django.shortcuts import render
from . import models
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


class IndexView(TemplateView):
    template_name = 'home/index.html'


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

    return render(request, 'home/register.html', {'user_form': user_form,
                                                  'profile_form': profile_form,
                                                  'registered': registered
                                                  })


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('home:index'))

            else:
                return HttpResponse('Not logged in!')

        else:
            print("failed tried to login and failed")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse('invalid login details suplied')

    else:
        return render(request, 'home/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:index'))


@login_required
def profile(request):
    return render(request, 'home/profile.html', {})

# @login_required
# class UserProfileDetailView(DetailView):
#     model = UserProfileInfo

