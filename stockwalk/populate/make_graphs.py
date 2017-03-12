from subprocess import call
# call(["ls", "-l"])
from os.path import abspath, dirname, join

data_dir = abspath(join(dirname(__file__), '..', '..',))
rfile = join(data_dir, 'rfbp.R')
print(rfile)
