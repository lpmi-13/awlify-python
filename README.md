# Awlify

A very basic tool that takes in a sentence of text and outputs
the same text, annotated with information about whether any of
its words are in the [Academic Word List](https://www.victoria.ac.nz/lals/resources/academicwordlist/information).

## installing
`pip install awlify`

## tests
`python test`

## command usage
```
from awlify import awlify

result = awlify('please inform me of the academic words in
this sentence')

print(result)
{'data': {'sentence': 'please inform me of the academic words in this sentence', 'awl_words': [{'index': 24, 'word': 'academic', 'meta': {'head': 'academy', 'sublist': 5}}]}}
```

## expected input / output
output format:
```
{
  'data': {
    'sentence': 'THIS IS THE ORIGINAL SENTENCE',
    'awl_words': [
      {
        'index': INDEX_OF_AWL_WORD_FOUND,
        'word': 'AWL_WORD_FOUND',
        'meta': {
          'head': 'THE_HEADWORD_FROM_THE_AWL',
          'sublist': THE_AWL_SUBLIST_OF_THE_WORD
        }
      }
    ]
  }
}
```

example input for a simple sentence (no AWL words):
```
simple_sentence = awlify('this is a sentence')
```


example output for a simple sentence (no AWL words):
```
{
  'data': {
    'sentence': 'this is a sentence',
    'awl_words': []
  }
}
```

example input for a complex sentence (a few AWL words):
```
complex_sentence = awlify('the economic recovery is ongoing and potentially problematic')
```

example output for a complex sentence (a few AWL words):
```
{
  'data': {
    'sentence': 'the economic recovery is ongoing and potentially problematic',
    'awl_words': [
      {
        'index': 4,
        'word': 'economic',
        'meta': {
          'head': 'economy',
          'sublist': 1
        }
      },
      {
        'index': 13,
        'word': 'recovery',
        'meta': {
          'head': 'recover',
          'sublist': 6
        }
      },
      {
        'index': 37,
        'word': 'potentially',
        'meta': {
          'head': 'potential',
          'sublist': 2
        }
      }
    ]
  }
}
```

## NOTES

The current implementation of the sentence tokenization uses spacy,
and so it's a bit heavier than absolutely necessary, since we're
not taking advantage of any of the more advanced characteristics
of the package.

In theory, it could probably perform 98% as well with just a simple
regex, so I might add the option to do that in the future if there
aren't any real use cases for needing the full weight of spacy.

## REFERENCES
Coxhead, Averil (2000) A New Academic Word List. TESOL Quarterly, 34(2): 213-238.
