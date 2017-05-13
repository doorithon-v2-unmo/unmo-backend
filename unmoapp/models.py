class StdResponse(dict):
    def __init__(self, message, data=None):
        super().__init__()
        self.update({
            "result": message == "success",
            "message": message,
            "data": data
        })

    def result(self):
        return self.get("result", False)

    def message(self):
        return self.get("message", "unknown")

    def data(self):
        return self.get("data", None)
