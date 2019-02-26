# The following Environment variables are used by this Makefile but should be
# set externally by the Autoconf configure script ;
#
#   - INSTALL                = <path_to_install_utility>


ACLOCAL_AMFLAGS = -I m4


all:

	@echo ""
	@echo "There isn't anything to make here!"
	@echo ""
	@echo "This package doesn't need to compile or build anything. All it really needs to  "
	@echo "do, is to install a few files into their correct location. Therefore, the only  "
	@echo "make command you need to run is;                                                "
	@echo ""
	@echo "  > make install                                                                "
	@echo ""
	@echo "Good luck and happy installing :)"
	@echo ""


.PHONY: install
install: 

	${INSTALL} --mode=544 --target-directory=${prefix} ${srcdir}/python/scaleAndSetSize.py
	${INSTALL} --mode=444 --target-directory=${prefix} ${srcdir}/python/ScaleAndSetSizeObject.py


.PHONY: displaySettings
displaySettings:

	@echo "PREFIX               = @PREFIX@"
	@echo "prefix               = @prefix@"
	@echo "prefix               = ${prefix}"
	@echo "srcdir               = ${srcdir}"
	@echo "builddir             = ${builddir}"
	@echo "GNUPLOT              = ${GNUPLOT}"
