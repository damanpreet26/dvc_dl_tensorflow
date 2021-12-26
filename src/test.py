import logging
import os.path

log_str = "[%(asctime)s: %(level_name)s: %(module)s] : %(message)s"



logging.basicConfig(filename="logs/file.log" , format='%(asctime)s - %(message)s', level=logging.INFO)


if __name__=="__main__":
    logging.info('firsty')