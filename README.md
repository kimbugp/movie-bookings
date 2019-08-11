[![Build Status](https://travis-ci.com/kimbugp/ticket-bookings.svg?branch=master)](https://travis-ci.com/kimbugp/ticket-bookings)
[![Coverage Status](https://coveralls.io/repos/github/kimbugp/ticket-bookings/badge.svg?branch=master)](https://coveralls.io/github/kimbugp/ticket-bookings?branch=master)
# Ticket-bookings
A ticket booking app


# App documentation  
[![Postman](https://run.pstmn.io/button.svg)](https://documenter.getpostman.com/view/5531020/SVYrryHS)

# Set Up Development With Docker (Preferred setup)

1. Download Docker from [here](https://docs.docker.com/)
2. Set up an account to download Docker
3. Install Docker after download
4. Go to your terminal run the command `docker login`
5. Input your Docker email and password

To setup for development with Docker after cloning the repository please do/run the following commands in the order stated below:

-   `cd <project dir>` to check into the dir
-   create a `.env` file from the template `.env.example` and update the variables
-   `docker-compose build` to build the application images
-   `docker-compose up -d` to start the api after the previous command is successful

The `docker-compose build` command builds the docker image where the api and its postgres database would be situated.

The `docker-compose up -d` command starts the application 

To stop the running containers run the command `docker-compose down`