import json
from urllib import request


def convertJson(listIdProperti):
    print(listIdProperti)

    listDetail = []

    for idProperti in listIdProperti:
        # print(idProperti)
        url = "https://api.koseeker.id/property/" + idProperti
        response = request.urlopen(url)
        data = json.loads(response.read())
        if data["error"] == False:
            listDetail.append(data["data"])

    return listDetail
    # url = "https://api.koseeker.id/property/" + idProperti
    # response = request.urlopen(url)
    # data = json.loads(response.read())
    # return data["data"]
