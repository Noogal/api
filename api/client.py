# -*- coding: utf-8 -*-

import asyncio
import logging

from . import __version__ as library_version
from .http import HTTPClient
#from .errors import InvalidArgument

log = logging.getLogger(__name__)


class Client:
    """Represents a client connection that connects to noogalapp.
    This class is used to interact with the Noogal API.

    .. _event loop: https://docs.python.org/3/library/asyncio-eventloops.html
    .. _aiohttp session: https://aiohttp.readthedocs.io/en/stable/client_reference.html#client-session

    Parameters
    ==========
    token :
        An API Token
    app :
        An instance of a noogalapp.com Client object
    **loop : Optional[event loop].
        The `event loop`_ to use for asynchronous operations.
        Defaults to ``bot.loop``.
    **session : Optional
        The aiohttp session to use for requests to the API.
    """

    def __init__(self, app, token, **kwargs):
        self.app = app
        self.restaurantID = None
        self.loop = kwargs.get('loop') or app.loop
        self.http = HTTPClient(token, loop=self.loop, session=kwargs.get('session'))
        self._isClosed = False
        self.loop.create_task(self.__ainit__())

    async def __ainit__(self):
        await self.app.wait_until_ready()
        self.restaurantID = self.app.restaurant.id

    async def getMenu(self, restaurantID: int=None):
        """This function is a coroutine.

        Gets the menu of a restaurant from noogalapp.com

        Parameters
        ==========

        restaurantID: int[Optional]
            The restaurantID of the restaurant you want to lookup.
            Defaults to the Restaurant provided in Client init

        Returns
        =======

        menu: dict
            The menu of a restaurant.
            The date object is returned in a datetime.datetime object
        """
        if restaurantID is None:
            restaurantID = self.restaurantID
        return await self.http.getMenu(restaurantID)

        async def close(self):
        """This function is a coroutine.
        Closes all connections."""
        if self._isClosed:
            return
        else:
            await self.http.close()
            self._isClosed = True
