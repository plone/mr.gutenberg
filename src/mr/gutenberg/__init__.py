from sphinxext import InfoTableDirective


def setup(app):
    app.add_directive('docbase_pkginfo', InfoTableDirective)
