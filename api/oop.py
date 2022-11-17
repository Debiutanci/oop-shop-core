class InstrumentDisplay:
    def display(self):
        ...


class ColorMap:
    color_map = {
        'beżowy': '#faf7e6',
        'brązowy': '#724330',
        'biały': '#ffffff',
        'czarny': '#0b0b0b',
        'czerwony': '#ec1d2f',
        'fioletowy': '#6341b4',
        'różowy': '#fa9cac',
        'zielony': '#a8e74f',
        'niebieski': '#00a6e7',
        'pomarańczowy': '#ff7d05',
        'szary': '#979895',
        'turkusowy': '#18d7cb',
        'żółty': '#ffe70e',
        'drewno jasne': '000000',
        'drewno średnie': '000000',
        'drewno ciemne': '000000',
    }

    @property
    def avaliable_colors(self):
        return self.color_map.keys()

    def get_css_value(self, name):
        return self.color_map[name]


class Color:
    @staticmethod
    def __get_color_hex(name):
        cm = ColorMap()
        try:
            return cm.get_css_value(name=name)
        except KeyError:
            return None

    def __init__(self, name) -> None:
        self.name = name
        self.hex = self.__get_color_hex(self.name)

    def json(self):
        return {
            "name": self.name,
            "hex": self.hex
        }
