import importlib
import subprocess
import sys

def check_and_install_dependencies():
    required_packages = ['colorcontroller']
    
    for package in required_packages:
        try:
            importlib.import_module(package)
        except ImportError:
            print(f"{package} not found. Attempting to install...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"{package} installed successfully.")

check_and_install_dependencies()

from .color_name_to_hex import ColorNameToHex

NODE_CLASS_MAPPINGS = {
    "ColorNameToHex": ColorNameToHex
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ColorNameToHex": "Color Name to Hex"
}

__all__ = ['NODE_CLASS_MAPPINGS']