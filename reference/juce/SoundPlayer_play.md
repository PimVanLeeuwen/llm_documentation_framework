#### play() [5/5]


 void SoundPlayer::play ( AudioBuffer< float > \* buffer, 
 
 bool deleteWhenFinished = false, 
 bool playOnAllOutputChannels = false ) 

Plays the sound from an audio sample buffer.This will output the sound contained in an audio sample buffer. If deleteWhenFinished is true then the audio sample buffer will be automatically deleted once the sound has finished playing.If playOnAllOutputChannels is true, then if there are more output channels than buffer channels, then the ones that are available will be reused on multiple outputs so that something is sent to all output channels. If it is false, then the buffer will just be played on the first output channels.