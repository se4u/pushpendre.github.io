import biblib.bib
import biblib.messages
import re, sys

def parse(bibfn):
  db = biblib.bib.Parser().parse(open(bibfn), log_fp=sys.stderr).get_entries()
  db = biblib.bib.resolve_crossrefs(db)
  recoverer = biblib.messages.InputErrorRecoverer()
  ret = {}
  for ent in db.values():
    with recoverer:
      ret[ent.key] = ent
  recoverer.reraise()
  return ret

def camelsplit(x):
  return re.sub('(?!^)([A-Z][a-z]+)', r' \1', x)
