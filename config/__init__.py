import configparser
import os


def create_config(path):
    config = configparser.ConfigParser()
    config.add_section("default")
    config.set("default", "inp", "request")
    config.set("default", "out", "mongo")
    config.set("default", "info", "Use of %(inp)s and %(out)s tools")

    with open(path, "w") as config_file:
        config.write(config_file)


def write_config(cfg, path):
    with open(path, "w") as config_file:
        cfg.write(config_file)


def get_config(path):
    if not os.path.exists(path):
        create_config(path)

    config = configparser.ConfigParser()
    config.read(path)
    return config


def get_sections(path):
    config = get_config(path)
    return config.sections()


def get_section(path, section):
    config = get_config(path)
    return dict(config.items(section))


def get_setting(path, section, setting):
    config = get_config(path)
    value = config.get(section, setting)
    msg = "{section} {setting} is {value}".format(
        section=section, setting=setting, value=value)
    print(msg)
    return value


def update_setting(path, section, setting, value):
    config = get_config(path)
    config.set(section, setting, value)
    with open(path, "w") as config_file:
        config.write(config_file)


def delete_setting(path, section, setting):
    config = get_config(path)
    config.remove_option(section, setting)
    with open(path, "w") as config_file:
        config.write(config_file)

# path = "conf/data.ini"
# cnf = get_config(path)
# cnff = {s:dict(cnf.items(s)) for s in cnf.sections() }
# print(cnff)

# print(get_sections("conf/data.ini"))
# print(get_section("conf/data.ini", 'default'))
