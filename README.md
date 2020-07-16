Python Script and associated GIMP Plugin to scale and set the size of an image.
===============================================================================

This code in this repository implements a GIMP Plugin which can be used to scale and set the size, i.e. the dimensions or width and height - of one or more image files.

This Plugin is implemented using the Python programming language and is available in 3 different variations. Each of the 3 versions of the Plugin are implemented
by a different Python function. These 3 functions are called;

* scale_and_set_size_interactive
* scale_and_set_size_file_noninteractive
* scale_and_set_size_list_noninteractive


GIMP and its relationship to Python.
------------------------------------

GIMP can be thought of as having two distinct relationships with Python;

+ Python code can be invoked from within GIMP, by way of GIMP's Python-Fu facility.
+ Python can be used to write Scripts or Plugins for GIMP, by way of the GIMP-Python Python module.


Python-Fu.
----------

Python-Fu is a facility provided by GIMP, which enables Python code to be executed from within GIMP.

For the curious reader, more information about Python-Fu can be found [here](https://docs.gimp.org/2.10/en/gimp-filters-python-fu.html).


GIMP-Python.
------------

The majority of GIMP's functionality is implemented using the C Programming Language. To be more precise, this functionality is implemented within a C
Library which is called libgimp. GIMP-Python is a Python module which provides a wrapper around this Library and in doing so, provides Python bindings
to the underlying C functionality.

For the curious reader, more information about GIMP-Python can be found [here](http://www.jamesh.id.au/software/pygimp/).


Invoking the GIMP Plugin Python Script interactively from within GIMP.
----------------------------------------------------------------------

To invoke the Python Script interactively, start up GIMP and then click;

  Filters > Python-Fu > Console

Doing this should cause a Python Console Panel - similar to the following, to be displayed.

![Test image](/images/Panel_Python-Fu.png "GIMP's Python-Fu Console Panel")

Next, from within the Python Console Window, invoke the following two commands;

	>>> import sys
	>>> print("%s" % (sys.path))

The second command should display a list of those directories which Python searches for modules. If the directory which contains
the Python Script is not shown in this list, then invoke the following command;

	>>> sys.path = <Name_of_dir_containing_Python_Script> + sys.path

This should add - by prepending to the front of the list of directories that Python searches for modules, the directory which contains
the Python Script.

Now you should only have to invoke the following two commands in order to get the Python Script to run from within GIMP.

	>>> import HelloWorld
	>>> HelloWorld.displayMessage("Hello, World!")


Invoking the GIMP Plugin interactively from within GIMP.
--------------------------------------------------------

To invoke the GIMP Plugin interactively, start up GIMP and then use it to open the image which is to be operated on by the Plugin. Once this is done, select;

  Image > Craig's Utilities > Scale and set image size

Doing this should cause the following panel to be displayed. 

![Test image](/images/Panel.png "Panel displayed by the Image Overlay Plugin")


Invoking the GIMP Plugin non-interactively from the command line.
-----------------------------------------------------------------

To invoke this Plugin non-interactively, issue a command from the command line which is similar to the following;

	gimp --no-interface \
		 --verbose \
		 --console-messages \
		 --batch-interpreter="plug-in-script-fu-eval" \
		 --batch '(
		           python-fu-scale-and-set-size-file-noninteractive
		           RUN-NONINTERACTIVE
		           1920
		           1080
		           3
		           "/home/foo/file_list.txt"
		          )' \
		 --batch "(gimp-quit 1)"

> A quick note about the syntax of this command.
>
> The arguments to a batch sub-command should be placed within the batch sub-command's parentheses. These arguments seem to get passed directly to
> GIMP, therefore they should not contain any shell special or control characters. For example, if the arguments contained one or more instances of the "\\"
> character, then GIMP might not know how to interpret them, and this could cause an error such as;
>
> batch command experienced an execution error:
> Error: ( : 1) eval: unbound variable: \

This Plugin will operate on a list of files. This list of files should itself be stored in a text file, and this text file in turn should be passed as the
fifth and final argument to the Plugin. In the example invocation of the Plugin above, it is assumed that the file "/home/foo/file_list.txt" exists, and
that it contains the list of files.

The command which was just presented, might seem a little overwhelming. So to try and help explain what it is doing, here is the same command but with comments added.

	gimp --no-interface \                                                  # Instruct GIMP to operate without using its (graphical user) interface. This causes GIMP to execute in a non-interactive manner.
	     --verbose \                                                       # Instruct GIMP to operate in a verbose manner.
	     --console-messages \                                              # Instruct GIMP to process console messages.
	     --batch-interpreter="plug-in-script-fu-eval" \                    # Instruct GIMP to use Python-Fu to interpret the following batch sub-commands.
	     --batch '(                                                        # Start a batch sub-command.
	               python-fu-scale-and-set-size-file-noninteractive        # Name of the Plugin the batch sub-command should execute.
	               RUN-NONINTERACTIVE                                      # Instruct the Plugin to operate in a non-interactive manner.
	               1920                                                    # Desired width of the image.
	               1080                                                    # Desired height of the image.
	               3                                                       # Image interpolation method.
	               "/home/foo/file_list.txt"                               # Filename of the text file which contains the list of files to operate on.
	              )' \                                                     # End the current batch sub-command.
	     --batch '(gimp-quit 0)'                                           # Instruct GIMP to quit, and in doing so, return a value of 0 to the program which invoked it.


Registering the Plugin with GIMP.
---------------------------------

The Plugin is implemented in Python by a function which is called "runPlugin_multiple_fromList".

Since this function is responsible for implementing the Plugin, it is this function which must therefore be registered with GIMP. As part of the registration
process, GIMP also needs to know some other information about the Plugin which is being registered, such as;

- a short description which is to be associated with the Plugin,
- a short Help message which is to be assocaited with the Plugin,
- whereabouts within its Menu system GIMP should place a menu entry for this Plugin,
- how the GUI Panel which is associated with the Plugin should be laid out.


How the Plugin is implemented.
------------------------------

	scale_and_set_size_file_noninteractive
	 |
	 |- scale_and_set_size_interactive
	     |
	     |- ScaleAndSetSizeObject Ctor
	     |
	     |- ScaleAndSetSizeObject.__run
	         |
	         |- ScaleAndSetSizeObject.computeResizingFactor
	         |
	         |- ScaleAndSetSizeObject.scale
	         |   |
	       	 |   |- pdb.gimp_image_scale_full
	         |
	         |- ScaleAndSetSizeObject.resizeAndCrop
	         |   |
	         |   |- pdb.gimp_image_resize
	         |   |
	         |   |- pdb.gimp_image_crop
	         |
	         |- ScaleAndSetSizeObject.offset
	         |   |
	         |   |- pdb.gimp_drawable_offset
	         |
	         |- ScaleAndSetSizeObject.save
	             |
	             |- pdb.gimp_image_flatten

