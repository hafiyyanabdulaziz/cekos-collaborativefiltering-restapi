from django.urls import path
from collaborativefiltering.views import CollaborativeFiltering, PostCF
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("<input>/", CollaborativeFiltering.as_view()),
    path("", csrf_exempt(PostCF.as_view())),
    # path(r"^post/", PostCF.as_view()),
]

# from django.urls import path

# from my_app.views import MyFriend, MyFriendDetail

# urlpatterns = [
#    path('', MyFriend.as_view()),
#    path('<int:pk>/', MyFriendDetail.as_view()),
# ]
