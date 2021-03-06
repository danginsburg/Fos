import numpy as np
import nibabel as nib

from fos import World, Window, WindowManager
from fos.actor.curve import InteractiveCurves

# bug:
# check ordering of window. get_world not working
#w = wi.get_world()

# file
fname = '/home/stephan/Downloads/Tracks/fibers.trk'
streams,hdr = nib.trackvis.read(fname)

T=[s[0] for s in streams]
Trk=np.array(T, dtype=np.object)
print "loaded file"

cu = InteractiveCurves(curves = T)

w=World()
w.add(cu)

wi = Window(caption="Multi-Modal 1")
wi.attach(w)

wm = WindowManager()
wm.add(wi)
wm.run()