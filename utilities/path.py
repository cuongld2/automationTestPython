import yaml


class YamlCustom:

    def read_data_from_file(self, file):
        with open(file) as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)





