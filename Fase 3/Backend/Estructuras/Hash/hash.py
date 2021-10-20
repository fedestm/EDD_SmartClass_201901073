class Hash:
    def __init__(self):
        self.claves = []
        self.size = 7
        self.claves_usadas = 0
        for i in range(self.size):
            self.claves.append(None)