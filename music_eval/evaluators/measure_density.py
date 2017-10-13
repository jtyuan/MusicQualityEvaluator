from .utils import *


def measure_density(score, max_note_num=16):
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
    count = 0
    for i, m in enumerate(expanded):
        if isinstance(m, (stream.Measure, stream.Voice)):
            if m.duration.quarterLength != barQuarterLength:
                if (not merged
                    and i + 1 < len(expanded)
                    and isinstance(expanded[i + 1], (stream.Measure, stream.Voice))
                    and len(expanded[i + 1].notes) > 0
                        and (m.duration.quarterLength + expanded[i + 1].duration.quarterLength) == barQuarterLength):
                    merged = True
                    count += len(m.notes) + 1
                    continue
                else:
                    merged = False
            else:
                count += len(m.notes)

    return count / (len(expanded) * max_note_num)
