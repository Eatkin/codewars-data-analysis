# Codewars Data Analysis

## What is This Project?

Codewars is a website where users can submit and complete coding problems in a variety of programming languages. Since I started using it in March 2023, I have become a huge fan of it and generally try to solve problems every day.  

I decided to create this project because I was solving a lot of problems on Codewars, exploring new languages, and improving my technical skills over time. A data analysis and visualisation project was a good way of showing the progress I'd made over time.

This project was also for me to practice data sourcing, exploration and visualisation.

## Data Sourcing

I used the included [web scraper](https://github.com/Eatkin/codewars-scraper/tree/b38d0378b38b5a873e192e02314415f4eff19237) that I built to collect all the problems I have solved on Codewars.

This provides details about the programming language used, difficulty and date completed.

To get additional data about each problem, the Codewars API is used.

## Using Your Own Data

The dataset in this project is dynamic, since I am always solving new kata and thus expanding it. This means that you can use the included Codewars scraper and run the notebook cells to visualise your own data.  

It is not 100% modular so it's not guaranteed to work, but if you wish to try, simply delete the codewars.csv file and the notebook will create a new one based on the problem solutions it finds.

## Project Contents

* [Data Sourcing](https://github.com/Eatkin/codewars-scraper/tree/b38d0378b38b5a873e192e02314415f4eff19237):
  * I built a web scraper to collect all kata solved on Codewars, this is initialised as a submodule in the repository. Additional data is sourced from the Codewars API.
* [Main Notebook](https://github.com/Eatkin/codewars-data-analysis/blob/master/codewars-analysis.ipynb):
  * This is the source of where I do all my data exploration and visualisation using a Jupyter Notebook
* [Presentation Notebook](https://github.com/Eatkin/codewars-data-analysis/blob/master/presentation-notebook.ipynb)
  * This is the source of the final presentation format of the notebook. It is highly condensed, contains mostly charts and short summaries and does not contain any code.
* [Final presentation](https://eatkin.github.io/codewars-data-analysis/#/)
  * This is a slideshow created from the presentation notebook, and if you just wish to view some nice charts, this is the best way to do so
