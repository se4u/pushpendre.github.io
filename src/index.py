#!/usr/bin/env python3.5
# coding: pyxl
'''
MONTHS: This list is used to convert numeric months to words in bib files.
LINKS: This list is used to convert author names to urls in bib files.

'''
import biblib.algo
import sys
from argparse import Namespace
from functools import partial
from glob import glob
from os.path import basename
from pyxl import html
from index_impl import parse, camelsplit
MONTHS = 'January February March April May June July August September October November December'.split()
cssloc = "/res/css/pub.css"
LINKS = {
  "Benjamin Van Durme": "http://www.cs.jhu.edu/~vandurme/",
  "Raman Arora": "http://www.cs.jhu.edu/~raman/",
  "Jason Eisner": "http://www.cs.jhu.edu/~jason/",
  "James Spall": "http://www.ams.jhu.edu/~spall/Personal/",
  "Vince Lyzinski": "https://www.ams.jhu.edu/~lyzinski/",
  "Matt Post": "https://mjpost.github.io/",
  "Aaron Steven White": "https://aaronstevenwhite.io",
  "Arpit Gupta": "https://www.linkedin.com/in/arpit-gupta-77759719/",
  "Tongfei Chen": "http://www.cs.jhu.edu/~tongfei/",
  "Mathias Lambert": "https://www.linkedin.com/in/mathiasl/",
  "Adam Poliak": "https://www.cs.jhu.edu/~apoliak1/",
  "Ryan Cotterell": "https://ryancotterell.github.io/",
  "Jingyi Zhu": "https://www.linkedin.com/in/jingyizhu/"
}

def makelink(x, tostring=False):
  if x in LINKS:
    r = <a href="{LINKS[x]}">{x}</a>
    if tostring:
      r = r.to_string()
  else:
    r = x
  return r

# ----------------------------------------------- #
# Create Publications list from bibliography file #
# ----------------------------------------------- #
def formatpub(ent):
  key, typ = ent.key, ent.typ
  title = year = month = author = ''
  if 'title' in ent:
    title = '"' + biblib.algo.tex_to_unicode(biblib.algo.title_case(
      ent['title'], pos=ent.field_pos['title']))+'".'
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
      author = makelink(authors[0], True)
    else:
      author = ', '.join([makelink(e, True) for e in authors[:-1]])
      if len(authors) > 2:
        author += ','
      if ent.authors()[-1].is_others():
        author += ' et al.'
      else:
        author += ' and ' + makelink(authors[-1], True)
  else:
    pass
  def make_publink(a,b):
    highlight = any(a[4:].startswith(e) for e in 'best press'.split())
    if highlight:
      return <a style="background-color: rgb(255,255,0); color: rgb(255,0,0)" href={b}>{'[' + a[4:] + ']'}</a>
    else:
      return <a href={b}>{'[' + a[4:] + ']'}</a>

  links = ' '.join([make_publink(a,b).to_string()
                    for a,b
                    in ent.items()
                    if a.startswith('link')])
  ret = title + author + '. (%s) '%(year) + links
  return ret

bib = parse('../../Bibliography_all.bib')
PUBKEYS=('chen2019improv rastogi2019scaling regan2019dataset rastogi2018nvse '
         ' poliak2017eco rastogi2017vertex rastogi2016weighting '
         ' rastogi2016efficient rastogi2015multiview rastogi2011stationarity').split()
PUBLICATIONS = <ul/>
[PUBLICATIONS.append(<li>{html.rawhtml(formatpub(bib[x]))}</li>)
 for x in PUBKEYS]

# ---------------------------------------------- #
# Create List of conferences I have reviewed for #
# ---------------------------------------------- #
REVIEWS = ', '.join(sorted([camelsplit(basename(x)) for x in glob('../../review/[A-Z]*')],
                           key=(lambda x: tuple(reversed(x.split('-')))),
                           reverse=True))
assert len(REVIEWS) > 5

# ------------ #
# INTRODUCTION #
# ------------ #
INTRODUCTION = <p>I joined the Dialog State Tracking in Amazon Alexa in April 2019. I completed my Ph.D. in Computer Science at <a href="http://www.clsp.jhu.edu">The Center For Language and Speech Processing, Johns Hopkins University</a>. My advisor was {makelink("Benjamin Van Durme")}. I TA\'d graduate courses on representation learning and machine learning for three semesters during my Phd studies, and I received the <a href="https://engineering.jhu.edu/excellence-teaching-awards/#tbs_nav_item_1">George Sommerman Graduate Teaching Assistant Award</a> with a cash award of $1000. I have reviewed for {REVIEWS}.</p>
# While at JHU I also worked with {makelink("Raman Arora")}, {makelink("Jason Eisner")}, {makelink("James Spall")}, {makelink("Vince Lyzinski")}, {makelink("Matt Post")}, {makelink("Kevin Duh")"Kevin Duh": "https://cs.jhu.edu/~kevinduh/"}, {makelink("Aaron Steven White")} amongst other .

EDUCATION = <table>
    <tbody>
      <tr>
        <td style="text-align: left;">Ph.D. and M.S. in Computer Science</td>
        <td>Johns Hopkins University</td>
        <td>2013-19</td>
        <td>3.75/4.0</td>
      </tr>
      <tr><td colspan="4" style="text-align: left;">Thesis Topic: Representation Learning for Words and Entities. I presented new methods for unsupervised learning of word and entity embeddings from texts and knowledge bases.<br/>
Courses and Grades: Natural Language Processing (A), Machine Learning in Complex Domains (A), Stochastic Search & Optimization (B), Parallel Programming (A-), Principles of Programming Languages (A-), Combinatorial Optimization (A+), Introduction to Convexity (A-)</td>
      </tr>
      <tr>
        <td  style="text-align: left;">M.Tech. in Information and Communication Technology</td>
        <td>IIT Delhi</td>
        <td>2010-11</td>
        <td>8.77/10</td>
      </tr>
      <tr>
        <td  style="text-align: left;">B.Tech. in Electrical Engg.</td>
        <td>IIT Delhi</td>
        <td>2006-10</td>
        <td>8.86/10</td>
      </tr>
    </tbody>
    # <caption>Table Type Styles</caption>
  </table>

GITHUBLINK = '''<a href="https://stackexchange.com/users/257045/pushpendre"><img src="https://stackexchange.com/users/flair/257045.png" width="208" height="58" alt="profile for Pushpendre on Stack Exchange, a network of free, community-driven Q&amp;A sites" title="profile for Pushpendre on Stack Exchange, a network of free, community-driven Q&amp;A sites" /></a>
<a href="https://github.com/se4u"><svg width="5%" height="5%" viewBox="0 0 20 15"><path fill="#828282" d="M7.999,0.431c-4.285,0-7.76,3.474-7.76,7.761 c0,3.428,2.223,6.337,5.307,7.363c0.388,0.071,0.53-0.168,0.53-0.374c0-0.184-0.007-0.672-0.01-1.32 c-2.159,0.469-2.614-1.04-2.614-1.04c-0.353-0.896-0.862-1.135-0.862-1.135c-0.705-0.481,0.053-0.472,0.053-0.472 c0.779,0.055,1.189,0.8,1.189,0.8c0.692,1.186,1.816,0.843,2.258,0.645c0.071-0.502,0.271-0.843,0.493-1.037 C4.86,11.425,3.049,10.76,3.049,7.786c0-0.847,0.302-1.54,0.799-2.082C3.768,5.507,3.501,4.718,3.924,3.65 c0,0,0.652-0.209,2.134,0.796C6.677,4.273,7.34,4.187,8,4.184c0.659,0.003,1.323,0.089,1.943,0.261 c1.482-1.004,2.132-0.796,2.132-0.796c0.423,1.068,0.157,1.857,0.077,2.054c0.497,0.542,0.798,1.235,0.798,2.082 c0,2.981-1.814,3.637-3.543,3.829c0.279,0.24,0.527,0.713,0.527,1.437c0,1.037-0.01,1.874-0.01,2.129 c0,0.208,0.14,0.449,0.534,0.373c3.081-1.028,5.302-3.935,5.302-7.362C15.76,3.906,12.285,0.431,7.999,0.431z"/></svg></a>
<a href="https://www.linkedin.com/in/pushpendre/"><img src="https://upload.wikimedia.org/wikipedia/commons/0/01/LinkedIn_Logo.svg" width="100" height="25" /></a>'''

GOOGLE_SCHOLAR_PLUG = <p>See my <a href="https://scholar.google.com/citations?user=nqDASHMAAAAJ">google scholar profile</a> for a complete list of publications.</p>

TWITTER_ASYNC_SCRIPT = '''<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'''
# ------------ #
# Final Format #
# ------------ #
columncss = '''.menu {
      float:left;
      width:220px;
    }
    .mainContent {
      float:left;
      width:75%;
    }'''
print(
<html>
 # ------ #
 # Header #
 # ------ #
 <head>
  <title>Pushpendre Rastogi Homepage</title>
  # <link rel="stylesheet" href="{cssloc}"/>
  <style> {html.rawhtml(columncss)} </style>
 </head>

 # ---- #
 # Body #
 # ---- #
 <body>
  <div class="menu">
    <img src="res/header.png" width="90%"></img>
    <a class="twitter-timeline" href="https://twitter.com/Pushpendre89?ref_src=twsrc%5Etfw" data-width="200" data-height="725" data-dnt="true">Twitter</a>{html.rawhtml(TWITTER_ASYNC_SCRIPT)}
  </div>
  <div class="main-content">
   <header class="col-span">
    <h1 class="title counter-skip">Pushpendre Rastogi</h1>
    <h2 class="subtitle counter-skip">pushpendre at gmail</h2>
   </header>

   <h2>Introduction</h2>
   {INTRODUCTION}

   <h2>Selected Publications</h2>
   {GOOGLE_SCHOLAR_PLUG}
   {PUBLICATIONS}

   <h2>Education</h2>
   {EDUCATION}

   <h2>Flairs</h2>
   {html.rawhtml(GITHUBLINK)}

  </div>
 </body>
</html>
)

#  Local Variables:
#  mode: pyxl
#  End:
