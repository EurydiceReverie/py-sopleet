import spleeter

def separate_audio(input_file, output_folder):
    """Separates an audio file into stems using Spleeter.

    Args:
        input_file (str): Path to the input audio file.
        output_folder (str): Path to the folder where the stems will be saved.
    """

    # Pre-trained models: 2stems, 4stems, 5stems
    stems = "5stems"

    # Configure Spleeter
    config = spleeter.AudioConfiguration(
        bitrate="320k",
        stft_backend="auto", # Choose an appropriate STFT backend (e.g., "librosa")
        multiprocess=True  # Set according to your system resources
    )

    # Separate the audio using the specified model
    separator = spleeter.Separator(f"spleeter:{stems}", config)
    separator.separate_to_file(input_file, output_folder)

if __name__ == "__main__":
    input_file = "//path-here//song-file.mp3"  # Replace with your audio file
    output_folder = "//path-here" 

    separate_audio(input_file, output_folder)