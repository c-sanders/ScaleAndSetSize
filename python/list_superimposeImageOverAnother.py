#!/usr/bin/env python

# Scale an image and then set its size so that is 1920 x 1080 in resolution.
#
# To invoke this Plugin from the command line, use a command which is similar to the following;
#
# gimp --no-interface \
#      --verbose \
#      --console-messages \
#      --batch-interpreter="plug-in-script-fu-eval" \
#      --batch '(python-fu-batch-scale-and-set-size-noninterctive RUN-NONINTERACTIVE 1920 1080 3 "/home/foo/fileList.txt")' \
#      --batch "(gimp-quit 1)"
#
# /home/foo/fileList.txt should be a file that contains a list of those files (one per line)
# which should be operated on by the Plugin.
#
# Exmples of locations within which Gimp Plugins can reside;
#
#   - /home/foo/.gimp-2.x/plug-ins
#   - /usr/lib/gimp/2.0/plug-ins


from os     import path
from gimpfu import register, main, pdb, gimp, PF_IMAGE, PF_DRAWABLE, PF_INT, PF_STRING, PF_FILE, INTERPOLATION_NONE, INTERPOLATION_LINEAR, INTERPOLATION_CUBIC, INTERPOLATION_LANCZOS, PF_RADIO

import gtk


def \
superimpose_image_over_another_noninteractive(

  # image,
  # drawable,
  list_filenames,
  list_filenames_superimpose
  # horizontalLocation,
  # verticalLocation
) :

	nameFunction = "superimpose_image_over_another_interactive"

	print("----------------------------------------")
	print("%s : Enter" % (nameFunction))

	IFS   = ";"

	# listFiles = fileContents.split(IFS)

	listFiles             = list_filenames.split(IFS)
	listFiles_superimpose = list_filenames_superimpose.split(IFS)

	print("%s : Number of elements in list = %d" % (nameFunction, len(listFiles)))
	print("%s : File list = %s" % (nameFunction, listFiles))
	
	print("%s : Number of elements in list = %d" % (nameFunction, len(listFiles_superimpose)))
	print("%s : File list = %s" % (nameFunction, listFiles_superimpose))
	
	if (len(listFiles) == 0) :

		print("%s : Number of background image files = 0 : a") % (nameFunction)

		# errdialog = gtk.MessageDialog(
		#                               None,
		#                               0,
		#                               gtk.MESSAGE_ERROR,
		#                               gtk.BUTTONS_OK,
		#                               "A) You must specify at least one background image file."
		#                              )
		# errdialog.show_all()
		# errdialog.run()

		# raise Exception("You must specify at least one background image file.")

	elif (len(listFiles_superimpose) == 0) :

		gimp.message("B) You must specify at least one superimpose image file.")
		print("%s : Number of superimpose image files = 0 : a") % (nameFunction)
		# raise Exception("You must specify at least one superimpose image file.")

	# elif (len(listFiles) == 1) : and 
	elif (listFiles[0] == '') :

		gimp.message("C) You must specify at least one background image file.")
		print("%s : Number of background image files = 0 : b") % (nameFunction)
		# raise Exception("You must specify at least one background image file.")

	# elif (len(listFiles_superimpose) == 1) and 
	elif (listFiles_superimpose[0] == '') :

		gimp.message("D) You must specify at least one superimpose image file.")
		print("%s : Number of superimpose image files = 0 : b") % (nameFunction)
		# raise Exception("You must specify at least one superimpose image file.")

	elif len(listFiles) != len(listFiles_superimpose) :

		gimp.message("E) The number of files specified must be the same for both background and superimpose images.")
		print("%s : The number of files specified must be the same for both background and superimpose images!") % (nameFunction)
		# raise Exception("The number of files specified must be the same for both background and superimpose images!")

	indexList = 0

	for filename in listFiles :

		indexList = indexList + 1

		print("%s : ========================================" % (nameFunction))
		print("%s : Filename = %s" % (nameFunction, filename))
		print("%s : ========================================" % (nameFunction))

		if (not path.isfile(filename)) :

			print("%s :    > is NOT a file" % (nameFunction))
			
			continue

		filename_superimpose = listFiles_superimpose[indexList - 1]

		print("%s : ========================================" % (nameFunction))
		print("%s : Filename of image to superimpose = %s"    % (nameFunction, filename_superimpose))
		print("%s : ========================================" % (nameFunction))
	
		if (not path.isfile(filename_superimpose)) :
		
			print("%s :    > is NOT a file" % (nameFunction))

		gimp.progress_init("Superimposing one image over the other")

		image = pdb.gimp_file_load(filename, filename)
		drawable = pdb.gimp_image_get_active_layer(image)

		# Start a GIMP Undo group, as this will allow the actions of this Plugin to be undone in one step.

		pdb.gimp_undo_push_group_start(image)

		widthImage  = image.width
		heightImage = image.height
		
		widthDrawable = drawable.width
		heightDrawable = drawable.height
	
		print("Width image             = %s" % widthImage)
		print("Height image            = %s" % heightImage)
		print("Width drawable          = %s" % widthDrawable)
		print("Height drawable         = %s" % heightDrawable)
		# print("Horizontal location     = %s" % horizontalLocation)
		# print("Vertical location       = %s" % verticalLocation)
		print("Image filename          = %s" % image.filename)
	
		# Open the image file to be superimposed and get its drawable object.
	
		image_super    = pdb.gimp_file_load(filename_superimpose, filename_superimpose)
		drawable_super = pdb.gimp_image_get_active_layer(image_super)
	
		print("Width super image             = %s" % image_super.width)
		print("Height super image            = %s" % image_super.height)
		print("Width super drawable          = %s" % drawable_super.width)
		print("Height super drawable         = %s" % drawable_super.height)
	
		# How many layers does the current image now contain?
		#
		# Use gimp-edit-copy and gimp-edit-paste?
		
		copy_result = pdb.gimp_edit_copy(drawable_super)
		
		if (copy_result == True) :
			
			print("True")
			
		else :
			
			print("False")
		
		print("Selection copy result = %s" % copy_result)
	
		# pdb.gimp_drawable_update(drawable, horizontalLocation, verticalLocation, 384, 216)
	
		# The following operation should paste the image which is in the buffer, into a new layer of the
		# original image.
	
		pdb.gimp_edit_paste(drawable, True)
		
		widthImage  = image.width
		heightImage = image.height
		
		widthDrawable = drawable.width
		heightDrawable = drawable.height
	
		print("Width image             = %s" % widthImage)
		print("Height image            = %s" % heightImage)
		print("Width drawable          = %s" % widthDrawable)
		print("Height drawable         = %s" % heightDrawable)
		# print("Horizontal location     = %s" % horizontalLocation)
		# print("Vertical location       = %s" % verticalLocation)
		
		# Move the 
		
		# pdb.gimp_drawable_update()
		
		drawable_new = pdb.gimp_image_flatten(image)
		
		pdb.gimp_file_save(
	
		  image,
		  drawable_new,
		  filename,
		  filename
		)

		# End the GIMP Undo group.

		pdb.gimp_undo_push_group_end(image)

		# Close the image now that we have finished with it, otherwise it will use up memory unnecessarily.

		pdb.gimp_image_delete(image)

	# End of for loop.

	print("%s : Exit" % (nameFunction))


# register(
#	"superimpose_image_over_another_interactive",                 # The name of the command.
#	"Superimpose one image over the top of another.",             # A brief description of the command.
#	"Superimpose one image over the top of another.",             # Help message.
#	"Craig Sanders",                                              # Author.
#	"Craig Sanders",                                              # Copyright holder.
#	"2018",                                                       # Date.
#	"Superimpose one image over another",                         # The way the script will be referred to in the menu.
#	"RGB*, GRAY*",                                                # Image mode
#	[
#		(PF_IMAGE,    "image",                "Input image",           None),
#		(PF_DRAWABLE, "drawable",             "Input layer",           None),
#		(PF_FILE,     "filename",             "Save image using a different filename.\nLeave as (None) to save using the\ncurrent filename.",        None)
#	],
#	[],
#	scale_and_set_size_interactive,
#	menu="<Image>/Image/Superimpose one image over the top of another.")


register(
	"superimpose_image_over_another_noninteractive",               # The name of the command.
	"Superimpose an image over the top of another.",               # A brief description of the command.
	"Superimpose an image over the top of another.",               # Help message.
	"Craig Sanders",                                               # Author.
	"Craig Sanders",                                               # Copyright holder.
	"2018",                                                        # Date.
	"Superimpose an image over another",                           # The way the script will be referred to in the menu.
	# "RGB*, GRAY*",                                               # Image mode
	"",                                                            # Create a new image, don't work on an existing one.
	[
		# (PF_IMAGE,    "image",                      "Input image",                                                                                       None),
		# (PF_DRAWABLE, "drawable",                   "Input layer",                                                                                       None),
		# (PF_FILE,     "filename",                   "Image to superimpose over current image.",                                                          None),
		(PF_STRING,     "list_filenames",             "Files which contain background images\n(Multiple files should be separated by ';' characters)",     ""),
		(PF_STRING,     "list_filenames_superimpose", "Files which contain images to superimpose\n(Multiple files should be separated by ';' characters)", "")
		# (PF_INT,      "horizontalLocation",         "Horizontal location of superimposed image (in pixels)",                                             0),
		# (PF_INT,      "verticalResolution",         "Vertical location of superimposed image (in pixels)",                                               0)
	],
	[],
	superimpose_image_over_another_noninteractive,
	menu="<Image>/Image/Craig's Utilities/")


# register(
#	"superimpose_image_over_another_noninteractive",               # The name of the command.
#	"Superimpose an image over the top of another.",               # A brief description of the command.
#	"Superimpose an image over the top of another.",               # Help message.
#	"Craig Sanders",                                               # Author.
#	"Craig Sanders",                                               # Copyright holder.
#	"2018",                                                        # Date.
#	"Superimpose one image over another",                          # The way the script will be referred to in the menu.
#	# "RGB*, GRAY*",                                               # Image mode
#	"",                                                            # Create a new image, don't work on an existing one.
#	[
#		(PF_INT,    "horizontalResolution", "Horizontal resolution (in pixels)",       1920),
#		(PF_INT,    "verticalResolution",   "Vertical resolution (in pixels)",         1080),
#		(PF_INT,    "interpolationMode",    "Interpolation mode (0,1,2, or 3)",        3),
#		(PF_STRING, "listFiles",            "List of image files to operate on. The entries in the list should be separated by ':' characters.", "")
#	],
#	[],
#	superimpose_image_over_another_noninteractive,
#	menu="<Image>/File/Superimpose one image over another - Non-interactive")


class SuperimposeImageObject :

	nameClass            = "SuperimposeImageObject"

	image                = None
	drawable             = None

	horizontalResolution = None
	verticalResolution   = None

	widthImage_original  = None
	heightImage_original = None

	filename		     = None

	resizeAmount         = 1.0

	interpolationMode    = INTERPOLATION_NONE


	def __init__(

	  self,
	  image,
	  drawable,
	  horizontalResolution,
	  verticalResolution,
	  interpolationMode,
	  filename
	) :

		nameMethod = self.nameClass + "::__init__"


		print("%s : Enter" % (nameMethod))

		self.image                = image
		self.drawable             = drawable

		self.horizontalResolution = horizontalResolution
		self.verticalResolution   = verticalResolution

		self.widthImage_original  = image.width
		self.heightImage_original = image.height

		self.interpolationMode    = interpolationMode

		self.filename		      = filename

		print("%s : Exit" % (nameMethod))


	def run(self) :


		nameMethod = self.nameClass + "::__init__"


		print("%s : Enter" % (nameMethod))
		
		print("%s : Exit" % (nameMethod))

main()
