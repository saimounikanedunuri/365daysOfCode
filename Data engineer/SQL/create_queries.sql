--Write a MySQL query to create a simple table countries including columns country_id, country_name and region_id.
create table if not exists countries('country_id' int(20),'country_name' varchar(30), 'region_id' int(10))

--Write a MySQL query to create the structure of a table dup_countries similar to countries.
CREATE TABLE IF NOT EXISTS dup_countries as select * from countries;

--Write a MySQL query to create a duplicate copy of countries table including structure and data by name dup_countries.
create table if not exists dup as select * from countries

--Write a MySQL query to create a table countries set a constraint NULL.
create table if not exists countries1 (country_id varchar(2) not null)

-- Creating a table named 'countries' if it doesn't already exist, to store information about countries

CREATE TABLE IF NOT EXISTS countries(
    -- Column to store the two-letter country code
    COUNTRY_ID varchar(2),

    -- Column to store the name of the country (up to 40 characters)
    COUNTRY_NAME varchar(40),

    -- Column to store the region ID with decimal precision of 10, 0
    REGION_ID decimal(10,0)
);

