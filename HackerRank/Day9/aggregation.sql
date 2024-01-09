Query:
Query the Western Longitude (LONG_W)where the smallest Northern Latitude (LAT_N) in STATION is greater than . Round your answer to  decimal places.
Code:
select round((long_w),4) from station
where lat_n >38.7780 order by lat_n limit 1

