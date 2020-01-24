'''
Test input/output capabilities.
'''
from thefriendlystars.imports import *
from thefriendlystars.constellations import *

directory = 'examples'
mkdir(directory)

def test_io():
    cone = Gaia('GJ1214', radius=1*u.deg)
    filename = os.path.join(directory, 'test.txt')
    cone.write_to_text(filename)
    #reread = Gaia.from_text(filename)
    #assert((reread.at_epoch(2000).ra == cone.at_epoch(2000).ra).all())

if __name__ == '__main__':
    # pull out anything that starts with `test_`
    d = locals()
    tests = [x for x in d if 'test_' in x]
    # run those functions and save their output
    outputs = {k.split('_')[-1]:d[k]()
               for k in tests}
