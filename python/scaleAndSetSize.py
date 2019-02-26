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

from ScaleAndSetSizeObject import ScaleAndSetSizeObject


def \
scale_and_set_size_interactive(

  image,
  drawable,
  horizontalResolution,
  verticalResolution,
  interpolationMode,
  filename
) :

	nameFunction = "scale_and_set_size_noninteractive"


	print("%s : Enter" % (nameFunction))

	gimp.progress_init("Scaling and setting the size of image : " + image.filename)

	# Start a GIMP Undo group, as this will allow the actions of this Plugin to be undone in one step.

	pdb.gimp_undo_push_group_start(image)

	scaleAndSetSizeObject = ScaleAndSetSizeObject(

							  image,
							  drawable,
							  horizontalResolution,
							  verticalResolution,
							  interpolationMode,
							  filename
							)

	scaleAndSetSizeObject.run()

	# End the GIMP Undo group.

	pdb.gimp_undo_push_group_end(image)

	print("%s : Exit" % (nameFunction))


def \
scale_and_set_size_noninteractive(

  horizontalResolution,
  verticalResolution,
  interpolationMode,    # 0,1,2,3 : 3 = INTERPOLATION_LANCZOS
  listFiles
) :

	nameFunction = "scale_and_set_size_noninteractive"


	print("%s : Enter" % (nameFunction))

	print("%s : Checking if Interpolation mode value is valid" % (nameFunction))

	if (interpolationMode == INTERPOLATION_LANCZOS) :

		interpolationMode = 3

	# if ((int(interpolationMode) < 0) or (int(interpolationMode) > 3)) :

	else :

		print("%s : Interpolation mode value is NOT valid = %s" % (nameFunction, str(interpolationMode)))

		raise Exception("Invalid value for parameter : interpolationMode")

	print("%s : Interpolation mode value IS valid = %s" % (nameFunction, interpolationMode))

	debug = False

	IFS   = ":"

	# fileHandle = open(listFile, "r")

	# listFiles = fileHandle.read().splitlines()

	# fileHandle.close()

	# listFiles = fileContents.split(IFS)

	listFiles_split = listFiles.split(IFS)

	listFiles = listFiles_split

	print("%s : Number of elements in list = %d" % (nameFunction, len(listFiles)))
	print("%s : File list = %s" % (nameFunction, listFiles))

	for filename in listFiles :

		print("%s : ========================================" % (nameFunction))
		print("%s : Filename = %s" % (nameFunction, filename))
		print("%s : ========================================" % (nameFunction))

		if (not path.isfile(filename)) :

			print("%s :    > is NOT a file" % (nameFunction))

			continue

		# Open the image file and get its drawable object.

		image    = pdb.gimp_file_load(filename, filename)
		drawable = pdb.gimp_image_get_active_layer(image)

		#

		scale_and_set_size_interactive(
		  image,
		  drawable,
		  horizontalResolution,
		  verticalResolution,
		  interpolationMode,
		  filename
		)

		# Close the image now that we have finished with it, otherwise it will use up memory unnecessarily.

		pdb.gimp_image_delete(image)

		print("%s : Exit" % (nameFunction))


register(
	"scale_and_set_size_interactive",                             # The name of the command.
	"Scale and set an image to a particular size",                # A brief description of the command.
	"Scale and set an image to a particular size",                # Help message.
	"Craig Sanders",                                              # Author.
	"Craig Sanders",                                              # Copyright holder.
	"2018",                                                       # Date.
	"Scale and set image size",                                   # The way the script will be referred to in the menu.
	"RGB*, GRAY*",                                                # Image mode
	[
		(PF_IMAGE,    "image",                "Input image",           None),
		(PF_DRAWABLE, "drawable",             "Input layer",           None),
		(PF_INT,      "horizontalResolution", "Horizontal resolution", 1920),
		(PF_INT,      "verticalResolution",   "Vertical resolution",   1080),
		# (PF_INT,      "interpolationMode",    "Interpolation mode",    3),
		(PF_RADIO,    "interpolationMode",     "Inerpolation mode",       3,
		  (
			("None",            INTERPOLATION_NONE),
			("Linear",          INTERPOLATION_LINEAR),
			("Cubic",           INTERPOLATION_CUBIC),
			("Sinc (Lanczos3)", INTERPOLATION_LANCZOS)
		  )
		),
		(PF_FILE,     "filename",             "Save image using a different filename.\nLeave as (None) to save using the\ncurrent filename.",        None)
	],
	[],
	scale_and_set_size_interactive,
	menu="<Image>/Image/Craig's Utilities")                # The name used to refer to the action


register(
	"scale_and_set_size_noninteractive",                          # The name of the command.
	"Scale and set an image to a particular size",                # A brief description of the command.
	"Scale and set an image to a particular size",                # Help message.
	"Craig Sanders",                                              # Author.
	"Craig Sanders",                                              # Copyright holder.
	"2018",                                                       # Date.
	"Scale and set image size",                                   # The way the script will be referred to in the menu.
	# "RGB*, GRAY*",                                              # Image mode
	"",                                                           # Create a new image, don't work on an existing one.
	[
		(PF_INT,    "horizontalResolution", "Horizontal resolution (in pixels)",       1920),
		(PF_INT,    "verticalResolution",   "Vertical resolution (in pixels)",         1080),
		(PF_INT,    "interpolationMode",    "Interpolation mode (0,1,2, or 3)",         3),
		(PF_STRING, "listFiles",            "List of files to operate on (the files in the list should be separated by ':' characters)", "")
	],
	[],
	scale_and_set_size_noninteractive,
	menu="<Image>/File/Batch process files")


main()
