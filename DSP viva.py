#!/usr/bin/env python
# coding: utf-8

# # answer of ques 1
# 

# In[163]:



import thinkdsp as t
import thinkplot as d
from IPython.display import Audio
sig1=t.SinSignal(freq=22,amp=5,offset=0)
sig2=t.SinSignal(freq=10,amp=5,offset=0)
sig3=t.SinSignal(freq=2,amp=5,offset=0)
sig=sig1+sig2+sig3
wave=sig.make_wave(duration=1,start=0,framerate=42000)
spec=wave.make_spectrum()
spec.plot()


# # answer of ques 5

# In[164]:


import thinkdsp as t
a=t.SinSignal(freq=264, amp=5, offset=0)             ########## mobile vibration sound
a_wave=sa.make_wave(duration=1.5, start=0, framerate=42000)


c=a_wave
#c.plot()
from IPython.display import Audio
audio=Audio(data=c.ys, rate=c.framerate)
audio


# # answer of ques 4

# In[165]:


import thinkdsp as t
import thinkplot as d
wave=t.read_wave("Downloads/My.wav")
wave.plot()
seg=wave.segment(start=0,duration=25)
aud=seg.make_audio()
spec=seg.make_spectrum()
spec.plot(high=1000)
aud

