from django.shortcuts import render, redirect
from model import Dependency
from model import Dependencies
from model import Agency
from model import Agencies
from model import Tour
from model import Tours


def lab1db(request):
    smth = "Welcome to catalog"
    dependencies = Dependencies()
    dependenciesarr= dependencies.show()
    tours = Tours()
    toursarr= tours.show()
    agencies = Agencies()
    agenciesarr= agencies.show()
    return render(request,'./templates/lab1db/lab1db.html',locals())

def createagency(request):
    if request.method == "POST":
        text = request.POST['agency_name']
        agency = Agency(0, text)
        if (agency.add()):
            smth = "Successfully created agency : [ " + text + " ] "
        else:
            smth = "Sorry,Agency already exist : [ " + text + " ] "

    dependencies = Dependencies()
    dependenciesarr= dependencies.show()
    tours = Tours()
    toursarr= tours.show()
    agencies = Agencies()
    agenciesarr= agencies.show()
    return render(request,'./templates/lab1db/lab1db.html',locals())


def createdependency(request):
    if request.method == "POST":
        aname = request.POST['agency_name']
        tname = request.POST['tour_name']
        agency = Agency(0, aname)
        tour = Tour(0, tname)
        if (agency.check()>0):
            if (tour.check()>0):
                connect = Dependency(aname,tname)
                if(connect.add() == False):
                    smth="Sorry, dependency between [ " + aname + " ] and [ " + tname + " ] already exists"
                else:
                    smth = "Successfully created dependency between [ " + aname + " ] and [ " + tname + " ] "

            else:
                smth = "Sorry, I can't find this tour : [ " + tname + " ] to create dependency with [ " + aname + " ] "
        else:
            smth = "Sorry, I can't find this agency : : [ " + aname + " ] to create dependency with [ " + tname + " ] "

    dependencies = Dependencies()
    dependenciesarr= dependencies.show()
    tours = Tours()
    toursarr= tours.show()
    agencies = Agencies()
    agenciesarr= agencies.show()
    return render(request,'./templates/lab1db/lab1db.html',locals())

def createtour(request):
    if request.method == "POST":
        text = request.POST['tour_name']
        tour = Tour(2, text)
        if (tour.add()):
            smth = "Successfully created tour : [ " + text + " ] "
        else:
            smth = "Sorry,tour with name [ " + text + " ] already exists"

    dependencies = Dependencies()
    dependenciesarr= dependencies.show()
    tours = Tours()
    toursarr= tours.show()
    agencies = Agencies()
    agenciesarr= agencies.show()
    return render(request,'./templates/lab1db/lab1db.html',locals())

def deleteagency(request):
    if request.method == "POST":
        text = request.POST['agency_name']
        agency = Agency(0, text)
        dependency = Dependency(text,"sadhkjgfcbasdciamcois")
        if (agency.delete()):
            dependency.deleteall()
            smth = "Successfully deleted agency : [ " + text + " ] "
        else:
            smth = "Sorry,Agency with this name [ " + text + " ] doesn't exist "

    dependencies = Dependencies()
    dependenciesarr= dependencies.show()
    tours = Tours()
    toursarr= tours.show()
    agencies = Agencies()
    agenciesarr= agencies.show()
    return render(request,'./templates/lab1db/lab1db.html',locals())

def deletedependency(request):
    if request.method == "POST":
        aname = request.POST['agency_name']
        tname = request.POST['tour_name']
        agency = Agency(0, aname)
        tour = Tour(0, tname)
        connect = Dependency(aname,tname)
        if (connect.delete()):
            smth = "Successfully deleted dependency between [ " + aname + " ] and [ " + tname + " ] "
        else:
            smth = "Sorry, I can't find this dependency between [ " + aname + " ] and [ " + tname + " ] "
    dependencies = Dependencies()
    dependenciesarr= dependencies.show()
    tours = Tours()
    toursarr= tours.show()
    agencies = Agencies()
    agenciesarr= agencies.show()
    return render(request,'./templates/lab1db/lab1db.html',locals())


def deletetour(request):
    if request.method == "POST":
        text = request.POST['tour_name']
        tour = Tour(2, text)
        dependency = Dependency("sadhkjgfcbasdciamcois", text)
        if (tour.delete()):
            dependency.deleteall()
            smth = "Successfully deleted tour : [ " + text + " ] "
        else:
            smth = "Sorry, I can't find this tour to [ " + text + " ] "

    dependencies = Dependencies()
    dependenciesarr= dependencies.show()
    tours = Tours()
    toursarr= tours.show()
    agencies = Agencies()
    agenciesarr= agencies.show()
    return render(request,'./templates/lab1db/lab1db.html',locals())

def findtour(request):
    if request.method == "POST":
        tname = request.POST['tour_name']
        connect = Dependency("", tname)
        agencies = connect.findtour()
        smth="You can buy tour to [ " + tname + " ] here: "
        if (not agencies):
            smth = "Sorry, I can't find agency that sales tours to [ " + tname + " ] "
        else:
            for agency in agencies:
                smth+= " [ " + agency  + " ] "

    dependencies = Dependencies()
    dependenciesarr= dependencies.show()
    tours = Tours()
    toursarr= tours.show()
    agencies = Agencies()
    agenciesarr= agencies.show()
    return render(request,'./templates/lab1db/lab1db.html',locals())


def findagency(request):
    if request.method == "POST":
        aname = request.POST['agency_name']
        connect = Dependency(aname,"")
        tours = connect.findagency()
        smth="Tours that are sold by [ " + aname + " ] here: "
        if (not tours):
            smth = "Sorry, I can't find tours by [ " + aname + " ] "
        else:
            for tour in tours:
                smth+= " [ " + tour  + " ] "

    dependencies = Dependencies()
    dependenciesarr= dependencies.show()
    tours = Tours()
    toursarr= tours.show()
    agencies = Agencies()
    agenciesarr= agencies.show()
    return render(request,'./templates/lab1db/lab1db.html',locals())