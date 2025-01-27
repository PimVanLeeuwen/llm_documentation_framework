#### getCurrentlyPlayingNote()


 MPENote MPESynthesiserVoice::getCurrentlyPlayingNote ( ) const noexcept 
 

Returns the MPENote that this voice is currently playing.Returns an invalid MPENote if no note is playing (you can check this using MPENote::isValid() or MPEVoice::isActive()).