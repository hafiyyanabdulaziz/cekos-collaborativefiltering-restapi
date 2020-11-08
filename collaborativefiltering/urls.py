from django.conf.urls import url
from collaborativefiltering.views import CollaborativeFiltering, PostCF

urlpatterns = [
    url(r"^(?P<input>[\w]+)", CollaborativeFiltering.as_view()),
    url(r"^post/", PostCF.as_view()),
]
