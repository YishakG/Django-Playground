Views:
1. Accept a request from the client
2. Performs some logic
3. Return a response

Two Types
1. Function based views
    def my_view(request):
    if request.method == "POST":
        ...
    elif request.method == "GET":
        ...
2. Class based views
   APIView handles request parsing content regotiation and response formattino
   define multiple get(), post(), put(), delete()