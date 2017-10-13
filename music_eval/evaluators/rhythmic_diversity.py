from .utils import *


def rhythmic_signature(notes):
    result = ''
    for n in notes:
        result += str(int(n.duration.quarterLength * 10000)) + '-'
    return result[:-1]


def rhythmic_diversity(score):
    unique_measure = set()
    try:
        expanded = score.parts[0].expandRepeats()
    except:
        expanded = score.parts[0]

    for ts in expanded[0]:
        if isinstance(ts, meter.TimeSignature):
            break

    barQuarterLength = ts.numerator * ts.beatLengthToQuarterLengthRatio
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
                    signature = rhythmic_signature(get_notes(m.notes) + [expanded[i + 1].notes[0]])
                    unique_measure.add(signature)
                    continue
                else:
                    merged = False
            else:
                signature = rhythmic_signature(m.notes)
                unique_measure.add(signature)
                #     print(unique_measure)
    return len(unique_measure) / len(expanded)
