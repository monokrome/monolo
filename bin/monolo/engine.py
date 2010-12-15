from monolo.core import GameObject
import monolo.conf
import os, sys

class Engine(GameObject):
    argv = None

    def __init__(self, argv=None):
        """ Initializes the engine. """

        self.argv = argv

        self._engine_dir = os.path.dirname(os.path.abspath(argv[0]))
        self.game_name = getattr(monolo.conf, 'game_name', 'Demo')

        if getattr(monolo.conf, 'debug', False):
            print('Engine initialized.')

            print('Game directory is {0}'.format(self.game_dir))
            print('Engine directory is {0}'.format(self.engine_dir))

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
            new_name.lower(),
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
