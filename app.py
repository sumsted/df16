""" Bottle app for backtrack """

import bottle_sqlalchemy as sqlalchemy
from bottle import TEMPLATE_PATH, install, run

from db_setup import DbSetup
from services.sf_helper import SfHelper
from settings import Settings

settings = Settings()
sf_helper = SfHelper()
TEMPLATE_PATH.insert(0, settings.DF16['TEMPLATE_FOLDER'])

# database
db_setup = DbSetup()
Base = db_setup.base
engine = db_setup.engine
plugin = sqlalchemy.Plugin(engine,
                           Base.metadata,
                           keyword='db',
                           commit=True,
                           create=False,
                           use_kwargs=False)
install(plugin)

# routes are here and use default_app, to be after app and db setup
import routes.web
import routes.alexa_api
import routes.carrier_api

if __name__ == '__main__':
    run(host=settings.DF16['HOST'], port=settings.DF16['PORT'], debug=True)
