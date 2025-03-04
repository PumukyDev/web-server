#!/bin/bash

source /etc/environment

# Make a POST request to the IONOS API to update the Dynamic DNS
# Then, storage the response in 'output'
output=$(curl -X 'POST' \
  'https://api.hosting.ionos.com/dns/v1/dyndns' \
  -H "accept: application/json" \
  -H "X-API-Key: $ID.$SecretKey" \
  -H "Content-Type: application/json" \
  -d '{
  "domains": [
    "pumukydev.com",
    "www.pumukydev.com",
    "grafana.pumukydev.com",
    "url-shortener.pumukydev.com"
    "stream.pumukydev.com"
  ],
  "description": "Dynamic DNS"
}')

# Extract the 'updateUrl' from the JSON response using jq
# The '-r' flag ensures that jq outputs without quotes
updateUrl=$(echo "$output" | jq -r '.updateUrl')

# Write the update URL to 'update_url' file
echo $updateUrl > update_url

# Display the content of the 'update_url' file
cat update_url