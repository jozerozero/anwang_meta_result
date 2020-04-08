import shutil
import os
from glob import glob 

gta_path = '../tacotron_output'
# for line in open('../worst_sample')
for audio_path in glob(os.path.join('../worse_sample', '*.wav')):
	audio_name = os.path.basename(audio_path)
	shutil.copyfile(os.path.join(gta_path, audio_name+".wav"), audio_name)

