# Problem 6: Most Popular Even Destination
# Given a list of integers destinations, where each integer represents the popularity 
# score of a destination, return the most popular even destination.

# If there is a tie, return the smallest one. If there is no such destination, return -1.

from typing import Counter


def most_popular_even_destination(destinations):
  freq_map = {}

  for destination in destinations:
    if destination % 2 == 0:
      freq_map[destination] = freq_map.get(destination, 0) + 1

  if not freq_map:
    return -1

  popular_destination = -1
  max_popularity_score = 0

  for destination, popularity_score in freq_map.items():
    if popularity_score > max_popularity_score:
      max_popularity_score = popularity_score
      popular_destination = destination

    elif popularity_score == max_popularity_score:
      popular_destination = min(destination, popular_destination)

  return popular_destination
  

destinations1 = [0, 1, 2, 2, 4, 4, 1]
destinations2 = [4, 4, 4, 9, 2, 4]
destinations3 = [29, 47, 21, 41, 13, 37, 25, 7]
destinations4 = [0, 1, 4, 2, 4, 2, 1]

print(most_popular_even_destination(destinations1))
print(most_popular_even_destination(destinations2))
print(most_popular_even_destination(destinations3))
print(most_popular_even_destination(destinations4))
