from django.shortcuts import render
from django.http import HttpResponse
from .models import Classes,Notes
from django.template.defaulttags import register
import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from forms import UserForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from .forms import NoteForm
from django.shortcuts import redirect
from django.utils import timezone
import pytz
from datetime import datetime




@login_required(login_url="login/")
def index(request):
    allClasses = Classes.objects.order_by('-title')[:10]
    classwise_notes = {}
    for subject in allClasses:
        notes = Notes.objects.filter(classname = subject).values()
        note_list = []
        for each_note in notes:
            note_list.append(each_note.get('slug'))

        classwise_notes[str(subject)] = note_list
    
    

    saved = False

    if request.method == "POST":
        form = NoteForm(request.POST,request.FILES) 
        if form.is_valid():
            print "valid"
            note = form.save(commit=False)
            #post.author = request.user
            note.pub_date =  timezone.now()
            note.classname = Classes.objects.get(title=str(request.POST.get('classname')))
            note.save()
            return redirect('/')
        else:
            print "form is not valid"

    else:
        form = NoteForm()

    context = {'classes_list': classwise_notes,'form': form,'saved':saved}
    return render(request, 'notes/index.html',context)

def detail(request,notes_name_slug):
    latest_post_list = Classes.objects.order_by('-title')[:10]
    note = Notes.objects.get(slug=notes_name_slug)

    allClasses = Classes.objects.order_by('-title')[:10]
    classwise_notes = {}
    for subject in allClasses:
        notes = Notes.objects.filter(classname = subject).values()
        note_list = []
        for each_note in notes:
            note_list.append(each_note.get('slug'))


        classwise_notes[str(subject)] = note_list
    
    saved = False

    saved = False

    if request.method == "POST":
        form = NoteForm(request.POST,request.FILES) 
        if form.is_valid():
            print "valid"
            note = form.save(commit=False)
            #post.author = request.user
            note.pub_date =  timezone.now()
            note.classname = Classes.objects.get(title=str(request.POST.get('classname')))
            note.save()
            return redirect('/')
        else:
            print "form is not valid"

    else:
        form = NoteForm()



    context = {'latest_post_list':latest_post_list, 'note':note, 'classes_list':classwise_notes,'form': form,'saved':saved}
    return render(request, 'notes/blank-page.html',context)

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()


            # Update our variable to tell the template registration was successful.
            registered = True
            print "registered is true"

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render(request,'registration/form-1/index3.html', {'user_form': user_form,'registered': registered} )
def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your BoardScribe account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            invalidLogin = True
            print "Invalid login details: {0}, {1}".format(username, password)
            return render(request, 'registration/form-1/index3.html', {'invalidLogin':invalidLogin})

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'registration/form-1/index3.html', {'invalidLogin':invalidLogin})

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    print "logged out"
    request.session.flush()
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/login')


def new_note(request):

    form = NoteForm()
    return render(request, 'blog/post_edit.html', {'form': form})

    if request.method == "POST":
        title = request.POST.get('title')
        image = request.POST.get('password')
    else:
        print "hello"
