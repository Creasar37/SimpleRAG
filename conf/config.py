import yaml

with open("conf/config.yaml", "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)
