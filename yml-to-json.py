#!/usr/bin/env python3

import json
from pathlib import Path
import sys
import yaml


def convert_all_yml_to_json(folder_path):
    """

    :param folder_path:
    :return:
    """
    yml_paths = folder_path.glob('*.yml')

    for yml_path in yml_paths:
        with yml_path.open(mode='r') as yml_file:
            yml_data = yaml.load(yml_file, Loader=yaml.FullLoader)

        json_path = yml_path.parent / '{}.json'.format(yml_path.stem)
        with json_path.open(mode='w') as json_file:
            # print(json.dumps(yml_data, indent=2))
            json.dump(yml_data, json_file, indent=2)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        yml_path = Path(' '.join(sys.argv[2:])).resolve()
    else:
        yml_path = Path(__file__).resolve().parent

    # print(yml_path)
    convert_all_yml_to_json(yml_path)
