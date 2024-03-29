#!/usr/bin/env python
#coding=utf-8

import web
import sys, os

from config.urls import urls

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

app = web.application(urls, globals())


if __name__ == "__main__":
    if 'SERVER_SOFTWARE' in os.environ:
        import sae
        sae.create_wsgi_app(app.wsgifunc())
    else:
        app.run()
