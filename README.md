# ons-test-fast-api



### The Challenge
Utilising either Flask or FastAPI, create a web application that does the following.
- [x] Allows somebody to create or edit a survey. This survey will be stored as a JSON file in a Google Storage Bucket.
- [x] Allows somebody to answer a survey. This flow should save their current process / answers as they go, and allow a person to return to complete a survey at any time. The progress will be stored as a JSON object in a Google Firestore Database.
- Show a completed survey. Pulling data from both the Google Storage Bucket and the Firestore Database, display a completed survey.


Notes:

- The basic happy path functionlity has been implemented to allow templates to be created/updated via rest api endpoints, temmplated are stored as JSON files in a google cloud stroage bucked. Surveys can also be started/saved/submitted with all data for a users survey progress being stored in firestore.
- Surveys can be marked as complete within firestore but do not currently get uploaded to a cloud storage bucket on completion
- mulit-layered repository pattern was followed to build the BE architecture
- some happy path intergration tests have been written for each of the endpoint used to create/update/submit the templates and surveys


Improvements:

- handle non-happy path journeys (pydantic was used to check post req body responses but I would handle errors and HTTP responses in more detail
- bucket/file versioning in cloud storage buckets to allow versionn control of templates
- more indepth integration tests / unit tests converage
- correct configuration of IAM policies and auth with google client SDK (currently points to local json files containing secrets)
