# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install telephone
#
# You can edit this file again by typing:
#
#     spack edit telephone
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *

def ignore_CVS(path):
    if (str(path).find("CVS") >= 0):
        return True
    return False

class Telephone(Package):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"
    cvs = ":pserver:anonymous@cdcvs.fnal.gov:/cvs/cd_read_only%module=telephone"

    version("v5_4")
    version("v5_3")
    version("v5_2")

    depends_on("perl-libwww-perl")
    depends_on("py-ansi2html", type="build")
    depends_on("py-setuptools", type="build")

    def patch(self):
        filter_file(
            'man2html',
            'ansi2html',
            'html/Makefile',
        )


    def install(self, spec, prefix):
        make = which("make")
        make()
        install_tree(self.stage.source_path, prefix, ignore=ignore_CVS)
