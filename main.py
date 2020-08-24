from journey.Journey import Journey
from journey.View import View

if __name__ == "__main__":

    controller = Journey(View)
    controller.mainloop()