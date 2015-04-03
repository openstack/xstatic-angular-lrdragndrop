
"""
XStatic resource package

See package 'XStatic' for documentation and basic tools.
"""

# official name, upper/lowercase allowed, no spaces
DISPLAY_NAME = 'Angular-lrdragndrop'

# name used for PyPi
PACKAGE_NAME = 'XStatic-%s' % DISPLAY_NAME

NAME = __name__.split('.')[-1] # package name (e.g. 'foo' or 'foo_bar')
                               # please use a all-lowercase valid python
                               # package name

VERSION = '1.0.2' # version of the packaged files, please use the upstream
                  # version number
BUILD = '2' # our package build number, so we can release new builds
             # with fixes for xstatic stuff.
PACKAGE_VERSION = VERSION + '.' + BUILD # version used for PyPi

DESCRIPTION = "%s %s (XStatic packaging standard)" % (DISPLAY_NAME, VERSION)

PLATFORMS = 'any'
CLASSIFIERS = []
KEYWORDS = 'drag-n-drop angular table lrdragndrop xstatic'

# XStatic-* package maintainer:
MAINTAINER = 'Thai Tran'
MAINTAINER_EMAIL = 'tqtran@us.ibm.com'

# this refers to the project homepage of the stuff we packaged:
HOMEPAGE = 'https://github.com/lorenzofox3/lrDragNDrop'

# this refers to all files:
LICENSE = '(same as %s)' % DISPLAY_NAME

from os.path import join, dirname
BASE_DIR = join(dirname(__file__), 'data')
# linux package maintainers just can point to their file locations like this:
#BASE_DIR = '/usr/share/javascript/' + NAME

# location of the Javascript file that's the entry point for this package, if
# one exists, relative to BASE_DIR
MAIN='lrdragndrop.js'

LOCATIONS = {
    # CDN locations (if no public CDN exists, use an empty dict)
    # if value is a string, it is a base location, just append relative
    # path/filename. if value is a dict, do another lookup using the
    # relative path/filename you want.
    # your relative path/filenames should usually be without version
    # information, because either the base dir/url is exactly for this
    # version or the mapping will care for accessing this version.
}
