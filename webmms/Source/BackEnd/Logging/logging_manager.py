#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""This module contains the logger manager class.

In order to use this module make an instance of it and the call vConfigureLogger()

Todo:

"""
import logging
from logging.handlers import RotatingFileHandler  # noqa    # pylint: disable=W0611


class clsLoggingManager:
    """ This is the logging manager class.

    Args:
    """
    def __init__(self):
        super(clsLoggingManager, self).__init__()
        self._objRootLogger = None
        # Set up the logging format we want to use
        self._acLoggingFormat = "%(asctime)s,%(msecs)03d,%(filename)s,%(lineno)d,%(funcName)s,%(levelname)s,%(message)s"
        self._acLoggingDateFormat = "%Y,%m,%d,%H,%M,%S"
        self._objLogFormatter = None
        self._objLoggingConsoleHandler = None
        self._objLoggingRotatingFileHandler = None

    def vConfigureLogger(self, acFilenamePar: str = 'logging.log', iMaxBytesPar: int = 536870912, iBackupCountPar: int = 1) -> None:
        """ This public method which configures the logger manager after the constructor

        Parameters:
            acFilenamePar (str): The first parameter. The name of the log file.
            iMaxBytesPar (int): The second parameter. The maximum allowed size of the log file.
            iBackupCountPar (int): The third parameter. The number of backup files allowed.

        Returns:

        Raises:
            Raises no exceptions

        """

        self._objRootLogger = logging.getLogger()  # Get the logger instance
        self._objRootLogger.setLevel(logging.DEBUG)

        self._objLogFormatter = logging.Formatter(self._acLoggingFormat, self._acLoggingDateFormat)

        # Also make use of a StreamHandler so that we can log to the console as well to make development easier
        self._objLoggingConsoleHandler = logging.StreamHandler()
        self._objLoggingConsoleHandler.setLevel(logging.DEBUG)
        self._objLoggingConsoleHandler.setFormatter(self._objLogFormatter)
        self._objRootLogger.addHandler(self._objLoggingConsoleHandler)

        # When we log to file it must be a rotating log file
        self._objLoggingRotatingFileHandler = logging.handlers.RotatingFileHandler(filename=acFilenamePar, mode='a', maxBytes=iMaxBytesPar, backupCount=iBackupCountPar)
        self._objLoggingRotatingFileHandler.setLevel(logging.DEBUG)
        self._objLoggingRotatingFileHandler.setFormatter(self._objLogFormatter)
        self._objRootLogger.addHandler(self._objLoggingRotatingFileHandler)

    def objGetLoggerInstance(self) -> None:
        """ This public method is used to get the instance of the logger.

        Parameters:

        Returns:
            (object): The getlogger() instance

        Raises:
            Raises no exceptions

        """
        return(self._objRootLogger)
