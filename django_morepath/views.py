from django.http import HttpResponse
from morepath import Request as MorepathRequest

from http.cookies import SimpleCookie


def make_morepath_view(app):
    def view(request, path):
        # request._stream.stream.seek(0)

        morepath_request = MorepathRequest(request.environ, app)
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

