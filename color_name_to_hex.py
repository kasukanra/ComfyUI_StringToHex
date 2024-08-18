from ColorController import ColorController

class ColorNameToHex:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "color_name": ("STRING", {
                    "multiline": False,
                    "default": "blue"
                }),
            },
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("hex_color",)
    FUNCTION = "convert"
    CATEGORY = "color"

    def convert(self, color_name):
        try:
            color = ColorController(name=color_name)
            hex_codes = color.hex_code
            if isinstance(hex_codes, list):
                # If multiple hex codes are returned, use the first one
                hex_color = hex_codes[0]
            else:
                hex_color = hex_codes
            return (hex_color,)
        except Exception as e:
            print(f"Error converting color name '{color_name}': {str(e)}")
            return ("#000000",)  # Return black as default

NODE_CLASS_MAPPINGS = {
    "ColorNameToHex": ColorNameToHex
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ColorNameToHex": "Color Name to Hex"
}