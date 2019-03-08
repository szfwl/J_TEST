
import yaml,os

def ret_yaml(file_name):
    file_path = os.getcwd() + os.sep + file_name + ".yml"
    with open(file_path,"r") as f:
        return yaml.load(f)