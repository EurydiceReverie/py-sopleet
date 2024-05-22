import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Ensure that spleeter is installed
try:
    import spleeter
except ImportError:
    install('spleeter')

from spleeter.separator import Separator

# Custom configuration
custom_config = {
    "codec": "wav",
    "bitrate": "1411k",
    "sample_rate": 44100,
    # Add additional configuration parameters if needed
}

def extract_stems(input_file, output_path, stems=2):
    separator_config_string = f'spleeter:{stems}stems'
    separator = Separator(separator_config_string)
    separator.separate_to_file(input_file, output_path)
    print(f'Stems extracted successfully to {output_path}')

# Example usage
extract_stems('06. This Is Heaven - Nick Jonas - Spaceman - USUM72102471.mp3', 'output', stems=5)