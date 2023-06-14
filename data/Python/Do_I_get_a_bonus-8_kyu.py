# https://www.codewars.com/kata/56f6ad906b88de513f000d96
# 2023-06-01T14:02:27.945+0000
def bonus_time(salary, bonus):
    celery = salary
    salary = celery * 10
    if bonus:
        celery = salary
    return "$" + str(celery)