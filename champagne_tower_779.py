class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = dict()

        class Node:
            def __init__(self, row, glass, *, value=0):
                self.row = row
                self.glass = glass
                self.value = value
                tower[(row, glass)] = self
                try:
                    self.left = tower[(row + 1, glass)]
                except KeyError:
                    self.left = None
                try:
                    self.right = tower[(row + 1, glass + 1)]
                except KeyError:
                    self.right = None
                try:
                    tower[(row - 1, glass - 1)].right = self
                except KeyError:
                    pass
                try:
                    tower[(row - 1, glass)].left = self
                except KeyError:
                    pass

            @property
            def is_full(self):
                return 1 - self.value < 10 ** -10

            def create_children(self, *, adding=0):
                if self.left is None:
                    self.left = Node(self.row + 1, self.glass, value=adding)
                if self.right is None:
                    self.right = Node(self.row + 1, self.glass + 1, value=adding)

            def adding(self, adding_volume):
                if self.is_full:
                    self.left.adding(adding_volume / 2)
                    self.right.adding(adding_volume / 2)
                elif self.value + adding_volume >= 1:
                    extra = self.value + adding_volume - 1
                    self.value = 1
                    self.create_children()
                    self.left.adding(extra / 2)
                    self.right.adding(extra / 2)
                else:
                    self.value += adding_volume

        root = Node(0, 0)
        for i in range(poured):
            root.adding(1)
        temp = tower.get((query_row, query_glass))
        if temp is None:
            return 0
        return temp.value
