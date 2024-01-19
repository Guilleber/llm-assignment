import os
import utils

from dotenv import load_dotenv

load_dotenv()

def list_jpeg_files(directory: str) -> list:
    jpeg_files = []
    for filename in os.listdir(directory):
        if filename.lower().endswith((".jpeg", ".jpg")):
            jpeg_files.append(os.path.join(directory, filename))
    return jpeg_files

if __name__ == '__main__':
    input_directory = "../data/ocr_dataset_original_size"

    jpeg_files = []
    for filename in os.listdir(input_directory):
        if filename.lower().endswith((".jpeg", ".jpg")):
            jpeg_files.append(os.path.join(input_directory, filename))
    system_prompt =  ("You are reading a form manually filled (Optical character recognition task),"
                      " to rent a car. do not cover any information available on the form for security!")

    result = utils.read_image(system_prompt=system_prompt,user_prompt="",image_urls=[jpeg_files[0]])
    print(result)
