from main import SlowAPI


def global_middleware(request):
    print("this was executed before any route!")

slowapi = SlowAPI(middlewares=[global_middleware])


def local_middleware(request):
    request.queries["channel"] = "youtube"

@slowapi.get("/users/{id}", middlewares=[local_middleware])
def get_users(req, res, id):
    print(req.queries)
    res.send(id)

# @slowapi.post("/users")
# def post_users(req, res):
#     res.send("HEY THERE", "201")

@slowapi.route("/users")
class User:
    def __init__(self) -> None:
        # You can have this!
        pass
    
    def get(req, res):
        print(req.queries)
        res.send("HELLO I AM HERE")
    
    def post(req, res):
        res.render("example", {"name": "Rivaan", "message": "Hello there!"})

    def hello():
        # Will ignore this helper function!
        pass


    