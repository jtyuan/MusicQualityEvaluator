from .utils import *

eps = 1e-5


def x_cell(score, cell_size=4):
    notes = flat_notes(score)
    n_n = len(notes)

    if n_n == 0:
        return 0

    count = 0
    for i in range(0, n_n, cell_size):
        for j in range(0, cell_size - 1):
            #             print(notes[i+j].pitch, notes[i+j+1].pitch, notes[i + j].pitch.ps - notes[i + j + 1].pitch.ps)
            if abs(abs(get_pitch(notes[i + j]).ps - get_pitch(notes[i + j + 1]).ps) - 1) > eps:
                break
        else:
            count += 1
    return count / float(n_n / cell_size)


def y_cell(score, cell_size=4):
    notes = flat_notes(score)
    n_n = len(notes)

    if n_n == 0:
        return 0

    count = 0
    for i in range(0, n_n, cell_size):
        for j in range(0, cell_size - 1):
            if abs(abs(get_pitch(notes[i + j]).ps - get_pitch(notes[i + j + 1]).ps) - 2) > eps:
                break
        else:
            count += 1
    return count / float(n_n / cell_size)


def z_cell(score, cell_size=4):
    notes = flat_notes(score)
    n_n = len(notes)

    if n_n == 0:
        return 0

    count = 0
    for i in range(0, n_n, cell_size):
        if (abs(abs(get_pitch(notes[i]).ps - get_pitch(notes[i + 1]).ps) - 2) < eps
            and abs(abs(get_pitch(notes[i + 1]).ps - get_pitch(notes[i + 2]).ps) - 4) < eps
                and abs(abs(get_pitch(notes[i + 2]).ps - get_pitch(notes[i + 3]).ps) - 2) < eps):
            count += 1
    return count / float(n_n / cell_size)
