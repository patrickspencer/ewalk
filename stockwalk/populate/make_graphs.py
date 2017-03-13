from subprocess import call
from stockwalk.models import dbsession, Company
from os.path import abspath, dirname, join, expanduser, isfile

# lib_dir is where rfbp.R is located
lib_dir = abspath(join(dirname(__file__), '..', '..', 'lib'))
rfbp_loc = join(lib_dir, 'rfbp.R')

attribute = "close"

graph_dir = join(expanduser("~"), "stockwalk_graphs")

symbols = dbsession.query(Company.symbol).all()
for s in symbols:
    symbol = s[0]
    file_name = symbol + "_" + attribute + ".png"
    file_full = join(graph_dir, file_name)
    if not isfile(file_full):
        call(["Rscript", rfbp_loc, symbol, attribute])
