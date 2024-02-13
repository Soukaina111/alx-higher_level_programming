-- Show average temperatures grouped by city 
SELECT city, AVG(value) AS average_tmp FROM temperatures GROUP BY city ORDER BY average_tmp DESC;
