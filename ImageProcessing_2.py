
import os


if __name__ == '__main__':
    """
    Put image in in/images folder and protect or object mask in in/masks folder
    Ouput image will be saved to out/images folder with filename_output
    """

    folder_in = 'in'
    folder_out = 'out'

    filename_input = 'image.jpg'
    filename_output = 'image_result.png'
    filename_mask = 'mask.jpg'
    new_height = 200
    new_width = 512
    output_image = os.path.join(folder_out, "images", filename_output)

    
