import musicalbeeps
import Note
class Melody:
    """Attributes:title author and notes
    """
    def __init__(self,filename):
        """(str)->nothing
        takes a filename finds the author of the song and the title, stores it in the object then stores all the notes in it aswell
        >>> mel=Melody('tetris.txt')
        >>> mel.notes[1]
        '0.25 B 4 natural'
        >>> mel=Melody('tetris.txt')
        >>> mel.author
        'Nikolay Nekrasov, Hirokazu Tanaka'
        >>> mel=Melody('tetris.txt')
        >>> mel.title
        'Tetris'
        """
        newnote=""
        file=open(filename,'r')
        content=file.read()
        file.close()
        char=""
        length=len(content)
        count=0
        title_list=[]
        author_list=[]
        notes_list=[]
        
        while char != '\n':
            char=content[count]
            title_list.append(char)
            count+=1
        
        title="".join(title_list)
        self.title=title[:-1]
        char=""
        
        while char != '\n':
            char=content[count]
            author_list.append(char)
            count+=1
            
        author="".join(author_list)
        self.author=author[:-1]
        char=""
        
        current_note=[]
        note_list=[]
        for line in content:
            while char != '\n':
                if count < len(content):
                    char=content[count]
                    current_note.append(char)
                    count+=1
                else:break
            if count < length:
                char=""
                note1="".join(current_note)
                note_list.append(note1[:-1])
                current_note=[]
            if count == length:
                note1="".join(current_note)
                note_list.append(note1[:-1])
                break
            
        check_end=0
        index=0
        count=1
        repeat_notes=[]
        final_repeat=-1
        for i in range(len(note_list)):
            note_list[i]=note_list[i].replace('NATURAL','natural')
            note_list[i]=note_list[i].replace('SHARP','sharp')
            note_list[i]=note_list[i].replace('FLAT','flat')
            temp=note_list[i].split()
            duration=float(temp[0])
            pitch=str(temp[1])
            octave=int(temp[2])
            accidental=str(temp[3])
            if temp[4] == 'true' and check_end == 0:
                check_end+=1
                repeat_notes.append(i)
                index=i+1
                repeat_components=note_list[index].split()
       
                if repeat_components[4] == 'true':
                    repeat_notes.append(index)
                    
                while repeat_components[4] != 'true':
                    count+=1
                    repeat_components=note_list[index].split()
                
                    repeat_notes.append(index)
                    index+=1
                index=i
                count=1
                final_repeat=repeat_notes[-1]
                
                for indices in repeat_notes:
                    repeat_components=note_list[indices].split()
                    durationr=float(repeat_components[0])
                    pitchr=str(repeat_components[1])
                    octaver=int(repeat_components[2])
                    accidentalr=str(repeat_components[3].lower())
                    newnote=Note.Note(durationr,pitchr,octaver,accidentalr)
                    notes_list.append(newnote)
                
            if i == final_repeat:
                final_repeat=-1
                check_end=0
                repeat_notes=[]
                
            
            index=index-count
            newnote = Note.Note(duration,pitch,octave,accidental)
            notes_list.append(newnote)
            
        self.notes=notes_list
        
    def play(self,obj):
        """(obj)->nothing
        takes a player object and plays the notes in the current melody
        """
        for notes in self.notes:
            note_components=str(notes).split()
            playable=Note.Note(float(note_components[0]),note_components[1],int(note_components[2]),note_components[3])
            playable.play(obj)
          
        
            
            
    def get_total_duration(self):
        """(self)->float
        counts the total duration of the melody and returns the value
        >>> mel=Melody('tetris.txt')
        >>> mel.get_total_duration
        21.25
        >>> mel=Melody('weasel.txt')
        >>> mel.get_total_duration()
        9.8
        >>> mel=Melody('twinkle.txt')
        >>> mel.get_total_duration()
        27.0
        """
        vals=[]
        for i in range(len(self.notes)):
    
            vals.append(self.notes[i].duration)
        return sum(vals)
                
                
            
    
    def lower_octave(self):
        """(self)->bool
        reduces all octaves by 1 if it is not possible returns false if it is returns true
        >>> mel=Melody('twinkle.txt')
        >>> mel.lower_octave()
        True
        >>> mel.lower_octave()
        True
        >>> mel.lower_octave()
        True
        >>> mel.lower_octave()
        False
        >>> mel=Melody('tetris.txt')
        >>> mel.lower_octave()
        True
        """
        new_melody=[]
        for i in range(len(self.notes)):
            current_note=self.notes[i]
            current_note.octave=current_note.octave-1
            if current_note.octave < 1:
                return False
            else:
                new_melody.append(current_note)
        self.notes=new_melody
        return True
    
    def upper_octave(self):
        """(self)->bool
        takes a melody object and increases the octave of every note by one, if it increases past 7 it returns false, otherwise it returns True
        >>> mel=Melody('tetris.txt')
        >>> mel.upper_octave()
        True
        >>> mel.notes
        ['0.25 E 6 natural', '0.25 B 5 natural', '0.25 C 6 natural', '0.5 D 6 natural', '0.25 C 6 natural', '0.25 B 5 natural', '0.5 A 5 natural', '0.25 A 5 natural', '0.25 C 6 natural', '0.5 E 6 natural', '0.25 D 6 natural', '0.25 C 6 natural', '0.75 B 5 natural', '0.25 C 6 natural', '0.5 D 6 natural', '0.5 E 6 natural', '0.5 C 6 natural', '0.5 A 5 natural', '0.25 A 5 natural', '0.25 A 5 natural', '0.25 B 5 natural', '0.25 C 6 natural', '0.75 D 6 natural', '0.25 F 6 natural', '0.5 A 6 natural', '0.25 G 6 natural', '0.25 F 6 natural', '0.75 E 6 natural', '0.25 C 6 natural', '0.5 E 6 natural', '0.25 D 6 natural', '0.25 C 6 natural', '0.5 B 5 natural', '0.25 B 5 natural', '0.25 C 6 natural', '0.5 D 6 natural', '0.5 E 6 natural', '0.5 C 6 natural', '0.5 A 5 natural', '0.5 A 5 natural']
        >>> mel=Melody('twinkle.txt')
        >>> mel.upper_octave()
        True
        >>> mel.upper_octave()
        True
        >>> mel.upper_octave()
        True
        >>> mel.upper_octave()
        False
        """
        new_melody=[]
        for i in range(len(self.notes)):
            current_note=self.notes[i]
            current_note.octave=current_note.octave+1
            if current_note.octave > 7:
                return False
            else:
                new_melody.append(current_note)
        self.notes=new_melody
        return True
        
        
    def change_tempo(self,tempo):
        """(float)->nothing
        takes a float and multiplies the duration of each note in the melody by that float
        >>> mel=Melody('hotcrossbuns.txt')
        >>> mel.change_tempo(3)
        >>> mel.notes
        ['1.5 B 4 natural', '1.5 A 4 natural', '3.0 G 4 natural', '0.75 G 4 natural', '0.75 G 4 natural', '0.75 A 4 natural', '0.75 A 4 natural', '1.5 B 4 natural', '1.5 A 4 natural', '3.0 G 4 natural']
        >>> mel=Melody('tetris.txt')
        >>> mel.change_tempo(5)
        >>> mel.notes[1]
        '1.25 B 4 natural'
        >>> mel=Melody('twinkle.txt')
        >>> mel.change_tempo(.2)
        >>> mel.notes[1]
        '0.1 C 4 natural'
        """
        new_melody=[]
        for i in range(len(self.notes)):
            current_note=self.notes[i]               
            current_note.duration=float(current_note.duration)*tempo
            new_melody.append(current_note)
        self.notes=new_melody