#!/bin/bash
echo "<<<<<<<<<<<<<<<<<<<< Seed database >>>>>>>>>>>>>>>>>>>>>>>>"
sleep 2
flask seed-database

echo "<<<<<<<<<<<<<<<<<<<< Seed database complete >>>>>>>>>>>>>>>>>>>>>>>>"

echo "<<<<<<<<<<<<<<<<<<<< START API >>>>>>>>>>>>>>>>>>>>>>>>"
gunicorn run:app -b 0.0.0.0:5000