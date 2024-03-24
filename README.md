# DNA Software Development Kit and CLI
## Overview
A Python package for interacting with the DNA Sequence Service.

### Prerequisites
Ensure that the `dna-service` API is up and running!

## Installation
At the root of this project, run the following command:
```
pip install .
```

## Setup
Export the following environment variable to target the DNA Sequence Service host (if you stuck with the defaults, the following will work as is):
```
export DNA_HOST="localhost:8080"
```

## Usage
### Upload a Test Dataset
This example uploads the test dataset from the `dna-service` project:
```
dna batch create -f  /path/to/dna-service/data/test_batch_1.json
```

### Upload a Random Dataset
This example uploads a random dataset of size n (=1000) with sequence length size k (=100000):
```
dna batch create --random -k 100000 -n 1000
```

### Search for DNA sequence by pattern
This example returns all sequences where the matching pattern "ATTA" was found:
```
dna sequence search "atta"
```
