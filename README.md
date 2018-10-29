# InterviewScheduler
This project consists in a interview calendar API.
Its purpose is to specify the 1h time slots available for candidates and interviewers in order to
get matches between them.
## Run this project
### Using docker-compose
```bash
$ docker-compose up -d
```
You can now go to `localhost:4001/v1/ui/` to experiment with the endpoints.
### Or you can do it yourself
I see you are a person that takes matters into his own hands
#### Interview Scheduler Service
To install the dependencies you could activate a `virtualenv` and do
```bash
pip install -r requirements.txt
```
To run the service in dev mode you can do
```bash
python application.py
```
or usign a WSGI
```bash
uwsgi --http :4001 -w application:application -p 16
```

#### Mongo database
You could run a mongo database by doing
```bash
docker run --name some-mongo --net=host -d mongo
```
If you don't, you need to have the mongoDB running in your machine and available on port 27017
## Initialize database with examples
After running the application, you could add the candidates
 *Carlos* and *Arturito*, and the interviewers *Ines* and *Ingrid*
with a few overlapping time slots to observe the behaviour of the
application.

Do:
```bash
./init_database.sh
```
You can now go to the `/slots/matches` endpoint and see the matches between these candidates and interviewers.
Or you could use the API to create more accounts, authenticate and create more interview slots.
## Project Structure
```
InterviewScheduler/
    Dockerfile                  - Dockerfile used to create an image used in the docker-compose.yaml
    docker-compose.yaml         - Docker-compose file that runs the back-end and mongo-database
    README.md                   - This is the document you are reading
    requirements.txt            - File that specifies dependencies to be installed using pip
    swagger.yaml                - Document that specifies the REST interface following the openApi 2.0 specification standards
    application.py              - Entrypoint for the application
    interview_scheduler_service/- Package containing all the code necessary to run the python application (application.py)
        business/               - Business logic code here 
            controllers/        - Since this application is a REST service, every endpoint is mapped to function present here
            utils/              - Collection of functions used by diferent controllers and functions
        crud/                   - Has all the methods needed to access the mongo database
    test/                       - Has unit tests. Run them using *pytest*
```

To analyse the code, I suggest going to `localhost:4001/v1/ui/` to see all the endpoints
 and then going to the `interview_scheduler/business/controllers/` directory to see each endpoint function and follow from there.

 