# https://python-sounddevice.readthedocs.io/en/0.3.15/api/checking-hardware.html
import sounddevice as sd
print(sd.query_devices())