from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse

# Create your views here.

# * these are the function based controllers!!!


# def index(request):
#     print("----- Start -----")
#     print("type of request: ", request.method)
#     print("tell the full page path: ", request.path)
#     print("tell what protocol the req is comming :", request.scheme)
#     print("raw data: ", request.body)
#     print("encoding: ", request.encoding)
#     print(request.content_type)
#     # print(request.META)
#     # print(request.headers)
#     print(request.session)
#     print(request.get_host())
#     print(request.build_absolute_uri())


#     return HttpResponse("Hello this is my first response, from Django!!!")
#     # return HttpResponseNotFound("Not founded")


"""
Learnong about the djanjo request and resposne
"""


def index(request):
    print("----- Start -----")
    # * Request object
    # print("schema: ", request.scheme)
    # print("body data: ", request.body)
    # # this doesn't includes any scheme, domain and query string
    # print("full url path: ", request.path)
    # print("request method: ", request.method)
    # print("content type of req: ", request.content_type)
    # print("content params: ", request.content_params)
    # print("content params: ", request.GET)
    # print("req cookies: ", request.COOKIES)
    # print("req uploaded file: ", request.FILES)
    # print("http header: ", request.META)
    # for key, val in request.META.items():
    #     print("{} : {}".format(key, val))
    # print("headers: ", request.headers)
    # * Response

    print("----- End -----")

    # res = HttpResponse()
    # res.write("<h2>this is the second tag</h2>")
    # res.write("<h3>this is the third tag tag</h3>")
    # return res

    # * we can set custom header in response object
    # res = HttpResponse()
    # res.headers["name"] = "unknown user!!!"
    # return res

    # res = HttpResponse()
    # res.status_code = 300
    # res.cookies["name"] = "unkown user!!"
    # return res

    # * json response
    data = {"name": "user", "age": 10, "is_active": False, "kill_list": [1, 2, 3, 4]}
    # with safe we can pass any data structure, default safe:True
    # return JsonResponse(["name", "age"], safe=False)
    return JsonResponse(data=data)

    # return HttpResponse("<h1>this is the main heading </h1>").status_code = 300
    # return render(request, "landing_page.html")


def get_heading(request):
    return HttpResponse("""
            <h1>this is the heading!! </h1>
        """)


def home_details(request):
    # print("home details view")
    # print(request.path)
    data = [
        {"name": "Toji", "age": 20, "gender": "Male", "degree": "CS"},
        {"name": "Naruto", "age": 10, "gender": "Male", "degree": "CS"},
        {"name": "Itachi", "age": 25, "gender": "Male", "degree": "Killer"},
        {"name": "Kouzwa", "age": 20, "gender": "Female", "degree": "MBBS"},
        {"name": "Nana", "age": 30, "gender": "Female", "degree": "BBA"},
    ]

    return render(request, "info.html", context={"data": data})
