from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("addlist", views.AddList, name="addlist"),
    path("list", views.List, name="list"),
    path("listDetails/<int:list_id>", views.ListDetails, name="listDetails"),
    path("addwatchlist", views.addwatchlist, name="addwatchlist"),
    path("watchlist/<int:watchlist_id>", views.watchlist, name="watchlist"),
    path("currentwatchlist", views.current_watchlist, name="currentwatchlist"),
    path("Check_Bid", views.Check_Bid, name="Check_Bid"),
    path("removewatchlist/<int:watchlist_id>",
         views.removewatch, name="removewatch"),
    path("notification", views.notification, name="notification"),
    path("comment", views.comments, name="comment"),
    path("category", views.Category, name="Category"),
    path("notifications/<str:user_notify>",
         views.notifications, name="notifications"),
    path("removelisting/<int:List_Id>", views.removelisting, name="removelisting")
    #path("arr", views.arrs, name="arr"),
    #path("arrwatch/<int:watchlist_id>", views.arrwatch, name="arrwatch")
]
