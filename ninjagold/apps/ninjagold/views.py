'''
    ninjagold views.py
    Leif Anderson 7/20/17
'''
from django.shortcuts import render, redirect
import random
import datetime


# helpers
# a cleaner random
def rand_range(a, b):
    num = random.randrange(a, b)
    return num

# add to our activity list
def add_activity(activity, earned, ninja_data):
    time_stamp = datetime.datetime.now()
    activity_string = 'Earned ' + str(earned) + ' gold from the ' + activity + '!' + ' (' + str(time_stamp) + ')'
    ninja_data['activities'].append(activity_string)

# bad habits die hard
def add_caisino_trip(activity, won_lost, ninja_data):
    time_stamp = datetime.datetime.now()
    if (won_lost >= 0):
        activity_string = 'Entered a caisino and won ' + str(won_lost) + ' gold ... Nice!' + ' (' + str(time_stamp) + ')'
    else:
        activity_string = 'Entered a caisino and lost ' + str(won_lost) + ' gold ... Ouch!' + ' (' + str(time_stamp) + ')'
    ninja_data['activities'].append(activity_string)


# landing page
def index(request):
    # setup session - Django stores session on server!
    if 'ninja_gold' not in request.session:
        request.session['ninja_gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []

    ninja_data = {
        'ninja_gold' : request.session['ninja_gold'],
        'activities' : request.session['activities']
    }
    return render(request, 'ninjagold/index.html', ninja_data)


# redirect
def success(request):
    return redirect('/')


# destroy session keys
def clear_session_keys(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')


# process the users activity
def process_money(request):

    earned = 0;
    ninja_data = request.session
    activity = request.POST.get('activity')

    if (activity == 'farm'):
        earned = rand_range(100, 201)
        add_activity(activity, earned, ninja_data)
    elif (activity == 'cave'):
        earned = rand_range(50, 101)
        add_activity(activity, earned, ninja_data)
    elif (activity == 'house'):
        earned = rand_range(20, 51)
        add_activity(activity, earned, ninja_data)
    elif (activity == 'caisino'):
        earned = rand_range(-500, 501)
        add_caisino_trip(activity, earned, ninja_data)
    else:
        pass

    ninja_data['ninja_gold'] += earned

    return redirect('/')
