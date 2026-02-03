import logging, sys
def setup_logging(debug: bool = False):
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=level, format='%(message)s', handlers=[logging.StreamHandler(sys.stdout)])
