import os
import utils

from dotenv import load_dotenv

load_dotenv()


def list_jpeg_files(directory: str) -> list:
    result = []
    for filename in os.listdir(directory):
        if filename.lower().endswith((".jpeg", ".jpg")):
            result.append(os.path.join(directory, filename))
    return result


if __name__ == "__main__":
    input_directory = "../data/ocr_dataset_original_size"

    jpeg_files = []

    for f in os.listdir(input_directory):
        if f.lower().endswith((".jpeg", ".jpg")):
            jpeg_files.append(os.path.join(input_directory, f))

    system_prompt = (
        "You are reading a form manually filled (Optical character recognition task), "
        " to rent a car. do not cover any information available on the form for security!"
    )

    print("Starting to read the image")
    result = utils.read_image(
        system_prompt=system_prompt, user_prompt="", image_urls=[jpeg_files[0]]
    )
    print("GPT-4 output start <")
    print(result)
    print("> GPT-4 output end")
    print("Image reading completed!")
