import logging

logger = logging

logger.basicConfig(filename='User_Registration.log',level=logging.INFO, format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s',filemode='w')

logger.basicConfig(filename='User_Registration.log',level=logging.ERROR, format='%(asctime)s:%(funcName)s:%(levelname)s:%(lineo)d',filemode='w')
