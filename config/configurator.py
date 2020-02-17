#!python3.7

import configparser

file_path = "conf/db3.ini"
parser = configparser.ConfigParser()


def config_parser(config_file):
    try:
        parser.read(config_file)
    except configparser.ParsingError as e:
        print("\n Error configparser", e)

    for section_name in parser:
        print('\nSection:', section_name)
        section = parser[section_name]
        print('  Options:', list(section.keys()))
        for name in section:
            print('  {} = {}'.format(name, section[name]))
        print()


# parse config file
config_parser(file_path)


