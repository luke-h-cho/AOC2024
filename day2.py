'''
--- Day 2: Red-Nosed Reports ---
Part 1:
Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.

While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign of the Chief Historian, the engineers there run up to you as soon as they see you. Apparently, they still talk about the time Rudolph was saved through molecular synthesis from a single electron.

They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. You offer to help with the unusual data.

The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
In the example above, the reports can be found safe or unsafe by checking those rules:

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?

Part 2:
The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
'''

from tools import process_string_input_by_lines
from inputs import day2_input

def helper(list: list[int]) -> bool:
  prev, next = list[0], list[1]
  # if the difference is within the allowed range (less than 4 but at least 1)
  if abs(next - prev) <= 3 and abs(next-prev) > 0:
    # declare the flag to indicate whether the list is increasing or decreasing
    is_increasing = (next - prev) > 0
    # iterate thru the report from index 1
    for i in range(1, len(list)):
      # set the current value
      next = list[i]
      # if it's increasing,
      if is_increasing:
        # make sure that it's within the range - if not,
        if (next - prev) <= 0 or (next - prev) > 3:
          # return False
          return False
      # if it's decreasing, same logic applies
      else:
        if (prev - next) <= 0 or (prev - next) > 3:
          return False
      # set the prev as the next value as we move onto the next element in the list
      prev = next
    # return true if the list is valid
    return True
  # return false by default
  return False

# part 1
def number_of_safe_reports(reports: list[list[int]]) -> int:
  # declare var to return
  safe_reports = 0
  # iterate thru the reports, which is the list of integers
  for list in reports:
    # use helper function to validate each report
    # if the list is valid
    if helper(list):
      # we increment the number of safe report by 1
      safe_reports += 1
  # return number of safe reports
  return safe_reports

# print(number_of_safe_reports(process_string_input_by_lines(day2_input)))

# part 2
def number_of_safe_reports_with_dampener(reports: list[list[int]]) -> int:
  # declare the var to return
  safe_reports = 0
  # iterate thru the reports
  for list in reports:
    # iterate thru the list
    for i in range(len(list)):
      # use the helper func to validate the temporary list with just one element removed from the original
      if helper(list[:i] + list[i+1:]):
        # once the safe report is found, increment and break out of the loop
        safe_reports += 1
        break
  # return the number of safe reports without or with one dempener used
  return safe_reports

# print(number_of_safe_reports_with_dampener(process_string_input_by_lines(day2_input)))
