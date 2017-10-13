from music21 import *


def flat_notes(score):
    notes = []
    try:
        expanded = score.parts[0].expandRepeats()
    except:
        expanded = score.parts[0]
    for m in expanded:
        if isinstance(m, (stream.Measure, stream.Voice)):
            for n in m.notes:
                notes.append(n)
    return notes


def get_pitch(note):
    if isinstance(note, chord.Chord):
        return note.pitches[0]
    else:
        return note.pitch


def get_notes(measure):
    notes = []
    for n in measure.notes:
        notes.append(n)
    return notes
