import logging


class NewStyleLogMessage(object):
    def __init__(self, message, *args, **kwargs):
        self.message = message
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        args = (i() if callable(i) else i for i in self.args)
        kwargs = dict((k, v() if callable(v) else v) for k, v in self.kwargs.items())

        return self.message.format(*args, **kwargs)


N = NewStyleLogMessage


class StyleAdapter(logging.LoggerAdapter):
    def __init__(self, logger, extra=None):
        super(StyleAdapter, self).__init__(logger, extra or {})

    def log(self, level, msg, *args, **kwargs):
        if self.isEnabledFor(level):
            msg, log_kwargs = self.process(msg, kwargs)
            self.logger._log(level, N(msg, *args, **kwargs), (), **log_kwargs)


logger = StyleAdapter(logging.getLogger("project"))