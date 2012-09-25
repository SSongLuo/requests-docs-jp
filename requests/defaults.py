# -*- coding: utf-8 -*-

"""
requests.defaults
~~~~~~~~~~~~~~~~~

.. This module provides the Requests configuration defaults.

このモジュールはRequestsのデフォルトの設定を提供します。

.. Configurations:

設定の一覧:

.. :base_headers: Default HTTP headers.
.. :verbose: Stream to write request logging to.
.. :max_redirects: Maximum number of redirects allowed within a request.s
.. :keep_alive: Reuse HTTP Connections?
.. :max_retries: The number of times a request should be retried in the event of a connection failure.
.. :danger_mode: If true, Requests will raise errors immediately.
.. :safe_mode: If true, Requests will catch all errors.
.. :strict_mode: If true, Requests will do its best to follow RFCs (e.g. POST redirects).
.. :pool_maxsize: The maximium size of an HTTP connection pool.
.. :pool_connections: The number of active HTTP connection pools to use.
.. :encode_uri: If true, URIs will automatically be percent-encoded.
.. :trust_env: If true, the surrouding environment will be trusted (environ, netrc).
.. :store_cookies: If false, the received cookies as part of the HTTP response would be ignored.

:base_headers: デフォルトのHTTPヘッダー。
:verbose: リクエストのログを書き込むストリーム。
:max_redirects: request.sにおいて、リダイレクトしてもいい回数の最大値。
:keep_alive: HTTPコネクションを維持するかどうか。
:max_retries: リクエストがコネクションに失敗した時にリトライする回数の最大値。
:danger_mode: trueにすると、Requestsはすぐにエラーを発生させます。
:safe_mode: trueにすると、全てのエラーをキャッチします。
:strict_mode: trueにすると、RequestsはRFCsに準拠するように試みます(例えば、POSTのリダイレクト)。
:pool_maxsize: HTTPコネクションプールのサイズの最大値。
:pool_connections: 使用するアクティブなHTTPコネクションプールの数。
:encode_uri: trueにすると、URIは自動的にパーセントエンコードされます。
:trust_env: trueにすると、環境全体(environ, netrc)を信頼出来るものとします。
:store_cookies: falseにすると、HTTPレスポンスの一部として受け取ったクッキーが無視されます。
"""

SCHEMAS = ['http', 'https']

from .utils import default_user_agent

defaults = dict()

defaults['base_headers'] = {
    'User-Agent': default_user_agent(),
    'Accept-Encoding': ', '.join(('gzip', 'deflate', 'compress')),
    'Accept': '*/*'
}

defaults['verbose'] = None
defaults['max_redirects'] = 30
defaults['pool_connections'] = 10
defaults['pool_maxsize'] = 10
defaults['max_retries'] = 0
defaults['danger_mode'] = False
defaults['safe_mode'] = False
defaults['strict_mode'] = False
defaults['keep_alive'] = True
defaults['encode_uri'] = True
defaults['trust_env'] = True
defaults['store_cookies'] = True