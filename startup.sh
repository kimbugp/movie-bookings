#!/bin/bash
echo "<<<<<<<<<<<<<<<<<<<< Seed database >>>>>>>>>>>>>>>>>>>>>>>>"
flask seed-database
sleep 2

echo "<<<<<<<<<<<<<<<<<<<< START API >>>>>>>>>>>>>>>>>>>>>>>>"
gunicorn run:app -b 0.0.0.0:5000