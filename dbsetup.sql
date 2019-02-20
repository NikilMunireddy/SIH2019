CREATE TABLE user_steps (user_id varchar(255) , steps integer ,date varchar(255), info json);

/*
 user_id | steps | date | info 
---------+-------+------+------

*/
CREATE TABLE user_competition_details (fb_name varchar(255) ,fb_id varchar(255), no_of_comp integer,  total_points integer, meta json );

/*
 fb_name | fb_id | no_of_comp | total_points | meta 
---------+-------+------------+--------------+------
*/