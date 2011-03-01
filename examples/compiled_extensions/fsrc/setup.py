from numpy.distutils.core import setup, Extension
import platform
import sys
import os


conf = {
    'fortran_lib' : None,
    'fortran_library_dir' : None
    }

if (os.environ.has_key('DFLAGS') == True):
    if (os.environ['DFLAGS'] == ''):
        import distutils.sysconfig
        old_str = distutils.sysconfig._config_vars['CFLAGS']
        distutils.sysconfig._config_vars['CFLAGS'] = old_str.replace('-g','')
        old_str = distutils.sysconfig._config_vars['OPT']
        distutils.sysconfig._config_vars['OPT'] = old_str.replace('-g','')

if (os.environ.has_key('OCFLAGS') == True):
    oflag = os.environ['OCFLAGS']
    import distutils.sysconfig
    old_str = distutils.sysconfig._config_vars['CFLAGS']
    distutils.sysconfig._config_vars['CFLAGS'] = old_str.replace('-O ','').replace('-O0','').replace('-O1','').replace('-O2','').replace('-O3','').replace('-O4','').replace('-O5','') + ' ' + oflag
    old_str = distutils.sysconfig._config_vars['OPT']
    distutils.sysconfig._config_vars['OPT'] = old_str.replace('-O ','').replace('-O0','').replace('-O1','').replace('-O2','').replace('-O3','').replace('-O4','').replace('-O5','') + ' ' + oflag


needf90 = False
if platform.system() == 'Darwin':
    needf90 = True 
    from numpy.distutils.fcompiler.gnu import GnuFCompiler
    GnuFCompiler.old_get_libraries = GnuFCompiler.get_libraries
    GnuFCompiler.old_get_library_dirs = GnuFCompiler.get_library_dirs

    # Have also found that on OS X, keeping cc_dynamic on the
    # link line prevents linkage--fortunately it appears that
    # none of our code requires cc_dynamic anyway.
    def get_libraries_gnuf(self):
        from numpy.distutils.fcompiler.gnu import Gnu95FCompiler
        libs = self.old_get_libraries()
        if ('cc_dynamic' in libs and
            isinstance(self, Gnu95FCompiler) == False):
            libs.remove('cc_dynamic')
        return libs

    def get_libraries_g95(self):
        libs = self.old_get_libraries()
        new_libs = ['SystemStubs']
        if (conf['fortran_lib'] != None):
            new_libs = [conf['fortran_lib'], 'SystemStubs']
        for l in new_libs:
            if l not in libs:
                libs.append(l)
        return libs

    # Need to add path to library for g2c, even though
    # g2c itself *is* already in list of libraries
    def get_library_dirs(self):
        dirs = self.old_get_library_dirs()
        if (conf['fortran_library_dir'] != None and
            conf['fortran_library_dir'] != './'):
            if conf['fortran_library_dir'] not in dirs:
                dirs.append(conf['fortran_library_dir'])
        else:
            # Try a likely path if fortran_library_dir points nowhere
            if '/sw/lib' not in dirs:
                dirs.append('/sw/lib')
        return dirs

    GnuFCompiler.get_libraries = get_libraries_gnuf
    GnuFCompiler.get_library_dirs = get_library_dirs

#    # Block gfortran from adding superfluous -arch flags
#    def _universal_flags(self, cmd):
#        # These need to come from CCEXTRA_ARGS, without setting
#        # LDFLAGS
#        return ['-arch', 'i386', '-arch', 'x86_64']

    from numpy.distutils.fcompiler.gnu import Gnu95FCompiler
#    Gnu95FCompiler._universal_flags = _universal_flags


    # If on the Intel Mac, must use g95 to compile Fortran
    # Use gcc as linker, because g95 just isn't helping us make
    # bundles on OS X
    from numpy.distutils.fcompiler.g95 import G95FCompiler
    G95FCompiler.old_get_library_dirs = G95FCompiler.get_library_dirs
    G95FCompiler.old_get_libraries = G95FCompiler.get_libraries
    G95FCompiler.get_library_dirs = get_library_dirs
    G95FCompiler.get_libraries = get_libraries_g95
    G95FCompiler.executables['linker_so'] = ["gcc","-undefined dynamic_lookup -bundle"]

extension_modules = [
    Extension('_model',
              ['beta.f',
               'gauss.f'])
    ]

setup(name='_model',
      ext_modules=extension_modules)
