from django.conf.urls import url
from collaborativefiltering.views import CollaborativeFiltering

urlpatterns = [
    url(r"^(?P<input>[\w]+)", CollaborativeFiltering.as_view()),
]
