#!/usr/bin/env python

import sys



# Initialize counters
GET_count = 0
PUT_count = 0
POST_count = 0
total_requests = 0

for line in sys.stdin:
  if line.strip():  # Skip empty lines
        total_requests += 1
        GET_count += line.count('GET')
        PUT_count += line.count('PUT')
        POST_count += line.count('POST')

# Calculate the percentage of GET requests
percentage_get_requests = (GET_count / total_requests) * 100
percentage_put_requests = (PUT_count / total_requests) * 100
percentage_post_requests = (POST_count / total_requests) * 100

# Display the result
print(f"Percentage of GET requests: {percentage_get_requests:.2f}%")
print(f"Percentage of PUT requests: {percentage_put_requests:.2f}%")
print(f"Percentage of POST requests: {percentage_post_requests:.2f}%")

