# TODO: With the current implementation, references to objects in multiple game
#       objects can cause unpredictable results due to auto destruction of
#       children. Is this an issue / something that we want to support?

class GameObject(list):
    """ An object which defines a few game events, as well as derives the list
        object in order to contain a list of child objects, which implement the
        same interface. """

    per_frame = False
    """ If true, 'update' will be called on every frame. Think functions will
        still be called only when they have been asked to be called. """

    def __init__(self, children=[]):
        self.extend(children)

        self.create()

    def create(self):
        """ Initialization method. This is where we can safely reference other
            game objects without worrying about initialization issues. """

        for child in self:
            child.create()

    def update(self, frame_time):
        """ Called whenever this object requests to be updated. """

        for child in self:
            child.update(frame_time)

    def destroy(self):
        """ Generic shutdown method. """

        for child in self:
            child.destroy()

    def __del__(self):
        self.destroy()

