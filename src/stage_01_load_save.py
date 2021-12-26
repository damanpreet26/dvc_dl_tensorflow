import os
from src.utils.all_utils import *
import pandas as pd
import argparse
import shutil
from tqdm import  tqdm
import logging

log_dir="logs"
create_dir([log_dir])
logging.basicConfig(filename=os.path.join(log_dir,"new_log.log") , format='%(asctime)s - %(message)s', level=logging.INFO)


def load_save_data(config_path):
    config=read_yaml(config_path)

    artifacts_dir =  config["artifacts"]["artifacts_dir"]
    cat_down_data_folder = config["source_download_path"]["cat"]
    dog_down_data_folder = config["source_download_path"]["dog"]

    cat_data_folder = config["source_folder"]["cat"]
    dog_data_folder = config["source_folder"]["dog"]

    cat_val=os.listdir(cat_down_data_folder)
    for cats in cat_val:
        src=os.path.join(cat_down_data_folder,cats)
        tgt=os.path.join(cat_data_folder,cats)
        shutil.copy(src,tgt)




if __name__=="__main__":
    arg=argparse.ArgumentParser()
    arg.add_argument("--config","-c",default="config/config.yaml")
    parsed_args=arg.parse_args()

    try:
        logging.info("starting Stage 01")
        load_save_data(parsed_args.config)
        logging.info("stage 1 completed and all data saved in local directorues")
    except Exception as e:
        logging.exception(e)
        raise e