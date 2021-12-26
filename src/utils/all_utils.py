import os
import yaml


def read_yaml(path_to_file:str)-> dict:
    with open(path_to_file,"r") as yfile:
        content=yaml.safe_load(yfile)
    return content

def create_dir(dir_list: list, ):
    for dir in dir_list:
        os.makedirs(dir)
    print(f"directory created {dir_list}")

def save_local_files(data, data_path, index_status=False):
    data.to_csv(data_path, index=index_status)
    print(f"File saved at {data_path}")

def save_report(report, report_path):
    with open(report_path, "w") as f:
        f.write(report)
    print(f"report saved at {report_path}")
