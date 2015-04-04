#!/usr/bin/python -tt  

import sys
import time
import os.path
import urllib
import feedparser

feedDetails = [
  # URL, Directory Name
  ['http://reformedforum.org/programs/ctc/feed/?type=audio','Reformed_Forum_CTC'],
  ['http://feeds.feedburner.com/dancarlin/history?format=xml','Hardcore_History']
]

backupDirectory = '/data/Media/Audio/Podcasts/'
audioFile = urllib.URLopener()

for feedEntry in feedDetails:
  feedResults = feedparser.parse(feedEntry[0])
  print 'Downloading {} to {}{}/'.format(feedResults.feed.title, backupDirectory, feedEntry[1])
  for feedItem in feedResults.entries:
    itemTitle = feedItem.title.encode('utf-8')
    itemDate = time.strftime('%Y%m%d-%H%M%S', feedItem.published_parsed)
    print '{}.....'.format(itemTitle),
    sys.stdout.flush()
    if feedItem.enclosures:
      filePath = '{}{}/{}_{}.mp3'.format(backupDirectory, feedEntry[1], itemDate, itemTitle.replace (' ', '_'))
      if not os.path.exists(filePath):
        audioURL = urllib.urlopen(feedItem.enclosures[0]['href'])
        audioFile.retrieve(audioURL.geturl(), filePath)
        print "Done"
      else:
        print "Skipped"
