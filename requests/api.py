# -*- coding: utf-8 -*-

"""
requests.api
~~~~~~~~~~~~

This module implements the Requests API.

:copyright: (c) 2012 by Kenneth Reitz.
:license: ISC, see LICENSE for more details.

"""

from . import sessions
from .safe_mode import catch_exceptions_if_in_safe_mode


@catch_exceptions_if_in_safe_mode
def request(method, url, **kwargs):
    """Constructs and sends a :class:`Request <Request>`.
    Returns :class:`Response <Response>` object.

    :param method: method for the new :class:`Request` object.
    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`.
    :param data: (optional) Dictionary or bytes to send in the body of the :class:`Request`.
    :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
    :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
    :param files: (optional) Dictionary of 'name': file-like-objects (or {'name': ('filename', fileobj)}) for multipart encoding upload.
    :param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
    :param timeout: (optional) Float describing the timeout of the request.
    :param allow_redirects: (optional) Boolean. Set to True if POST/PUT/DELETE redirect following is allowed.
    :param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
    :param return_response: (optional) If False, an un-sent Request object will returned.
    :param session: (optional) A :class:`Session` object to be used for the request.
    :param config: (optional) A configuration dictionary. See ``request.defaults`` for allowed keys and their default values.
    :param verify: (optional) if ``True``, the SSL cert will be verified. A CA_BUNDLE path can also be provided.
    :param prefetch: (optional) if ``True``, the response content will be immediately downloaded.
    :param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
    """

    # if this session was passed in, leave it open (and retain pooled connections);
    # if we're making it just for this call, then close it when we're done.
    adhoc_session = False
    session = kwargs.pop('session', None)
    if session is None:
        session = sessions.session()
        adhoc_session = True

    try:
        return session.request(method=method, url=url, **kwargs)
    finally:
        if adhoc_session:
            session.close()


def get(url, **kwargs):
    """
    .. Sends a GET request. Returns :class:`Response` object.

    GETリクエストを送信します。 :class:`Response` オブジェクトを返します。

    .. :param url: URL for the new :class:`Request` object.
    .. :param \*\*kwargs: Optional arguments that ``request`` takes.
    :param url: 新しい :class:`Request` オブジェクトのURL。
    :param \*\*kwargs: ``request`` が受け取る任意の引数。
    """

    kwargs.setdefault('allow_redirects', True)
    return request('get', url, **kwargs)


def options(url, **kwargs):
    """
    .. Sends a OPTIONS request. Returns :class:`Response` object.

    OPTIONSリクエストを送信します。 :class:`Response` オブジェクトを返します。

    .. :param url: URL for the new :class:`Request` object.
    .. :param \*\*kwargs: Optional arguments that ``request`` takes.
    :param url: 新しい :class:`Request` オブジェクトのURL。
    :param \*\*kwargs: ``request`` が受け取る任意の引数。
    """

    kwargs.setdefault('allow_redirects', True)
    return request('options', url, **kwargs)


def head(url, **kwargs):
    """
    .. Sends a HEAD request. Returns :class:`Response` object.

    HEADリクエストを送信します。 :class:`Response` オブジェクトを返します。

    .. :param url: URL for the new :class:`Request` object.
    .. :param \*\*kwargs: Optional arguments that ``request`` takes.
    :param url: 新しい :class:`Request` オブジェクトのURL。
    :param \*\*kwargs: ``request`` が受け取る任意の引数。
    """

    kwargs.setdefault('allow_redirects', False)
    return request('head', url, **kwargs)


def post(url, data=None, **kwargs):
    """
    .. Sends a POST request. Returns :class:`Response` object.

    POSTリクエストを送信します。 :class:`Response` オブジェクトを返します。

    .. :param url: URL for the new :class:`Request` object.
    .. :param data: (optional) Dictionary or bytes to send in the body of the :class:`Request`.
    .. :param \*\*kwargs: Optional arguments that ``request`` takes.
    :param url: 新しい :class:`Request` オブジェクトのURL
    :param data: (任意の)辞書、もしくは :class:`Request` の本文として送るためのデータ
    :param \*\*kwargs: ``request`` が受け取る任意の引数
    """

    return request('post', url, data=data, **kwargs)


def put(url, data=None, **kwargs):
    """
    .. Sends a PUT request. Returns :class:`Response` object.

    PUTリクエストを送信します。 :class:`Response` オブジェクトを返します。

    .. :param url: URL for the new :class:`Request` object.
    .. :param data: (optional) Dictionary or bytes to send in the body of the :class:`Request`.
    .. :param \*\*kwargs: Optional arguments that ``request`` takes.
    :param url: 新しい :class:`Request` オブジェクトのURL
    :param data: (任意の)辞書、もしくは :class:`Request` の本文として送るためのデータ
    :param \*\*kwargs: ``request`` が受け取る任意の引数
    """

    return request('put', url, data=data, **kwargs)


def patch(url, data=None, **kwargs):
    """
    .. Sends a PATCH request. Returns :class:`Response` object.

    PATCHリクエストを送信します。 :class:`Response` オブジェクトを返します。

    .. :param url: URL for the new :class:`Request` object.
    .. :param data: (optional) Dictionary or bytes to send in the body of the :class:`Request`.
    .. :param \*\*kwargs: Optional arguments that ``request`` takes.
    :param url: 新しい :class:`Request` オブジェクトのURL
    :param data: (任意の)辞書、もしくは :class:`Request` の本文として送るためのデータ
    :param \*\*kwargs: ``request`` が受け取る任意の引数
    """

    return request('patch', url,  data=data, **kwargs)


def delete(url, **kwargs):
    """
    .. Sends a DELETE request. Returns :class:`Response` object.

    DELETEリクエストを送信します。 :class:`Response` オブジェクトを返します。

    .. :param url: URL for the new :class:`Request` object.
    .. :param \*\*kwargs: Optional arguments that ``request`` takes.
    :param url: 新しい :class:`Request` オブジェクトのURL
    :param \*\*kwargs: ``request`` が受け取る任意の引数
    """

    return request('delete', url, **kwargs)