class Bird:
    def _fly(self):
        print("I can fly")
class Fish:
    def _swim(self):
        print("I can swim")
class FlyFish(Bird,Fish):
    pass
if __name__ == "__main__":
    f = FlyFish()
    f._swim()
    f._fly()