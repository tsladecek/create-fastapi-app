import os
import pathlib
import subprocess


def apply_template_option(option_name: str, option: str, target: str):
    options_name_dir = pathlib.PurePath(pathlib.Path(__file__).resolve().parent, 'options', option_name)
    options_dir = pathlib.PurePath(options_name_dir, option)

    for op_dir in [options_name_dir, options_dir]:
        for f in os.listdir(op_dir):
            if f.endswith('py') and f != '__init__.py':
                subprocess.run(['cp', pathlib.PurePath(op_dir, f), pathlib.PurePath(target, f.replace('-', '/'))])
