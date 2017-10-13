from .utils import *


# http://solomonsmusic.net/pcsets.htm
pc_sets = {
    'Unison': {0},
    'Semitone': {0, 1},
    'Whole-tone': {0, 2},
    'Minor Third': {0, 3},
    'Major Third': {0, 4},
    'Perfect Fourth': {0, 5},
    'Tritone': {0, 6},
    'BACH /Chromatic Trimirror': {0, 1, 2},
    'Phrygian Trichord': {0, 1, 3},
    'Minor Trichord': {0, 2, 3},
    'Major-minor Trichord.1': {0, 1, 4},
    'Major-minor Trichord.2': {0, 3, 4},
    'Incomplete Major-seventh Chord.1': {0, 1, 5},
    'Incomplete Major-seventh Chord.2': {0, 4, 5},
    'Rite chord.2, Tritone-fourth.1': {0, 1, 6},
    'Rite chord.1, Tritone-fourth.2': {0, 5, 6},
    'Whole-tone Trichord': {0, 2, 4},
    'Incomplete Minor-seventh Chord': {0, 2, 5},
    'Incomplete Dominant-seventh Chord.2': {0, 3, 5},
    'Incomplete Dominant-seventh Chord.1/Italian-sixth': {0, 2, 6},
    'Incomplete Half-dim-seventh Chord': {0, 4, 6},
    'Quartal Trichord': {0, 2, 7},
    'Diminished Chord': {0, 3, 6},
    'Minor Chord': {0, 3, 7},
    'Major Chord': {0, 4, 7},
    'Augmented Chord': {0, 4, 8},
    'BACH /Chromatic Tetramirror': {0, 1, 2, 3},
    'Major-second Tetracluster.2': {0, 1, 2, 4},
    'Major-second Tetracluster.1': {0, 2, 3, 4},
    'Alternating Tetramirror': {0, 1, 3, 4},
    'Minor Third Tetracluster.2': {0, 1, 2, 5},
    'Minor Third Tetracluster.1': {0, 3, 4, 5},
    'Major Third Tetracluster.2': {0, 1, 2, 6},
    'Major Third Tetracluster.1': {0, 4, 5, 6},
    'Perfect Fourth Tetramirror': {0, 1, 2, 7},
    'Arabian Tetramirror': {0, 1, 4, 5},
    'Double Fourth Tetramirror': {0, 1, 5, 6},
    'Double Tritone Tetramirror': {0, 1, 6, 7},
    'Minor Tetramirror': {0, 2, 3, 5},
    'Phrygian Tetrachord': {0, 1, 3, 5},
    'Major Tetrachord': {0, 2, 4, 5},
    'Harmonic-minor Tetrachord': {0, 2, 3, 6},
    'Major-third Diminished Tetrachord': {0, 3, 4, 6},
    'Minor-second Diminished Tetrachord': {0, 1, 3, 6},
    'Perfect-fourth Diminished Tetrachord': {0, 3, 5, 6},
    'Major-second Minor Tetrachord': {0, 2, 3, 7},
    'Perfect-fourth Major Tetrachord': {0, 4, 5, 7},
    'All-interval Tetrachord.1': {0, 1, 4, 6},
    'All-interval Tetrachord.2': {0, 2, 5, 6},
    'Minor-second Quartal Tetrachord': {0, 1, 5, 7},
    'Tritone Quartal Tetrachord': {0, 2, 6, 7},
    'Major-minor Tetramirror': {0, 3, 4, 7},
    'Major-diminished Tetrachord': {0, 1, 4, 7},
    'Minor-diminished Tetrachord': {0, 3, 6, 7},
    'Minor-augmented Tetrachord': {0, 1, 4, 8},
    'Augmented-major Tetrachord': {0, 3, 4, 8},
    'Major-seventh Chord': {0, 1, 5, 8},
    'Whole-tone Tetramirror': {0, 2, 4, 6},
    'Major-second Major Tetrachord': {0, 2, 4, 7},
    'Perfect-fourth Minor Tetrachord': {0, 3, 5, 7},
    'Quartal Tetramirror': {0, 2, 5, 7},
    'Augmented Seventh Chord': {0, 2, 4, 8},
    'French-sixth Chord': {0, 2, 6, 8},
    'Minor-seventh Chord': {0, 3, 5, 8},
    'Half-diminished Seventh Chord': {0, 2, 5, 8},
    'Dominant-seventh/German-sixth Chord': {0, 3, 6, 8},
    'Diminished-seventh Chord': {0, 3, 6, 9},
    'All-interval Tetrachord.3': {0, 1, 3, 7},
    'All-interval Tetrachord.4': {0, 4, 6, 7},
    'Chromatic Pentamirror': {0, 1, 2, 3, 4},
    'Major-second Pentacluster.2': {0, 1, 2, 3, 5},
    'Major-second Pentacluster.1': {0, 2, 3, 4, 5},
    'Minor-second Major Pentachord': {0, 1, 2, 4, 5},
    'Spanish Pentacluster': {0, 1, 3, 4, 5},
    'Blues Pentacluster': {0, 1, 2, 3, 6},
    'Minor-third Pentacluster': {0, 3, 4, 5, 6},
    'Major-third Pentacluster.2': {0, 1, 2, 3, 7},
    'Major-third Pentacluster.1': {0, 4, 5, 6, 7},
    'Oriental Pentacluster.1, Raga Megharanji (13161)': {0, 1, 2, 5, 6},
    'Oriental Pentacluster.2': {0, 1, 4, 5, 6},
    'DoublePentacluster.1, Raga Nabhomani (11415)': {0, 1, 2, 6, 7},
    'Double Pentacluster.2': {0, 1, 5, 6, 7},
    'Tritone-Symmetric Pentamirror': {0, 2, 3, 4, 6},
    'Tritone-Expanding Pentachord': {0, 1, 2, 4, 6},
    'Tritone-Contracting Pentachord': {0, 2, 4, 5, 6},
    'Alternating Pentachord.1': {0, 1, 3, 4, 6},
    'Alternating Pentachord.2': {0, 2, 3, 5, 6},
    'Center-cluster Pentachord.1': {0, 2, 3, 4, 7},
    'Center-cluster Pentachord.2': {0, 3, 4, 5, 7},
    'Locrian Pentamirror': {0, 1, 3, 5, 6},
    'Augmented Pentacluster.1': {0, 1, 2, 4, 8},
    'Augmented Pentacluster.2': {0, 2, 3, 4, 8},
    'Double-seconds Triple-fourth Pentachord.1': {0, 1, 2, 5, 7},
    'Double-seconds Triple-fourth Pentachord.2': {0, 2, 5, 6, 7},
    'Assymetric Pentamirror': {0, 1, 2, 6, 8},
    'Major-minor-dim Pentachord.1': {0, 1, 3, 4, 7},
    'Major-minor-dim Pentachord.2': {0, 3, 4, 6, 7},
    'Minor-major Ninth Chord': {0, 1, 3, 4, 8},
    'Gypsy Pentachord.1': {0, 1, 4, 5, 7},
    'Gypsy Pentachord.2': {0, 2, 3, 6, 7},
    'Javanese Pentachord': {0, 1, 3, 6, 7},
    'Balinese Pentachord': {0, 1, 4, 6, 7},
    'Balinese Pelog Pentatonic (12414), Raga Bhupala, Raga Bibhas': {0, 1, 3, 7, 8},
    'Hirajoshi Pentatonic (21414), Iwato (14142), Sakura/Raga Saveri (14214)': {0, 1, 5, 7, 8},
    'Syrian Pentatonic/Major-augmented Ninth Chord, Raga Megharanji (13134)': {0, 1, 4, 5, 8},
    'Lebanese Pentachord/Augmented-minor Chord': {0, 3, 4, 7, 8},
    'Persian Pentamirror, Raga reva/Ramkali (13314)': {0, 1, 4, 7, 8},
    'Minor Pentachord': {0, 2, 3, 5, 7},
    'Major Pentachord': {0, 2, 4, 5, 7},
    'Phrygian Pentachord': {0, 1, 3, 5, 7},
    'Lydian Pentachord': {0, 2, 4, 6, 7},
    'Diminished-major Ninth Chord': {0, 2, 3, 5, 8},
    'Minor-diminished Ninth Chord': {0, 3, 5, 6, 8},
    'Diminished-augmented Ninth Chor': {0, 2, 4, 5, 8},
    'Augmented-diminished Ninth Chord': {0, 3, 4, 6, 8},
    'Major-Ninth Chord': {0, 1, 3, 5, 8},
    'Minor-Ninth Chord': {0, 3, 5, 7, 8},
    'Augmented-sixth Pentachord.1': {0, 2, 3, 6, 8},
    'Augmented-sixth Pentachord.2': {0, 2, 5, 6, 8},
    'Kumoi Pentachord.2': {0, 1, 3, 6, 8},
    'Kumoi Pentachord.1': {0, 2, 5, 7, 8},
    'Enigmatic Pentachord.1': {0, 1, 4, 6, 8},
    'Enigmatic Pentachord.2, Altered Pentatonic (14223)': {0, 2, 4, 7, 8},
    'Diminished Minor-Ninth Chord': {0, 1, 3, 6, 9},
    'Ranjaniraga/Flat-Ninth Pentachord': {0, 2, 3, 6, 9},
    'Neapolitan Pentachord.1': {0, 1, 4, 6, 9},
    'Neapolitan Pentachord.2': {0, 1, 4, 7, 9},
    'Whole-tone Pentamirror': {0, 2, 4, 6, 8},
    'Dominant-ninth/major-minor/Prometheus Pentamirror, Dominant Pentatonic (22332)': {0, 2, 4, 6, 9},
    '"Black Key" Pentatonic/Slendro/Bilahariraga/Quartal Pentamirror, Yo (23232)': {0, 2, 4, 7, 9},
    'Major-seventh Pentacluster.2': {0, 1, 2, 4, 7},
    'Minor-seventh Pentacluster.1': {0, 3, 5, 6, 7},
    'Center-cluster Pentamirror': {0, 3, 4, 5, 8},
    'Diminished Pentacluster.1': {0, 1, 2, 5, 8},
    'Diminished Pentacluster.2': {0, 3, 6, 7, 8}
}


def count_in_pc_set(notes, cs):
    count = 0
    for n in notes:
        if get_pitch(n).pitchClass in cs:
            count += 1
    return count


def pitch_class_set(score, cs='any', max_set_size=5):
    notes = flat_notes(score)
    n_n = len(notes)
    max_count = 0

    if n_n == 0:
        return 0

    if isinstance(cs, str):
        if cs == 'any':
            max_count = 0
            for name, cs in pc_sets.items():
                if len(cs) > max_set_size:
                    break
                count = count_in_pc_set(notes, cs)
                if count > max_count:
                    max_count = count
        elif cs in pc_sets:
            max_count = count_in_pc_set(notes, pc_sets[cs])
    elif isinstance(cs, list):
        max_count = count_in_pc_set(notes, cs)

    return max_count / float(n_n)
