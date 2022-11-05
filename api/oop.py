class InstrumentDisplay:
    def display():
        ...


class ColorMap:
    color_map = {
        'beżowy': '#faf7e6,',
        'brązowy': '#724330,',
        'biały': '#ffffff,',
        'czarny': '#0b0b0b,',
        'czerwony': '#ec1d2f,',
        'fioletowy': '#6341b4,',
        'różowy': '#fa9cac,',
        'zielony': '#a8e74f,',
        'niebieski': '#00a6e7,',
        'pomarańczowy': '#ff7d05,',
        'szary': '#979895,',
        'turkusowy': '#18d7cb,',
        'żółty': '#ffe70e,',
        'drewno jasne': '000000',
        'drewno średnie': '000000',
        'drewno ciemne': '000000',
        'wielobarwny': 'linear-gradient(#EC1D2F, #00A6E7, #5DAF1A, #FFE70E, #EC1D8C)'
    }

    def avaliable_colors(self):
        return self.color_map.keys()

    def get_css_value(self, name):
        # TODO add validation
        return 


class Color:
    @staticmethod
    def get_color_hex(name):
        return name

    def __init__(self, name) -> None:
        self.name = name
        self.hex = self.get_color_hex(self.name)