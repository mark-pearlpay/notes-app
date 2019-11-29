# Pre-Requisites
* [SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3.7](https://www.python.org/downloads/)
* [Docker](https://hub.docker.com/search/?type=edition&offering=community)
* [LocalStack](https://github.com/localstack/localstack)
    

# Steps to run locally

### Serve localstack via docker compose
    <Code Repo Location>/notes-app$ docker-compose up

### Start local API gateway instance
    sam build -u; sam local start-api --docker-network notes-app_default --env-vars json/env.json
    
### Create a new note via local API
    curl -d '{"title": "test title", "content": "test content"}' http://127.0.0.1:3000/notes
    
# Running Tests
* BDD Tests are now runnable via pytest on pycharm, path is `/notes-app/tests/features/`
* TODO: Find out how to run via CLI

# TODO
- [ ] Create service and repository code
- [ ] Create unit tests
- [ ] Finish remaining scenarios for CRUD
- [ ] Add in authentication