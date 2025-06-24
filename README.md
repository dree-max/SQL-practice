Inspired by a question from https://x.com/asmah2107
on a tweet https://x.com/asmah2107/status/1937224695625187744

Quick question :

You need to add a new, required phone_number column to your users table, which has 500 million rows.

You write a simple ALTER TABLE script. 

You run it during a "maintenance window." 

It locks the entire users table for 8 hours while it adds the new column to every row.

For 8 hours, no one can sign up or log in. 

Pain right ? You cannot perform "stop the world" operations on a live, large scale database

How will you do a “Painless Database Migration” ?

=========
To run this locally simply clone the repo and run docker-compose up --build

