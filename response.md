# Response
> Current content is an example; please edit it to fit your style.
## A. Required Information
1. install python to your laptop or pc
2. git clone this project
3. open CMD to here
4. python -m venv venv     for build virtual environment
5. .\venv\Scripts\activate        to activate virtual environment
6. run pip install -r requirements.txt        to install all requirement package
### A.1. Requirement Completion Rate
- [x] List all pharmacies open at a specific time and on a day of the week if requested.
  - Implemented at /get_pharmacy_time_day/{input_time}/{input_day} API.
- [x] List all masks sold by a given pharmacy, sorted by mask name or price.
  - Implemented at /mask/{input_pharmacy_name}/{input_sorted_by} API.
- [x] List all pharmacies with more or less than x mask products within a price range.
  - Implemented at /mask/{input_mask_name}/{lower_price}/{upper_price} API.
- [x] The top x users by total transaction amount of masks within a date range.
  - Implemented at /get_total_mask_price/5/2021-1-1/2021-1-3  API.
- [x] The total number of masks and dollar value of transactions within a date range.
  - Implemented at /get_total_mask_price/{date_front}/{date_end} API.
- [x] Search for pharmacies or masks by name, ranked by relevance to the search term.
  - Implemented at /search_word/{key_word} API.
- [ ] Process a user purchases a mask from a pharmacy, and handle all relevant data changes in an atomic transaction.
  - Implemented at xxx API.
### A.2. API Document
> API Document is here! [swagger UI ](https://localhost:8000/api/ui).
Before you read API Document, build the api server first. 
See A.3

### A.3. Import Data Commands
Please run these script commands to migrate the data into the database.

```
$ python app.py
$ python build_db.py
$ python load_data.py
```
## B. Bonus Information (Not yet)

>  If you completed the bonus requirements, please fill in your task below.
### B.1. Test Coverage Report

I wrote down the 20 unit tests for the APIs I built. Please check the test coverage report at [here](#test-coverage-report).

You can run the test script by using the command below:

```ruby
bundle exec rspec spec
```

### B.2. Dockerized
Please check my Dockerfile / docker-compose.yml at [here](#dockerized).

On the local machine, please follow the commands below to build it.

```bash
$ docker build --build-arg ENV=development -p 80:3000 -t my-project:1.0.0 .  
$ docker-compose up -d

# go inside the container, run the migrate data command.
$ docker exec -it my-project bash
$ rake import_data:pharmacies[PATH_TO_FILE]
$ rake import_data:user[PATH_TO_FILE]
```

### B.3. Demo Site Url

The demo site is ready on [heroku](#demo-site-url); you can try any APIs on this demo site.

## C. Other Information

### C.1. ERD

My ERD [erd-link](#erd-link).

### C.2. Technical Document

For frontend programmer reading, please check this [technical document](technical-document) to know how to operate those APIs.

- --
