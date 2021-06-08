# Lottery System Assignment


This is a lottery system where only one event takes place each day and concludes at midnights. The winning numbers are chosen from the submitted lottery ballots of that day's event. Anyone can see the results of every lottery events, can register to the event of the day as a lottery participant, and participants are able to submit lottery ballots to the event of the day. I have developed the backend API using Python Django web framework to show that I am able to work with the technology stack you are working with and used Postgresql as database. Decided to deploy the backend service and database as docker containers to allow it to work independently from its environment. Created a cron job for the system to choose the winning lottery ballot, close the old event, then create a new event at every midnight. Created basic templates for viewing the events and their details. Also automated the build/run and removing docker container commands to simplify deployment/rollback processes. 

Since the application has a microservice architecture, it can be easily scaled for high load and provide higher TPS with a help of load balancer in front, so it is easier to resolve bottlenecks. By scaling, it can prevent single point of failure and it will be possible to add more features in time without downtime. Also it is possible to configure the database and backend services to comply with CQRS concept and seperate the read and update operations to the data store for better efficiency. For instance, database can be configured to operate on multiple hosts and some instances could be used for only read-only purposes like validating participants, while others are for write purposes like registering new participants. 


![Domain Model](/domain_model.png)
Format: ![Alt Text](url)


## What did I omit:

* Did not write test cases because it would take more time and was not a requirement but it would be beneficial to work with TDD principal for quality of code and eliminating potential bugs.

* Did not develop frontend service but would be nice to provide a UI with React.

* Did not provide a login service because it would take more time but can be added to index page.

* Left some templates unfinished like registering participant or submitting ballots because I didn't want to spend too much time on that but I a added the Postman collection of the request's so you can check them out.

* Could not automate the fake data generation for reviewing, but gave the instructions for it.



## Build/Run instructions:

* Prerequisites: docker engine and docker-compose must be already installed.

* Run start.sh script. See docker containers with "docker ps". After few seconds, can be reached from http://localhost:8000/lotteries

* Instructions of generating fake data to Database:

    * Get into postgres docker container:
      docker exec -it lottery-postgres-db bash

    * Get into database:
      psql -d lotterydb -U lottery

    * Copy, paste and run the code inside ./db/insert.sql
  

## Rollback instructions:

* Run remove.sh script.

