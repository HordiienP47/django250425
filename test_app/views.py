from django.http import HttpResponse, HttpRequest


def home_page(request: HttpRequest):
    return HttpResponse(
        "Hello, Elvish language!"
    )
def greetings(request: HttpRequest, user_name):
    return HttpResponse(
        f"Hello, {user_name}!"
    )
