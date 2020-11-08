from django.urls import path
from collaborativefiltering.views import CollaborativeFiltering, PostCF
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("<input>/", CollaborativeFiltering.as_view()),
    path("", csrf_exempt(PostCF.as_view())),
]
