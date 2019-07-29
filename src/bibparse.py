import biblib.bib
import biblib.messages
import biblib.algo
from argparse import Namespace
import sys

MONTHS = 'January February March April May June July August September October November December'.split()
def simplify(ent):
  key = ent.key
  typ = ent.typ
  title = year = month = ''
  if 'title' in ent:
    title = '  ' + biblib.algo.tex_to_unicode(biblib.algo.title_case(
      ent['title'], pos=ent.field_pos['title']))
  if 'year' in ent:
    year = ent['year']
  if 'month' in ent:
    month = MONTHS[ent.month_num() - 1]
  if 'author' in ent:
    authors = [
      biblib.algo.tex_to_unicode(author.pretty(),
                     pos=ent.field_pos['author'])
      for author in ent.authors()]
    if len(authors) == 0:
      author = ''
    elif len(authors) == 1:
      author = authors[0]
    else:
      author = ', '.join(authors[:-1])
      if len(authors) > 2:
        author += ','
      if ent.authors()[-1].is_others():
        author += ' et al.'
      else:
        author += ' and ' + authors[-1]
  return Namespace(key=key, title=title, author=author, year=year, month=month)

def parse(bibfn):
  db = biblib.bib.Parser().parse(open(bibfn), log_fp=sys.stderr).get_entries()
  db = biblib.bib.resolve_crossrefs(db)
  recoverer = biblib.messages.InputErrorRecoverer()
  ret = {}
  for ent in db.values():
    with recoverer:
      ent = simplify(ent)
      ret[ent.key] = ent
  recoverer.reraise()
  return ret
