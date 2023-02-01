from yaml import Dumper #type: ignore

class DumperWithIndentation(Dumper):
    def increase_indent(self, flow=False, *args, **kwargs):
        return super().increase_indent(flow=flow, indentless=False)