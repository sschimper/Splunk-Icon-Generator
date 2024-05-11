import argparse
from PIL import Image, ImageOps

def create_splunk_icons():
    parser = argparse.ArgumentParser(
                        prog="splicon",
                        description="""Creates icons to be used for developing Splunk apps and add-ons via resizing a provided image.\n
                        More information about Splunk"s required image sizes can be found here:\n
                        https://dev.splunk.com/enterprise/docs/developapps/createapps#Add-icons-to-your-app
                        """
    )

    parser.add_argument("filename", help="Image file from which the Splunk icons are generated.")           
    parser.add_argument("-d", "--destination", help="Directory/Folder for storing the processed icons.")
    parser.add_argument("-v", "--version", action="version", version="1.0.1", help="Prints the version.")
    args = parser.parse_args()

    output_directory = "."
    if (args.destination):
        output_directory = args.destination

    with Image.open(args.filename) as im:
        ImageOps.contain(im, (72, 72)).save(f"{output_directory}/appIcon_2x.png")
        ImageOps.contain(im, (72, 72)).save(f"{output_directory}/appIconAlt_2x.png")

        ImageOps.contain(im, (36, 36)).save(f"{output_directory}/appIcon.png")
        ImageOps.contain(im, (36, 36)).save(f"{output_directory}/appIconAlt.png")

        ImageOps.contain(im, (160, 40)).save(f"{output_directory}/appLogo.png")
        ImageOps.contain(im, (320, 80)).save(f"{output_directory}/appLogo_2x.png")

    print("Resizing successfully completed!")
