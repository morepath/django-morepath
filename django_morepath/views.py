from django.http import HttpResponse
from morepath import Request as MorepathRequest

from http.cookies import SimpleCookie


def make_morepath_view(app):
    def view(request, path):
        morepath_request = MorepathRequest(request.environ, app)
        # consume everything already seen by django
        for i in range(resolved_segment_count(request.path, path)):
            morepath_request.unconsumed.pop()
        morepath_request.make_body_seekable()
        response = app.publish(morepath_request)
        cookies = SimpleCookie()
        django_response = HttpResponse(
            response.body, status=response.status_code
        )
        for (header, value) in response.headerlist:
            if header.upper() == "SET-COOKIE":
                cookies.load(value)
            else:
                django_response[header] = value

        for cookie_name, cookie in cookies.items():
            cookie_attributes = {
                "key": cookie_name,
                "value": cookie.value,
                "expires": cookie["expires"],
                "path": cookie["path"],
                "domain": cookie["domain"],
            }
            if cookie["max-age"]:
                # Starting in Django 1.3 it performs arithmetic operations
                # with 'Max-Age'
                cookie_attributes["max_age"] = int(cookie["max-age"])

            django_response.set_cookie(**cookie_attributes)
        return django_response

    return view


def resolved_segment_count(request_path, unconsumed_path):
    resolved_path = request_path[0 : len(request_path) - len(unconsumed_path)]
    if resolved_path.startswith("/"):
        resolved_path = resolved_path[1:]
    if resolved_path.endswith("/"):
        resolved_path = resolved_path[:-1]
    if resolved_path == "":
        return 0
    return len(resolved_path.split("/"))
