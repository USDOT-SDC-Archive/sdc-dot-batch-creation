[![Build Status](https://travis-ci.com/usdot-jpo-sdc/sdc-dot-batch-creation.svg?branch=master)](https://travis-ci.com/usdot-jpo-sdc/sdc-dot-batch-creation)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=usdot-jpo-sdc_sdc-dot-batch-creation&metric=alert_status)](https://sonarcloud.io/dashboard?id=usdot-jpo-sdc_sdc-dot-batch-creation)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=usdot-jpo-sdc_sdc-dot-batch-creation&metric=coverage)](https://sonarcloud.io/dashboard?id=usdot-jpo-sdc_sdc-dot-batch-creation)

# sdc-dot-batch-creation

This lambda function is responsible for creating new batches and updating the old batches.

The Secure Data Commons (SDC) is a cloud-based analytics platform that enables access to traffic engineers, researchers, and data scientists to various transportation related datasets. The SDC platform is a prototype created as part of the U.S. Department of Transportation (USDOT) research project.  The objective of this prototype is to provide a secure platform, which will enable USDOT and the broader transportation sector to share and collaborate their research, tools, algorithms, analysis, and more around sensitive datasets using modern, commercially available tools without the need to install tools or software locally.  Secure Data Commons (SDC) enables collaborative but controlled integration and analysis of research data at the moderate sensitivity level (PII & CBI).


<!---                           -->
<!---     Table of Contents     -->
<!---                           -->
## Table of Contents

[I. Release Notes](#release-notes)

[II. Usage Example](#usage-example)

[III. Configuration](#configuration)

[IV. Installation](#installation)

[V. Design and Architecture](#design-architecture)

[VI. Unit Tests](#unit-tests)

[VII.  File Manifest](#file-manifest)

[VIII.  Development Setup](#development-setup)

[IX.  Release History](#release-history)

[X. Contact Information](#contact-information)

[XI. Contributing](#contributing)

[XII. Known Bugs](#known-bugs)

[XIII. Credits and Acknowledgment](#credits-and-acknowledgement)

[XIV.  CODE.GOV Registration Info](#code-gov-registration-info)


<!---                           -->
<!---     Release Notes         -->
<!---                           -->

<a name="release-notes"/>

## I. Release Notes


<!---                           -->
<!---     Usage Example         -->
<!---                           -->

<a name="usage-example"/>

## II. Usage Example



<!---                           -->
<!---     Configuration         -->
<!---                           -->

<a name="configuration"/>

## III. Configuration


<!---                           -->
<!---     Installation          -->
<!---                           -->

<a name="installation"/>

## IV. Installation


<!---                                 -->
<!---     Design and Architecture     -->
<!---                                 -->

<a name="design-architecture"/>

## V. Design and Architecture

This lamda function is triggered by aws-cloudwatch rule periodically at an interval of 5 minutes.

**1.** It creates a new batch every 5 mins.For a new batch IsCurrent attribute is set to true and ReadyForProcessing is set to false.

**2.** Every time it creates new batch it check if a batch exists with IsCurrent as true, then it is set to false and ReadyForProcessing is set to true


<!---                           -->
<!---     Unit Tests          -->
<!---                           -->

<a name="unit-tests"/>

## VI. Unit Tests




<!---                           -->
<!---     File Manifest         -->
<!---                           -->

<a name="file-manifest"/>

## VII. File Manifest


<!---                           -->
<!---     Development Setup     -->
<!---                           -->

<a name="development-setup"/>

## VIII. Development Setup

The following instructions describe the procedure to build and deploy the lambda.

### Prerequisites
*Python 3.6

### Build and Deploy the Lambda

#### Environment Variables
Below are the environment variable needed :- 

DDB_BATCH_TABLE_ARN - {arn_of_dynamo_db}

LATEST_BATCH_ID  - {latest_batch_id}

SQS_CURATED_BATCHES_QUEUE_ARN - 

#### Build Process

**Step 1**: Setup virtual environment on your system by foloowing below link
https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example-deployment-pkg.html#with-s3-example-deployment-pkg-python

**Step 2**: Crete a script file with below contents for e.g(sdc-dot-batch-creation.sh)
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


<!---                           -->
<!---     Release History       -->
<!---                           -->

<a name="release-history"/>

## IX. Release History


<!---                             -->
<!---     Contact Information     -->
<!---                             -->

<a name="contact-information"/>

## X. Contact Information

<!-- Your Name – @YourTwitter – YourEmail@example.com
Distributed under the XYZ license. See LICENSE for more information.
https://github.com/yourname/github-link -->

For any queries you can reach to support@securedatacommons.com


<!---                           -->
<!---     Contributing          -->
<!---                           -->

<a name="contributing"/>

## XI. Contributing


<!---                           -->
<!---     Known Bugs            -->
<!---                           -->

<a name="known-bugs"/>

## XII. Known Bugs


<!---                                    -->
<!---     Credits and Acknowledgment     -->
<!---                                    -->

<a name="credits-and-acknowledgement"/>

## XIII. Credits and Acknowledgment
Thank you to the Department of Transportation for funding to develop this project.


<!---                                    -->
<!---     CODE.GOV Registration Info     -->
<!---                                    -->

<a name="code-gov-registration-info">

## XIV. CODE.GOV Registration Info
Agency:  DOT

Short Description: This lambda function is responsible for creating new batches and updating the old batches.

Status: Beta

Tags: transportation, connected vehicles, intelligent transportation systems

Labor Hours:

Contact Name: support@securedatacommons.com

<!-- Contact Phone: -->
