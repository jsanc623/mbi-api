# MBI SPA Backend

This is a Flask based API project which has two endpoints:

1. `/verify`
   1. Verifies an MBI following the [short spec](https://www.cms.gov/medicare/new-medicare-card/understanding-the-mbi.pdf) and returns true or false
2. `/generate`
   1. Generates and returns a random MBI, following the above-mentioned spec

# Tests

The project utilizes pytest for its unit testing. 

I have included a Postman collection for live testing of the API. This collection
tests the verify endpoint, generate endpoint, as well as a combination of the two (generate then verify).

# Deployment

The API is permanently deployed at https://mbi-api.juanleonardosanchez.com/

It can be deployed locally using the included `start.sh` which simply runs docker based on the provided Dockerfile.
