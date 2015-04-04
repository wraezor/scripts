#!/usr/bin/python -tt  

import sys
import math
import getopt
import datetime

def main(argv):

  inputStartDate = ""
  inputMonths    = ""
  inputReading   = "ALL"
  
  try:
    opts, args = getopt.getopt(argv, 'hups', ['startmonth=', 'duration=', 'read='])
  except getopt.GetoptError:
    print 'Invalid parameter specified'
    sys.exit(2)

  for opt, arg in opts:
    if opt in ('--startmonth'):
      inputStartDate = arg + "-01"
    elif opt in ('--duration'):
      inputMonths = arg
    elif opt in ('--read'):
      inputReading = arg

  # Set first day of plan
  startDate = datetime.datetime.strptime(inputStartDate, '%Y-%m-%d')
  
  # Overshoot duration (assuming all months have 31 days)
  planDuration = datetime.timedelta(days=int(inputMonths)*31)
  
  # Estimate end date
  endDate = startDate + planDuration
  
  # Correct duration to proper number
  planDuration = planDuration - datetime.timedelta(days=endDate.day)
   
  # Recalculate accurate end date
  endDate = startDate + planDuration


  total_chapters = (
    ("OT", 929),
    ("NT", 260)
  )

  bible = (
    ("OT", [
      ("Genesis", 50),
      ("Exodus", 40),
      ("Leviticus", 27),
      ("Numbers", 36), 
      ("Deuteronomy", 34),
      ("Joshua", 24),  
      ("Judges", 21),  
      ("Ruth", 4),
      ("1 Samuel", 31),
      ("2 Samuel", 24),
      ("1 Kings", 22),
      ("2 Kings", 25),
      ("1 Chronicles", 29),
      ("2 Chronicles", 36),
      ("Ezra", 10),
      ("Nehemiah", 13),
      ("Esther", 10),
      ("Job", 42),
      ("Psalm", 150),
      ("Proverbs", 31),
      ("Ecclesiastes", 12),
      ("Song of Solomon", 8),
      ("Isaiah", 66),  
      ("Jeremiah", 52),
      ("Lamentations", 5),
      ("Ezekiel", 48),
      ("Daniel", 12),
      ("Hosea", 14),
      ("Joel", 3),
      ("Amos", 9),
      ("Obadiah", 1),
      ("Jonah", 4),
      ("Micah", 7),
      ("Nahum", 3),
      ("Habakkuk", 3),
      ("Zephaniah", 3),
      ("Haggai", 2),
      ("Zechariah", 14),
      ("Malachi", 4)   
    ]),
    ("NT", [
      ("Matthew", 28),
      ("Mark", 16),
      ("Luke", 24),
      ("John", 21),
      ("Acts", 28),
      ("Romans", 16),
      ("1 Corinthians", 16),
      ("2 Corinthians", 13),
      ("Galatians", 6),
      ("Ephesians", 6),
      ("Philippians", 4),
      ("Colossians", 4),
      ("1 Thessalonians", 5),
      ("2 Thessalonians", 3),
      ("1 Timothy", 6),
      ("2 Timothy", 4),
      ("Titus", 3),
      ("Philemon", 1), 
      ("Hebrews", 13),
      ("James", 5),
      ("1 Peter", 5),
      ("2 Peter", 3),
      ("1 John", 5),
      ("2 John", 1),
      ("3 John", 1),
      ("Jude", 1),
      ("Revelation", 22)
    ]
  ))
  
  if inputReading == total_chapters[0][0]:
    plan_chapters = total_chapters[0][1]
    plan_book = bible[0][1]
  elif inputReading == total_chapters[1][0]:
    plan_chapters = total_chapters[1][1]
    plan_book = bible[1][1]
  elif inputReading == 'ALL':
    plan_chapters = total_chapters[0][1] + total_chapters[1][1]
    plan_book = bible[0][1] + bible[1][1]

  days_in_plan      = float(planDuration.days + 1)
  current_date      = startDate
  current_day       = 1
  chapters_per_day  = plan_chapters / days_in_plan
  chapters_read     = 0
  pace              = 0
  chapters_assigned = 0
  bookIndex         = 0
  chapterIndex      = 1

  # Loop Over Each Day in Plan
  while current_day <= days_in_plan:

    # Calculate Today's Reading Assignment
    if chapters_read < pace:
      chapters_assigned = int(math.ceil(chapters_per_day))
    else:
      chapters_assigned = int(math.floor(chapters_per_day))
      
    # Check if at the end of the Book, if so move to next Book and reset chapter index.
    if plan_book[bookIndex][1] < chapterIndex:
      chapterIndex = 1
      bookIndex += 1
      
    # Add first chapter to string for day.
    chaptersString = "{} {}".format(plan_book[bookIndex][0], chapterIndex)

    currentChapter = ""
    currentBook = ""
    for chapterNumber in range(1, chapters_assigned + 1):
      
      # Check if at the end of the Book, if so move to next Book and reset chapter index.
      if plan_book[bookIndex][1] < chapterIndex:
        chapterIndex = 1
        bookIndex += 1
      
      # Increment Chapter Counter
      chapterIndex += 1

    # Add last chapter to string for day.
    chaptersString += " - {} {}".format(plan_book[bookIndex][0], chapterIndex - 1)
    
    # Display Results
    dateString = current_date.strftime("%A, %B %d, %Y")
    print "{}\t{}".format('{:<30}'.format(dateString), chaptersString)

    # Increment Reading Counter
    chapters_read += chapters_assigned
    pace = current_day * chapters_per_day

    # Increment Dates
    current_date = startDate + datetime.timedelta(days=current_day)
    current_day += 1

if __name__ == '__main__':
    main(sys.argv[1:])
