import musicalbeeps
class Note:
    """Note class that describes a note with attributes: duration,pitch,octave,accidental
    """
    octave_min=1
    octave_max=7
    
    def __init__(self,duration,pitch,octave=1,accidental='natural'):
        '''(self,float,str,int,str)->nothing
        takes a duration, a pitch, an octave and an accidental and constructs a Note class object with those attributes
        >>> note = Note(2.0, "B", 1, "natural")
        >>> note.octave
        1
        >>> note = Note(2.0, "B", 4, "natural")
        >>> note.pitch
        'B'
        >>> note = Note(3.0, "G")
        >>> note.accidental
        'natural'
        '''
        accidentals=['sharp','flat','natural']
        pitches = ['A','B','C','D','E','F','G','R']
        
        
        if type(duration) is not float or type(pitch) is not str or type(octave) is not int or type(accidental) is not str:
            raise AssertionError("Invalid argument types")
        
        if duration < 0:
            raise AssertionError("Invalid Duration")
        
        if len(pitch) != 1:
            raise AssertionError("Invalid Pitch")
        
        if self.octave_min > octave or octave > self.octave_max:
            raise AssertionError("Invalid Octave")
        
        if accidental not in accidentals:
            raise AssertionError("Invalid Accidental value")
        
        if pitch not in pitches:
            raise AssertionError("Invalid Pitch")
        
        self.duration = float(duration)
        self.pitch = str(pitch)
        self.octave = int(octave)
        self.accidental = str(accidental)
        
    def __str__(self):
        """(self)->(str)
        takes self as input and returns a string with all the attributes of the given object
        >>> note = Note(2.0, "B", 4, "natural")
        >>> print(note)
        2.0 B 4 natural
        >>> note = Note(3.0, "G")
        >>> print(note)
        3.0 G 1 natural
        >>> note = Note(2.0, "B", 1, "natural")
        >>> print(note)
        2.0 B 1 natural
        """
        return str(self.duration)+" "+self.pitch+" "+str(self.octave)+" "+self.accidental
    
    def play(self,player):
        """(object)->nothing
        takes an object and passes it through the given player to make a sound
        """
        
        obj = musicalbeeps.Player()
        note=self.pitch+str(self.octave)
        if self.pitch == 'R':
            player.play_note('pause')
       
        elif self.accidental == 'sharp':
            player.play_note(note,self.duration,'#')
        
        elif self.accidental == 'flat':
            player.play_note(note,self.duration,'b')
            
        else:
            player.play_note(note,self.duration)
            
        
        
        
import musicalbeeps
class Note:
    """Note class that describes a note with attributes: duration,pitch,octave,accidental
    """
    octave_min=1
    octave_max=7
    
    def __init__(self,duration,pitch,octave=1,accidental='natural'):
        '''(self,float,str,int,str)->nothing
        takes a duration, a pitch, an octave and an accidental and constructs a Note class object with those attributes
        >>> note = Note(2.0, "B", 1, "natural")
        >>> note.octave
        1
        >>> note = Note(2.0, "B", 4, "natural")
        >>> note.pitch
        'B'
        >>> note = Note(3.0, "G")
        >>> note.accidental
        'natural'
        '''
        accidentals=['sharp','flat','natural']
        pitches = ['A','B','C','D','E','F','G','R']
        
        
        if type(duration) is not float or type(pitch) is not str or type(octave) is not int or type(accidental) is not str:
            raise AssertionError("Invalid argument types")
        
        if duration < 0:
            raise AssertionError("Invalid Duration")
        
        if len(pitch) != 1:
            raise AssertionError("Invalid Pitch")
        
        if self.octave_min > octave or octave > self.octave_max:
            raise AssertionError("Invalid Octave")
        
        if accidental not in accidentals:
            raise AssertionError("Invalid Accidental value")
        
        if pitch not in pitches:
            raise AssertionError("Invalid Pitch")
        
        self.duration = float(duration)
        self.pitch = str(pitch)
        self.octave = int(octave)
        self.accidental = str(accidental)
        
    def __str__(self):
        """(self)->(str)
        takes self as input and returns a string with all the attributes of the given object
        >>> note = Note(2.0, "B", 4, "natural")
        >>> print(note)
        2.0 B 4 natural
        >>> note = Note(3.0, "G")
        >>> print(note)
        3.0 G 1 natural
        >>> note = Note(2.0, "B", 1, "natural")
        >>> print(note)
        2.0 B 1 natural
        """
        return str(self.duration)+" "+self.pitch+" "+str(self.octave)+" "+self.accidental
    
    def play(self,player):
        """(object)->nothing
        takes an object and passes it through the given player to make a sound
        """
        
        obj = musicalbeeps.Player()
        note=self.pitch+str(self.octave)
        if self.pitch == 'R':
            player.play_note('pause')
       
        elif self.accidental == 'sharp':
            player.play_note(note,self.duration,'#')
        
        elif self.accidental == 'flat':
            player.play_note(note,self.duration,'b')
            
        else:
            player.play_note(note,self.duration)