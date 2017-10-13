# MusicQualityEvaluator

## Installation

```bash
$ pip install . --user --upgrade
```

## Usage

```python
from music_eval import evaluate, get_score
from music21 import converter

# Evaluate all music pieces in the given input file
o = converter.parse('input_file')
evaluate(o, output='output.csv')

# Evaluate a single music21 Score object
get_score(o.getScoreByNumber(0))
```
