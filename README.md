# sdc-dot-batch-creation

This lambda function is responsible for creating new batches and updating the old batches.

<a name="toc"/>

## Table of Contents

[I. Release Notes](#release-notes)

[II. Overview](#overview)

[III. Design Diagram](#design-diagram)

[IV. Getting Started](#getting-started)

[V. Unit Tests](#unit-tests)

[VI. Support](#support)

---

<a name="release-notes"/>


## [I. Release Notes](ReleaseNotes.md)
TO BE UPDATED

<a name="overview"/>

## II. Overview
This lamda function is triggered by aws-cloudwatch rule periodically at an interval of 5 minutes.

**1.** It creates a new batch every 5 mins.For a new batch IsCurrent attribute is set to true and ReadyForProcessing is set to false.

**2.** Every time it creates new batch it check if a batch exists with IsCurrent as true, then it is set to false and ReadyForProcessing is set to true

<a name="design-diagram"/>

## III. Design Diagram

![ssdc-dot-batch-creation](images/sdc-dot-batch-creation.png)

<a name="getting-started"/>

## IV. Getting Started

The following instructions describe the procedure to build and deploy the lambda.

### Prerequisites
* NA 

---
### ThirdParty library

*NA

### Licensed softwares

*NA

### Programming tool versions

*Python 3.6


---
### Build and Deploy the Lambda

#### Environment Variables
Below are the environment variable needed :- 

DDB_BATCH_TABLE_ARN - {arn_of_dynamo_db}

LATEST_BATCH_ID  - {latest_batch_id}

SQS_CURATED_BATCHES_QUEUE_ARN - 

#### Build Process

**Step 1**: Setup virtual environment on your system by foloowing below link
https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example-deployment-pkg.html#with-s3-example-deployment-pkg-python

**Step 2**: Crete a script file with below contents for e.g(sdc-dot-waze-data-curation.sh)
```#!/bin/sh

cd {path_to_your_repository}/sdc-dot-batch-creation
zipFileName="{path_to_your_repository}/sdc-dot-batch-creation.zip"

echo "Zip file name is = ${zipFileName}"

zip -9 $zipFileName lambdas/*
zip -r9 $zipFileName common/*
zip -r9 $zipFileName batch_creation_lambda_handler.py

cd {path_to_your_virtual_env}/python3.6/site-packages/
zip -r9 $zipFileName chardet certifi idna
```

**Step 3**: Change the permission of the script file

```
chmod u+x sdc-dot-batch-creation.sh
```

**Step 4** Run the script file
./sdc-dot-batch-creation.sh

**Step 5**: Upload the sdc-dot-metadata-ingest.zip generated from Step 4 to a lambda function via aws console.

[Back to top](#toc)

---
<a name="unit-tests"/>

## V. Unit Tests

TO BE UPDATED

---
<a name="support"/>

## VI. Support

For any queries you can reach to support@securedatacommons.com
---
[Back to top](#toc)

