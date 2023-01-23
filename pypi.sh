rm -fr dist/*
py -m build --sdist --wheel --outdir dist/
py -m twine upload dist/* --verbose