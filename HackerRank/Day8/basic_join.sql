Query:
Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.

Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

Code:
select sum(city.population)
from city, country
where city.countrycode=country.code 
and country.continent='asia';
