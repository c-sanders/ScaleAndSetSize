#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

# Shown below, is an example invocation of the resulting configure script. This will install the
# Gimp plugin(s) into /home/craig/.gimp-2.8/plug-ins
#
#   > ./configure --prefix=/home/craig/.gimp-2.8/plug-ins


# Invoke the necessary Autotools initialisation macros.
# -----------------------------------------------------

AC_PREREQ([2.69])

AC_INIT(
	[gimp_scaleandsetsize_plugin],
	[0.1],
	[craig@gravitas-toolworks.com])

AM_INIT_AUTOMAKE()

# The invocation of LT_INIT below, means that AC_PROG_RANLIB does not need to be
# invoked, as might be suggested by autoscan.

# LT_INIT()

# AC_CONFIG_SRCDIR([python/AnimationGenerator.py])


# Tell Autoconf where certain macros should be loaded from.
# ---------------------------------------------------------

# AC_CONFIG_MACRO_DIRS([m4])

# m4_include([m4/ax_compare_version.m4])
# m4_include([m4/ax_gnuplot.m4])
# m4_include([m4/ax_ffmpeg.m4])


# Checks for programs.
# --------------------

AC_PROG_CXX()

AC_PROG_INSTALL()

AC_PROG_MAKE_SET()


# Generate the necessary files.
# -----------------------------

AC_CONFIG_FILES(
	[Makefile \
	 python/Makefile])

AC_OUTPUT
