
class AWS:
    context = "AWS"

    def __init__(self, key, user):
        self.key = key
        self.user = user

    @static_method
    def check_context():
        print(AWS.context)

    def load(self):
        self.loader()

    def loader(self):
        print("Loading")

    def writer(self):
        print("Save")

    def stack(self):
        print("Check stack")


