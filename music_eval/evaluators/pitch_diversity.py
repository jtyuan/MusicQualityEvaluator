from .utils import *


def pitch_signature(notes):
    result = ''
    for i in range(1, len(notes)):
        p0 = get_pitch(notes[i - 1]).ps
        p1 = get_pitch(notes[i]).ps
        diff = p1 - p0
        if diff > 0:
            result += str(int(diff)) + 'u'
        elif diff < 0:
            result += str(int(-diff)) + 'd'
        else:
            result += '0'
    return result


def pitch_diversity(score):
    unique_measure = set()
    try:
        expanded = score.parts[0].expandRepeats()
    except:
        expanded = score.parts[0]

    try:
        for ts in expanded[0]:
            if isinstance(ts, meter.TimeSignature):
                barQuarterLength = ts.numerator * ts.beatLengthToQuarterLengthRatio
                break
        else:
            barQuarterLength = 4.0
    except:
        barQuarterLength = 4.0

    merged = False
    for i, m in enumerate(expanded):
        if isinstance(m, (stream.Measure, stream.Voice)):
            if m.duration.quarterLength != barQuarterLength:
                if (not merged
                    and i + 1 < len(expanded)
                    and isinstance(expanded[i + 1], (stream.Measure, stream.Voice))
                    and len(expanded[i + 1].notes) > 0
                        and (m.duration.quarterLength + expanded[i + 1].duration.quarterLength) == barQuarterLength):
                    merged = True
                    signature = pitch_signature(get_notes(m.notes) + [expanded[i + 1].notes[0]])
                    unique_measure.add(signature)
                    continue
                else:
                    merged = False
            else:
                signature = pitch_signature(m.notes)
                unique_measure.add(signature)

    return len(unique_measure) / float(len(expanded))
