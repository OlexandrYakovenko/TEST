import os
text = "Привіт! Це RHVoice."
os.system(f'echo "{text}" | festival --tts')
