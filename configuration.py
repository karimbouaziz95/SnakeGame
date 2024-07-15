import yaml

with open("SnakeGame/config.yaml") as stream:
    try:
        config = yaml.safe_load(stream)
    except Exception as e:
        raise ImportError("Could not open config file")

