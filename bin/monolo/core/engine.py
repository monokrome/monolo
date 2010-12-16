from monolo.core import GameObject
import monolo.conf
import os, sys

class Engine(GameObject):
    argv = None

    def __init__(self, argv=None):
        """ Initializes the engine. """

        self.argv = argv

        # Describes the to our engine directory to be formatted into a string
        path_info = [os.path.dirname(argv[0]), os.sep, '..']

        self._engine_dir = os.path.abspath('{0}{1}{2}'.format(*path_info))
        self.game_name = getattr(monolo.conf, 'game_name', 'Demo')

        # In debug mode, let people know where we've initialized everything.
        if getattr(monolo.conf, 'debug', False):
            print('Engine initialized.')

            print('Engine directory is {0}'.format(self.engine_dir))
            print('Game directory is {0}'.format(self.game_dir))

    @property
    def game_name(self):
        """ Property refering to the name of the current game being played. """

        return self._game_name

    @game_name.setter
    def game_name(self, new_name):
        """ Change the game name, and update our cached game directory. """

        self._game_name = new_name

        format_args = (
            self.engine_dir,
            os.sep,
            '../{0}'.format(new_name.lower()),
        )

        self._game_dir = os.path.abspath('{0}{1}{2}'.format(*format_args))

    @property
    def game_dir(self):
        """ Get the directory that the current game exists within. """

        return self._game_dir

    @property
    def engine_dir(self):
        """ Get the directory in which our engine is running from. """

        return self._engine_dir

