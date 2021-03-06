from distutils.core import *
from subprocess import *

package_name = 'kyotocabinet'
package_version = '1.6'
package_description = 'a straightforward implementation of DBM'
package_author = 'FAL Labs'
package_author_email = 'info@fallabs.com'
package_url = 'http://fallabs.com/kyotocabinet/'
module_name = 'kyotocabinet'


def getcmdout(cmdargs):
    try:
        pipe = Popen(cmdargs, stdout=PIPE)
        output = pipe.communicate()[0].decode('utf-8')
    except:
        output = ""
    return output.strip()

include_dirs = []
myincopts = getcmdout(['kcutilmgr', 'conf', '-i']).split()
for incopt in myincopts:
    if incopt.startswith('-I'):
        incdir = incopt[2:]
        include_dirs.append(incdir)
if len(include_dirs) < 1:
    include_dirs = ['/usr/local/include']

extra_compile_args = []
if sys.version_info[0] == 2:
    sources = ['kyotocabinet2.cc']
else:
    sources = ['kyotocabinet3.cc']

library_dirs = []
libraries = []
mylibopts = getcmdout(['kcutilmgr', 'conf', '-l']).split()
for libopt in mylibopts:
    if libopt.startswith('-L'):
        libdir = libopt[2:]
        library_dirs.append(libdir)
    elif libopt.startswith('-l'):
        libname = libopt[2:]
        libraries.append(libname)
if len(library_dirs) < 1:
    library_dirs = ['/usr/local/lib']
if len(libraries) < 1:
    if (os.uname()[0] == "Darwin"):
        libraries = ['kyotocabinet', 'z', 'stdc++', 'pthread', 'm', 'c']
    else:
        libraries = ['kyotocabinet', 'z', 'stdc++', 'rt', 'pthread', 'm', 'c']

module = Extension(module_name,
                   include_dirs=include_dirs,
                   extra_compile_args=extra_compile_args,
                   sources=sources,
                   library_dirs=library_dirs,
                   libraries=libraries)

setup(name=package_name,
      version=package_version,
      description=package_description,
      author=package_author,
      author_email=package_author_email,
      url=package_url,
      ext_modules=[module])
