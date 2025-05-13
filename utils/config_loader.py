import os

import yaml


def load_config(path="config/config.yaml"):
    """
    Load YAML config file from the specified path.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found at: {path}")

    with open(path, "r") as f:
        return yaml.safe_load(f)
