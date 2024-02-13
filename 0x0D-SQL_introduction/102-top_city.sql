-- Show top 3 cities of the  given database
SELECT city, AVG(value) AS average_tmp FROM temperatures WHERE month IN (7, 8) GROUP BY city ORDER BY average_tmp DESC LIMIT 3;
