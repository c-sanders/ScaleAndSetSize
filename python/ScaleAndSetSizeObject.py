from gimpfu import pdb, INTERPOLATION_NONE
from math   import ceil


class ScaleAndSetSizeObject :

	nameClass            = "ScaleAndSetSizeObject"

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

		# 1) Compute and select the appropriate resizing factor.
		# 2) Scale the image using this resizing factor.
		# 3) Resize and crop the image accordingly as certain layers may still have larger older dimensions.
		# 4) Compute the x and y offsets.
		# 5) Offset the image so as to centre it within the new dimensions.

		# self.displayDiagnostics_pre()

		self.computeResizingFactor()

		self.scale()

		self.resizeAndCrop()

		self.offset()

		# self.displayDiagnostics_post()

		self.save()

		print("%s : Exit" % (nameMethod))


	def displayDiagnostics_pre(self) :

		nameMethod = self.nameClass + "::displayDiagnostics_pre"


		print("%s : Enter" % (nameMethod))

		layerList = pdb.gimp_image_get_layers(image)

		print("%s Number of layers in image = %d" % (nameMethod, len(layerList)))

		if pdb.gimp_drawable_is_layer(drawable) :

			print("Drawable is a layer")

		else :

			print("Drawable is NOT a layer")

		activeLayer = pdb.gimp_image_get_active_layer(image)

		print("Desired horizontal resolution of image = %s" % horizontalResolution)
		print("Desired vertical resolution of image   = %s" % verticalResolution)
		print("Current width of image  = %s"                % self.widthImage_original)
		print("Current height of image = %s"                % self.heightImage_original)

		print("%s : Exit" % (nameMethod))


	def displayDiagnostics_post(self) :

		nameMethod = self.nameClass + "::displayDiagnostics_post"


		print("%s : Enter" % (nameMethod))

		layerActive = pdb.gimp_image_get_active_layer(image)

		print layerActive

		[numLayers, listLayers] = pdb.gimp_image_get_layers(image)

		print("Number of layers in the image = %d" % numLayers)

		print("Layer ID = %d" % listLayers[0])

		layerActive.set_offsets(offset_x, offset_y)

		widthImage  = image.width
		heightImage = image.height

		print("Image width  = %s" % widthImage)
		print("Image height = %s" % heightImage)

		print("Drawable width  = %s" % pdb.gimp_drawable_width(drawable))
		print("Drawable height = %s" % pdb.gimp_drawable_height(drawable))

		if (resizeAmountVertical > resizeAmountHorizontal) :

			resizeAmount = resizeAmountHorizontal

			print("resizeAmountVertical > resizeAmountHorizontal")
			print("x difference = %d" % (widthImage_original  - widthImage))
			print("y difference = %d" % (heightImage_original - heightImage))

		else :

			resizeAmount = resizeAmountVertical

			print("resizeAmountVertical <= resizeAmountHorizontal")
			print("x difference = %d" % (widthImage_original  - widthImage))
			print("y difference = %d" % (heightImage_original - heightImage))

		print("%s : Exit" % (nameMethod))


	def computeResizingFactor(self) :

		nameMethod = self.nameClass + "::computeResizingFactor"


		print("%s : Enter" % (nameMethod))

		# Calculate both the horizontal and the vertical scaling factors for the image.

		resizeAmountHorizontal = float(self.horizontalResolution) / float(self.image.width)
		resizeAmountVertical   = float(self.verticalResolution)   / float(self.image.height)

		print("%s : Scale amount horizontal = %f" % (nameMethod, resizeAmountHorizontal))
		print("%s : Scale amount vertical   = %f" % (nameMethod, resizeAmountVertical))

		# Select the smaller of the two scaling factors, otherwise one the dimensions will be too big after scaling.

		if (resizeAmountVertical > resizeAmountHorizontal) :

			self.resizeAmount = resizeAmountHorizontal

		else :

			self.resizeAmount = resizeAmountVertical

		print("%s : Resize amount = %f" % (nameMethod, self.resizeAmount))

		print("%s : Exit" % (nameMethod))


	def scale(self) :

		nameMethod = self.nameClass + "::scale"


		print("%s : Enter" % (nameMethod))

		# Re-scale the image using the scaling factor.

		pdb.gimp_image_scale_full(

		  self.image,
		  ceil(self.resizeAmount * self.image.width),
		  ceil(self.resizeAmount * self.image.height),
		  self.interpolationMode
		)

		#

		widthImage  = self.image.width
		heightImage = self.image.height

		print("%s : New width of image  = %s" % (nameMethod, widthImage))
		print("%s : New height of image = %s" % (nameMethod, heightImage))

		# The image may not have the dimensions we expect as one of the layers of the image may still have the original dimensions.

		if (widthImage != self.horizontalResolution) :

			print("%s : ########################################" % (nameMethod))
			print("%s : Scaled image width = %s"                  % (nameMethod, widthImage))
			print("%s : ########################################" % (nameMethod))

		if (heightImage != self.verticalResolution) :

			print("%s : ########################################" % (nameMethod))
			print("%s : Scaled image height = %s"                 % (nameMethod, heightImage))
			print("%s : ########################################" % (nameMethod))

		print("%s : Exit" % (nameMethod))


	def resizeAndCrop(self) :

		nameMethod = self.nameClass + "::resizeAndCrop"


		print("%s : Enter" % (nameMethod))

		#

		pdb.gimp_image_resize(

		  self.image,
		  self.horizontalResolution,
		  self.verticalResolution,
		  0,
		  0
		)

		# Crop the image.
		#
		# All Channels and Layers within the Image will be cropped to the new Image extents.

		pdb.gimp_image_crop(
		  self.image,
		  self.horizontalResolution,
		  self.verticalResolution,
		  0,
		  0
		)

		print("%s : Exit" % (nameMethod))


	def offset(self) :

		nameMethod = self.nameClass + "::offset"


		print("%s : Enter" % (nameMethod))

		offset_x = int(float(self.horizontalResolution - self.image.width)  / 2)
		offset_y = int(float(self.verticalResolution   - self.image.height) / 2)

		print("%s : Offset x = %d" % (nameMethod, offset_x))
		print("%s : Offset y = %d" % (nameMethod, offset_y))

		# pdb.gimp_layer_set_offsets(
		#   drawable,
		#   360,
		#   0
		# )

		pdb.gimp_drawable_offset(

		  self.drawable,
		  False,
		  0,
		  (self.widthImage_original - self.image.width) / 2,
		  0
		)

		print("%s : Exit" % (nameMethod))


	def save(self) :

		nameMethod = self.nameClass + "::save"


		print("%s : Enter" % (nameMethod))

		# Flatten the image and save it.

		print("%s : About to flatten the image" % (nameMethod))

		drawable = pdb.gimp_image_flatten(self.image)

		# Save the image to a file.

		print("%s : About to save the flattened image to file" % (nameMethod))

		# pdb.file_png_save(drawable,filename,raw_filename,interlace,compression,bkgd,gama,offs,phys,time)

		if (self.filename == None) :

			self.filename = self.image.filename

		pdb.gimp_file_save(

		  self.image,
		  drawable,
		  self.filename,
		  self.filename
		)

		# Don't close or delete the image, as this object didn't open it.

		print("%s : Exit" % (nameMethod))
