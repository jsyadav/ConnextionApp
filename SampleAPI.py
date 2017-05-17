import logging
import connexion

logger = logging.getLogger('sample-app')
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    app = connexion.App(__name__,
                        specification_dir="./",
                        debug=True)

    # use strict_validation during developent
    app.add_api('api.yaml')


    # Expose global WSGI app; the WSGI app is callable using uWSGI:
    #   uwsgi --http :8088 -w app
    APPLICATION = app.app

    # run our standalone gevent server
    app.run(port=8080, server='gevent')
