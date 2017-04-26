AC_INIT(CWiid,3.0.0,https://github.com/azzra/python3-wiimote/issues)
AC_CONFIG_HEADER(common/include/config.h)

AC_PROG_CC
AC_PROG_AWK
AC_PROG_LEX
if test "$LEX" != "flex"; then
	AC_MSG_ERROR([flex not found])
fi
if test -z "`echo %%|$LEX -t|grep yypop_buffer_state`"; then
	AC_MSG_ERROR([flex missing yypop_buffer_state - upgrade to version 2.5.33 or later])
fi
AC_PROG_YACC
if test "$YACC" != "bison -y"; then
	AC_MSG_ERROR([bison not found])
fi

AC_ARG_WITH(
	[python],
	[AS_HELP_STRING([--without-python],[compile without python support])],
	[case $withval in 
		yes)
			REQUIRE_PYTHON=1
			PYTHON_NAME=python3
		;;
		no)
			REQUIRE_PYTHON=
			PYTHON_NAME=
		;;
		*)
			REQUIRE_PYTHON=1
			PYTHON_NAME=$withval
		;;
	esac],
	[REQUIRE_PYTHON=1; PYTHON_NAME=python3])
if test $REQUIRE_PYTHON; then
	AC_CHECK_PROGS([PYTHON],$PYTHON_NAME)
	if test $REQUIRE_PYTHON -a ! $PYTHON; then
		AC_MSG_ERROR([$PYTHON_NAME not found])
	fi
fi
AC_SUBST(PYTHON)
if test $PYTHON; then
	PYTHON_VERSION=[`$PYTHON -c 'import sys; print(sys.version[:3])'`]
	AC_SUBST(PYTHON_VERSION)
	AC_DEFINE([HAVE_PYTHON],1,[Define to 1 if python support is enabled])
fi

AC_CHECK_LIB([pthread], [pthread_create],,
	AC_MSG_ERROR([pthread library not found]))
AC_CHECK_LIB([bluetooth], [hci_devid],,
	AC_MSG_ERROR([bluetooth library not found]))
AC_CHECK_LIB([dl], [dlopen],,
	AC_MSG_ERROR([dl lib not found]))
#AC_CHECK_LIB([rt], [clock_gettime],,
#	AC_MSG_ERROR([rt lib not found]))

AC_HEADER_STDC
AC_CHECK_HEADER([stdint.h],,
	AC_MSG_ERROR([stdint.h not found]))
AC_CHECK_HEADER([bluetooth/bluetooth.h],,
	AC_MSG_ERROR([bluetooth/bluetooth.h not found]))
AC_CHECK_HEADERS([bluetooth/l2cap.h bluetooth/hci.h],,
	AC_MSG_ERROR([bluetooth headers not found]),
	[#include <bluetooth/bluetooth.h>])
AC_CHECK_HEADER([linux/input.h],,
	AC_MSG_ERROR([linux/input.h not found]))
AC_CHECK_HEADER([linux/uinput.h],,
	AC_MSG_ERROR([linux/uinput.h]),
	[#include <linux/input.h>])

AC_ISC_POSIX

AC_ARG_WITH(ldconfig,AC_HELP_STRING([--disable-ldconfig],
	[don't execute ldconfig after install]))
if test "$enable_ldconfig" = "no"; then
	LDCONFIG="#ldconfig"
else
	LDCONFIG="ldconfig"
fi
AC_SUBST(LDCONFIG)

AC_OUTPUT(
	[Makefile]
	[defs.mak]
	[common/include/lib.mak]
	[libcwiid/Makefile]
	[libcwiid/cwiid.pc]
	[python/Makefile]
	)

