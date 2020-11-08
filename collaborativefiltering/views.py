from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

from collaborativefiltering.cf import *
from collaborativefiltering.convertjson import *


class CollaborativeFiltering(View):
    """
    def get(self, request, input):
        try:
            list = recommendations(input, 50, interactions_matrix)

        except:
            list = new_user()

        return JsonResponse(convertJson(list), safe=False)
    """

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

    # def post(self, request):
    # data = request.body.decode("utf8")
    # data = json.loads(data)
    # try:
    # new_friend = MyFriendList(
    #    friend_name=data["friend_name"], mobile_no=data["mobile_no"]
    # )
    # new_friend.save()
    # return JsonResponse({"created": "halo"}, safe=False)
    # except:
    # return JsonResponse({"error": "not a valid data"}, safe=False)


class PostCF(View):
    def post(self, request):
        data = request.body.decode("utf8")
        data = json.loads(data)
        # try:
        # new_friend = MyFriendList(
        #    friend_name=data["friend_name"], mobile_no=data["mobile_no"]
        # )
        # new_friend.save()
        # return JsonResponse({"created": "halo"}, safe=False)
        # except:
        return JsonResponse(data, safe=False)

    def get(self, request):

        return JsonResponse({"error": "not a valid datass"}, safe=False)
