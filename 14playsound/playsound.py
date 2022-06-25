import winsound
winsound.PlaySound('14playsound/audio.wav', winsound.SND_ASYNC)

import os
# os.system('aplay audio.wav') #linux
# os.system('afplay audio.wav') #mac

wait_for_sound = input("Press Enter to continue...")

