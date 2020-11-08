from django.http import JsonResponse
from django.views import View
from collaborativefiltering.cf import *


class CollaborativeFiltering(View):
    def get(self, request, input):
        try:
            return JsonResponse(
                recommendations(input, 50, interactions_matrix),
                safe=False,
            )
        except:
            return JsonResponse(
                new_user(),
                safe=False,
            )

    def post(self, request):
        data = request.body.decode("utf8")
        data = json.loads(data)
        try:
            new_friend = MyFriendList(
                friend_name=data["friend_name"], mobile_no=data["mobile_no"]
            )
            new_friend.save()
            return JsonResponse({"created": data}, safe=False)
        except:
            return JsonResponse({"error": "not a valid data"}, safe=False)
