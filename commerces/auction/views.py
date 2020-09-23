from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import sessions

from .models import User, listing, bids, watch, comment, notification

#count_Bid = 0


def index(request):
    lists = listing.objects.all()
    return render(request, "auction/index.html", {"lists": lists})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auction/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auction/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


arr = []


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auction/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auction/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auction/register.html")


def List(request):
    if request.method == "GET":
        lists = listing.objects.all()
        return render(request, "auction/list.html", {
            "lists": lists
        })
    else:
        Title = request.POST["Title"]
        Description = request.POST["Description"]
        Category = request.POST["Category"]
        ImageUrl = request.POST["ImageUrl"]
        Bid = request.POST["Bid"]
        List_Creator = request.POST["List_Creator"]
        list_save = listing(Title=Title, Description=Description,
                            Category=Category, Bid=Bid, ImageUrl=ImageUrl, List_Creator=List_Creator)
        list_save.save()
        lists = listing.objects.all()
        return render(request, "auction/index.html", {
            "lists": lists
            # "hour": listing.Time.time().hour,
            # "minute": lists.Time.minute,
            # "year": lists.date().year,
            # "month": lists.Time.date().month,
            # "day": lists.Time.date().day
        })


def AddList(request):
    return render(request, "auction/addform.html")


def ListDetails(request, list_id):
    lists = listing.objects.get(id=list_id)
    All_List = lists.Bids.first()
    #Availble_List = listing.objects.all()
    return render(request, "auction/listingDetails.html", {
        "listDetails": lists,
        "Comment": lists.Comment_For_Listing.all(),
        "Bid": All_List,
        "Min_Bid": All_List,
        "No_Bid": 0})


def watchlist(request, watchlist_id):
    lists = listing.objects.get(id=watchlist_id)
    Title = lists.Title
    Description = lists.Description
    Image = lists.Image
    ImageUrl = lists.ImageUrl
    Category = lists.Category
    Bid = lists.Bid
    Time = lists.Time
    List_Creator = lists.List_Creator
    watchlist = watch(Title=Title, Description=Description, Image=Image, ImageUrl=ImageUrl,
                      Category=Category, Bid=Bid, Time=Time, List_Creator=List_Creator)
    watchlist.save()
    return render(request, "auction/watchlist.html", {
        "list": watch.objects.get(Title=Title),
        "message": "Watchlist Added Succesfully!"})


def addwatchlist(request):
    lists = listing.objects.all()
    return render(request, "auction/addwatchlist.html", {"lists": lists})


def current_watchlist(request):
    return render(request, "auction/currentwatchlist.html", {
        "lists": watch.objects.all()
    })


def Check_Bid(request):
    Bid_Intial = int(request.POST["Bid_Initial"])
    Bid = int(request.POST["Bid"])
    user = request.POST["user"]
    Initial_Bid = int(request.POST["Initial_Bid"])
    List_id = int(request.POST["Id"])
    username = User.objects.get(username=user)
    Bid_List = listing.objects.get(id=List_id)
    All_List = Bid_List.Bids.first()
    #Real_List = All_List
    print(type(All_List))
    print(All_List)
    if All_List is None and Bid > Initial_Bid:
        bid_save = bids(Start_Bid=Bid)
        bid_save.save()
        Bids = bids.objects.get(Start_Bid=Bid)
        Bids.Bidding.add(Bid_List)
        Bids.User_Bid.add(username)
        return render(request, "auction/success.html")
    elif All_List is not None and Initial_Bid > Bid:
        return render(request, "auction/Error.html")
    elif All_List is None and Bid < Initial_Bid:
        return render(request, "auction/Error.html")
    elif All_List is not None and Bid_Intial < Bid:
        Bid_List.Bids.first().delete()
        bid_save = bids(Start_Bid=Bid)
        bid_save.save()
        Bids = bids.objects.get(Start_Bid=Bid)
        Bids.Bidding.add(Bid_List)
        Bids.User_Bid.add(username)
        return render(request, "auction/success.html")
    elif All_List is not None and Bid_Intial > Bid:
        return render(request, "auction/Error.html")
    else:
        bid_save = bids(Start_Bid=Bid)
        bid_save.save()
        Bids = bids.objects.get(Start_Bid=Bid)
        Bids.Bidding.add(Bid_List)
        Bids.User_Bid.add(username)
        return render(request, "auction/success.html")


def removewatch(request, watchlist_id):
    watch_delete = watch.objects.get(id=watchlist_id)
    watch_delete.delete()
    return render(request, "auction/currentwatchlist.html", {"lists": watch.objects.all()})


def notifications(request, user_notify):
    User_To_Notify = User.objects.get(username=user)
    return render(request, "auction/notification.html", {
        "Notify": User_To_Notify.User_To_Be_Notifieds.all()})


def comments(request):
    Id = int(request.POST["Id"])
    List_Id = listing.objects.get(id=Id)
    Comment_For_User = request.POST["Comment"]
    username = request.POST["user"]
    Username = User.objects.get(username=username)
    comment_made = comment(Comment=Comment_For_User, Comment_By=username)
    comment_made.save()
    comment_gotten = comment.objects.get(Comment=Comment_For_User)
    comment_gotten.List_Comment.add(List_Id)
    comment_gotten.User_Comment.add(Username)
    return render(request, "auction/listingDetails.html")


def Category(request):
    lists = listing.objects.all()
    Electronics = listing.objects.filter(Category="Electronics").all()
    Toys = listing.objects.filter(Category="Toys").all()
    Fashion = listing.objects.filter(Category="Fashion").all()
    Home = listing.objects.filter(Category="Home").all()
    Books = listing.objects.filter(Category="Books").all()
    return render(request, "auction/category.html", {
        "All": lists,
        "Electronics": Electronics,
        "Toys": Toys,
        "Books": Books,
        "Home": Home,
        "Fashion": Fashion})


def removelisting(request, List_Id):
    List_Id = listing.objects.get(id=List_Id)
    User_To_Notify = List_Id.User_Bidings.all()
    Title = List_Id.Title
    Notify = f"Your Bid for {Title} has been approved by the user!"
    n = notification(Notifications=Notify)
    n.save()
    List_Id.User_To_Be_Notified.add(User_To_Notify)
    return render(request, "auction/index.html")
