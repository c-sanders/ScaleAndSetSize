# The following Environment variables are used by this Makefile but should be
# set externally by the configure script ;
#
#   - INSTALL = <path_to_install_utility>


# Install these files into the directory which is specified by ${prefix}

gimpdir         = ${prefix}
gimp_supportdir = ${prefix}

gimp_SCRIPTS         = scaleAndSetSize.py
gimp_support_SCRIPTS = ScaleAndSetSizeObject.py


# all:
#
#	@echo ""
#	@echo "This make target doesn't need to do anything!                                   "
#	@echo ""
#	@echo "For more information as to why it doesn't need to do anything, please invoke    "
#	@echo "this exact same make target from within the parent directory.                   "
#	@echo ""


install-exec-hook: install-gimp-plugins
.PHONY: install-gimp-plugins
install-gimp-plugins:

	${MKDIR_P} ${prefix}
	${INSTALL} -m 544 ${gimp_SCRIPTS} ${prefix}
	${INSTALL} -m 444 ${gimp_support_SCRIPTS} ${prefix}


.PHONY: displaySettings
displaySettings:

	@echo "PREFIX               = @PREFIX@"
	@echo "prefix               = @prefix@"
	@echo "prefix               = ${prefix}"
	@echo "srcdir               = ${srcdir}"
	@echo "builddir             = ${builddir}"
	@echo "GNUPLOT              = ${GNUPLOT}"
	@echo "gimpdir              = ${gimpdir}"
	@echo "DESTDIR              = ${DESTDIR}"
	@echo "destdir              = ${destdir}"
