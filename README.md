# InterviewScheduler

## Run this project
### Using docker-compose
```bash
$ docker-compose up -d
```
You can now go to `localhost:4001/v1/ui/` to experiment with the endpoints.
### Do it your self
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

## Project Structure
```
InterviewScheduler/
    Dockerfile                  - Dockerfile used to create an image used in the docker-compose.yaml
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
 