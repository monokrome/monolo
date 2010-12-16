class Observer(object):
    mapping = {}

    def bind(self, key, method, *args, **kwargs):
        """ Bind the provided event key to the provided event method with the
            default arguments given by this call.

        """

        # Create our list for this key if it doesn't yet exist
        if not key in self.mapping:
            self.mapping[key] = []

        self.mapping[key].append({
            'callback': method,
            'args': args,
            'kwargs': kwargs,
        })

    def unbind(self, key, method=None):
        """ Remove all bound events with the given key and method. """

        if key in self.mapping:
            for event_data in self.mapping[key]:
                if method is None or event_data['callback'] is method:
                    self.mapping[key].remove(event_data)

            return True

        return False

    def trigger(self, key, *args, **kwargs):
        """ Trigger an event with the given name, and passes the given
            arguments merged with the defaults provided through bind.

        """

        if key in self.mapping:
            for event_data in self.mapping[key]:
                if 'args' in event_data:
                    orig_args = list(event_data['args'])
                    orig_args.extend(args)

                    args = orig_args

                if 'kwargs' in event_data:
                    orig_kwargs = event_data['kwargs']
                    orig_kwargs.update(kwargs)

                    kwargs = orig_kwargs

                event_data['callback'](*args, **kwargs)

