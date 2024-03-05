class Logger:
    FILENAME = "log.txt"

    @classmethod
    def log(cls, message: str):
        with open(cls.FILENAME, "w") as file:
            file.write(message + "\n")
