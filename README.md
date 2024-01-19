# Movie Connections Finder: CS50 AI Inspired Project

This Python script finds the shortest connection path between actors using movie appearance data. It's inspired by the CS50 AI's "Degrees" project and demonstrates graph search algorithms.

## Features

- Implements `shortest_path` to determine minimum degrees of separation between two actors.
- Processes actor and movie data from CSV files.
- Employs graph search algorithms for efficient data traversal.

## Specifications

- `shortest_path` returns a list of `(movie_id, person_id)` pairs, or `None` if no path exists.
- Utilizes `neighbors_for_person` to explore actor connections.

## Usage

Run with `python degrees.py [directory]`, where `[directory]` contains `people.csv`, `movies.csv`, `stars.csv`.

## More Info

Based on CS50 AI course. Project details: [CS50 AI Project - Degrees](https://cs50.harvard.edu/ai/2024/projects/0/degrees/).
