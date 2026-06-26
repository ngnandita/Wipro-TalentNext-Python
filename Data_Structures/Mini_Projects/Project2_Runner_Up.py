"""
Project Name : Runner-Up Score Finder
Module       : Data Structure
"""

# Input scores
scores = [2, 3, 6, 6, 5]

# Duplicate values remove karo
unique_scores = list(set(scores))

# Highest score remove karo
unique_scores.remove(max(unique_scores))

# Runner-up print karo
print("Scores:", scores)
print("Runner-up score:", max(unique_scores))