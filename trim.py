from pydub import AudioSegment
t1 = 6
t2 = 11
t1 = t1 * 1000 #Works in milliseconds
t2 = t2 * 1000
newAudio = AudioSegment.from_wav("male.wav")
newAudio = newAudio[t1:t2]
newAudio.export('male_'+str(3)+'.wav', format="wav") #Exports to a wav file in the current path.