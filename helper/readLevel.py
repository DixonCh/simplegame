class ReadLevel():

    def __init__(self, level):
        self.level = level
        self.x = 0
        self.y = 0
        self.data_list = []

    def get_level_data(self):
        linefile = open(self.level, "r")
        for line in linefile:
            self.x = 0
            for char in line:
                if char == "1":
                    self.data_list.append([self.x, self.y, True])
                else:
                    self.data_list.append([self.x, self.y, False])

                self.x += 32

            self.y += 32

        return self.data_list
