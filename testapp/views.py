from django.http import HttpResponse
import json


def root(request, path):
    return HttpResponse(
        json.dumps({"hello": "world"}), content_type="application/json"
    )
