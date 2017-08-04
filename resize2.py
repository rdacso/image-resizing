import os, sys
from PIL import Image

path = $PATH
current_directory = os.listdir(path)
agency = $AGENCY
env = "test"

def maybe_convert_extension(filename):
    if not filename.lower().endswith('.jpg'):
        new_file = Image.open(filename)
        convert_file = new_file.convert('RGB')
        covert_file.save(new_file)

        return new_file
    return filename
def get_dimensions(filename):
    img = Image.open(filename)
    f, e = os.path.splitext(filename)
    # XXXX: this returned an errror. We should handle the error.
    nf = f + '-converted.jpg'

    width = img.size[0]
    height = img.size[1]
    ratio = 1.5
    ratio_height = ratio * height

    if width > ratio_height:
        new_width = ratio_height
        new_height = height
        left = (width - new_width)/2
        top = (height - new_height)/2
        right = (width + new_width)/2
        bottom = (height + new_height)/2
    else:
        new_height = width/ratio
        new_width = width
        left = (width - new_width)/2
        top = (height - new_height)/2
        right = (width + new_width)/2
        bottom = (height + new_height)/2

    new_image = img.crop((left, top, right, bottom))

    imResize = new_image.resize((900,600), Image.NEAREST)
   
    
    
    imResize.save(nf, 'JPEG', quality=74, optimize=True)

    imResize.show()
    return nf


def process_image_file(filename):
    keyword = filename[:-4]
    print keyword
    newfilename = maybe_convert_extension(filename)
    print newfilename
    newfilename = get_dimensions(newfilename)
    print keyword, ":", newfilename
    # XXX: now we run 
    # ../../cmd --env=$env add_security_image --agency_id $agn 
    # --image $file --keyword SBTC --credit_title 'By OmniTrans' --credit_url 'http://www.omnitrans.org/'
    command = 'wk ../../cmd --env=' + env + ' add_security_image --agency_id=' + agency + " --image=" + newfilename + " --keyword=" + keyword + " --credit_title 'By AGENCY' --credit_url 'https://www.google.com'"
    os.system(command)


def process_all_image_files():
    # Clear current image files
    command = "wk ../../cmd --env=" + env + " clear_security_images --agency_id=" + agency
    os.system(command)

    #iterate through files
    for item in current_directory:
        if item.lower().endswith(('.jpg', '.png')) and not item.startswith('.'):
            process_image_file(item)


process_all_image_files()


