class Subject:
    def __init__(self, code, name, credits):
        self.code = code
        self.name = name
        self.credits = credits

    def __str__(self):
        return f"{self.code} | {self.name} ({self.credits} credits)"