from __future__ import print_function, division
import sys
sys.path.append('../code/')

import thinkdsp
import thinkplot

from numpy import *

cos_sig = thinkdsp.CosSignal(freq=440, amp=1.0, offset=0)
sin_sig = thinkdsp.CosSignal(freq=880, amp=0.5, offset=0)

cos_sig.plot()
thinkplot.config(title="Cos Wave")
thinkplot.config(xlabel="Time (s)")
thinkplot.show()

sin_sig.plot()
thinkplot.config(title="Sin Wave")
thinkplot.config(xlabel="Time (s)")
thinkplot.show()

mix = sin_sig + cos_sig

wave = mix.make_wave(duration=0.5, start=0, framerate=11025)
wave.plot()
thinkplot.config(title="Combo Wave")
thinkplot.show()

