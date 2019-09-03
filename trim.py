import numpy as np
from pydub import AudioSegment


def trim(start,end,file_name,format_,i):
    t1 = start
    t2 = end
    t1 = t1 * 1000 #Works in milliseconds
    t2 = t2 * 1000
    newAudio = AudioSegment.from_wav(file_name + "." +format_)
    newAudio = newAudio[t1:t2]
    newAudio.export(file_name+ "_" + str(i) + '.wav', format=format_) #Exports to a wav file in the current path.

if __name__ == '__main__':

	with open("time_stamps.txt", "rb") as file:
	    contents = list(map(float,file.read().decode("utf-8").split(',')))

	file_name = "male"
	format_ = "wav"
	for i in range(len(contents)):
		try :trim(contents[i],contents[i+1],file_name,format_,i)
		except : pass