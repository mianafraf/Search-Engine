from generate import generate
import time

start = time.time()
v = generate()
v.loadfindex()
v.loadinvindex()
v.sortfullinvindex()
v.saveinvindex()
print(time.time() - start)