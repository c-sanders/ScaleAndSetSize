SUBDIRS = python


all:

	@echo ""
	@echo "This make target doesn't need to do anything!                                   "
	@echo ""
	@echo "The reason it doesn't need to do anything, is because the GIMP Plugin which is  "
	@echo "installed by this package, is implemented in Python. As a consequence, the      "
	@echo "Plugin doesn't need to be compiled, built, or processed in any other way. It    "
	@echo "just needs to be installed into the appropriate location; that is, the directory"
	@echo "whose name was passed as an argument to the --prefix configure script option.   "
	@echo ""
	@echo "For example, invoking this package's configure script as shown below;           "
	@echo ""
	@echo "  > configure --prefix=/home/foo/.gimp-2.8/plug-ins                             "
	@echo ""
	@echo "will cause the GIMP Plugin to be installed into the directory;                  "
	@echo ""
	@echo "  /home/foo/.gimp-2.8/plug-ins                                                  "
	@echo ""
	@echo "For more information about installing the GIMP Plugin, please refer to the      "
	@echo "INSTALL file which should have been distributed as part of this package.        "
	@echo ""
	@echo "The only make target you need to invoke for this package is;                    "
	@echo ""
	@echo "  > make install                                                                "
	@echo ""
	@echo "Good luck and happy installing ;-)"
	@echo ""


# .PHONY: install
# install:
#
#	chmod 444 ${prefix}/scaleAndSetSize.py
#	chmod 444 ${prefix}/ScaleAndSetSizeObject.py
#	${INSTALL} --verbose --directory  ${prefix}/python
#	${INSTALL} --verbose --target-directory=${prefix} README 
#	${INSTALL} --verbose --target-directory=${prefix}/python ./python/runFfmpeg.py


.PHONY: displaySettings
displaySettings:

	@echo "PREFIX               = @PREFIX@"
	@echo "prefix               = @prefix@"
	@echo "prefix               = ${prefix}"
	@echo "srcdir               = ${srcdir}"
	@echo "builddir             = ${builddir}"
	@echo "GNUPLOT              = ${GNUPLOT}"
	@echo "gimpdir              = ${gimpdir}"
	@echo "INSTALL              = ${INSTALL}"
	@echo "INSTALL_SCRIPT       = ${INSTALL_SCRIPT}"
	@echo "MKDIR_P              = ${MKDIR_P}"
