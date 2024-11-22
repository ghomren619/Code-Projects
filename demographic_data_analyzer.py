# Author: Ghomren Victor Oghenetega
# Date: 20-11-2024
# Language used: Python
# Description: To thoroughly analyse a 1994 adult data census extract
# Modules used = Pandas as Numpy


import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = None

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = None

    # What is the average age of men?
    average_age_men = None

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = None

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = None
    lower_education = None

    # percentage with salary >50K
    higher_education_rich = None
    lower_education_rich = None

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = None

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = None

    rich_percentage = None

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None

    adult_data = pd.read_csv("adult.data.csv") 
    adult_data_df = pd.DataFrame(adult_data)
    
    sample_size = len(adult_data_df)
    
    race_list = adult_data_df['race'].values.tolist()
    race_list_set = list(set(race_list))
    white_citizens = black_citizens = other_citizens = amer_indian_eskimo_citizens = asian_pac_islander_citizens = 0

    for race in race_list:
        if race == "White":
            white_citizens += 1
        elif race == "Black":
            black_citizens += 1
        elif race == "Other":
            other_citizens += 1
        elif race == "Amer-Indian-Eskimo":
            amer_indian_eskimo_citizens += 1
        else:
            asian_pac_islander_citizens += 1
    
    all_citizens = [amer_indian_eskimo_citizens, black_citizens, asian_pac_islander_citizens, other_citizens, white_citizens]
    
    race_count = pd.Series(all_citizens)
    race_count.index = [race_list_set]
    
    gender_age_df = pd.DataFrame(adult_data_df["age"].values)
    
    # Making a dataframe for the males' ages
    gender_age_df.index = adult_data_df["sex"].values
    
    gender_age_df
    
    key_gender_list = adult_data_df["sex"].values.tolist()
    key_age_list = adult_data_df["age"].values.tolist()
    
    # Using a method to remove females and their ages out of the lists
    gender_series = pd.Series(key_age_list, index = key_gender_list)
    
    male_gender_series = gender_series.drop("Female")
    
    male_age_sum = np.sum(male_gender_series.values)
    male_age_sum = int(male_age_sum)
    
    male_length = len(male_gender_series)
    
    average_age_men = male_age_sum/male_length
    average_age_men = round(average_age_men, 1)

    # average_age_men (ANSWER TO QUESTION 2)
    degree_list = adult_data_df['education'].values.tolist()
    degree_num = adult_data_df['education-num'].values.tolist()
    degree_list_set = list(set(degree_list))
    
    degree_series = pd.Series(degree_num, index = degree_list)
    
    # Removing all educational degrees that are not "Bachelor"
    bachelor_series = degree_series.loc[degree_series.index.difference(["12th", "11th","10th", "9th", "7th-8th",
                                                                       "5th-6th", "1st-4th", "Masters", "Some-college",
                                                                       "Assoc-acdm","Preschool","Assoc-voc","Doctorate",
                                                                       "Prof-school","HS-grad"])]
    bachelor_length = len(bachelor_series)
    
    percentage_bachelors = (bachelor_length/sample_size) * 100
    percentage_bachelors = round(percentage_bachelors, 1)
    # percentage_bachelors (ANSWER TO QUESTION 3)
    
    salaries_list = adult_data_df['salary'].values.tolist()
    professional_salaries = pd.Series(salaries_list, index = degree_list)
    
    advanced_education = professional_salaries.loc[professional_salaries.index.difference(["12th", "11th","10th", "9th", "7th-8th",
                                                                       "5th-6th", "1st-4th", "Some-college",
                                                                       "Assoc-acdm","Preschool","Assoc-voc",
                                                                       "Prof-school","HS-grad"])]
    
    num_adv = len(advanced_education)
    
    reverse_adv_edu = pd.Series(advanced_education.index, index = advanced_education.values)
    
    adv_edu_above_50k = reverse_adv_edu.drop("<=50K")
    
    num_adv_edu_50k = len(adv_edu_above_50k)
    
    higher_education_rich = (num_adv_edu_50k/num_adv) * 100
    higher_education_rich = round(higher_education_rich, 1)
    
    lower_education_rich = 100 - higher_education_rich

    
    # percent_50l (ANSWER TO QUESTION 4)
    
    non_adv_education = professional_salaries.loc[professional_salaries.index.difference(["Bachelors", "Masters", "Doctorate"])]
    
    # swapping the series
    
    non_adv_education = pd.Series(non_adv_education.index, index = non_adv_education.values)
    
    non_adv_length = len(non_adv_education)
    
    # dropping those that make less than 50k
    
    non_adv_above_50k = non_adv_education.drop("<=50K")
    
    num_non_adv_above_50k = len(non_adv_above_50k)
    
    percent_non_adv_above_50k = (num_non_adv_above_50k/non_adv_length) * 100
    percent_non_adv_above_50k = round(percent_non_adv_above_50k, 1)
    
    #percent_non_adv_above (ANSWER TO QUESTION 5)
    
    hours_per_week = adult_data_df['hours-per-week'].values.tolist()
    
    min_work_hours = min(hours_per_week)
    
    # min_work_hours (ANSWER TO QUESTION 6)
    
    salary_hours = pd.Series(salaries_list, index=hours_per_week)
    
    #print(set(hours_per_week))
    
    # Getting the minimum hours series
    
    min_salary_hours = salary_hours.loc[salary_hours.index.difference([i for i in range(2,100)])]
    
    min_hour_len = len(min_salary_hours)
    
    reverse_min_salary_hours = pd.Series(min_salary_hours.index, index=min_salary_hours.values)
    reverse_min_salary_hours
    
    # dropping those who have 50k or less tha 50k
    min_hour_salary_50k = reverse_min_salary_hours.drop("<=50K")
    num_min_workers = len(min_hour_salary_50k)
    
    rich_percentage = (num_min_workers/min_hour_len) * 100
    rich_percentage = round(rich_percentage, 1)

    # num_min_workers (ANSWER TO QUESTION 7)
    
    countries_list = adult_data_df['native-country'].values.tolist()
    
    countries_salaries = pd.Series(countries_list, index=salaries_list)
    
    country_above_50k = countries_salaries.drop("<=50K")
    country_above_50k_len = len(country_above_50k)
    reverse_country_above_50k = pd.Series(country_above_50k.index, index=country_above_50k.values)
    
    # Using a special method to find the country with the highest number of >50k earners
    
    highest_earning_country = reverse_country_above_50k.index.value_counts().idxmax()
    
    
    # Getting the actual value for the highest country
    highest_earning_country_count = reverse_country_above_50k[reverse_country_above_50k.index == highest_earning_country].value_counts()
    highest_earning_country_int = highest_earning_country_count.values
    highest_earning_country_num = highest_earning_country_int.item()
    
    
    # Finding the percentage
    
    highest_earning_country_percentage = (highest_earning_country_num / country_above_50k_len) * 100
    highest_earning_country_percentage = round(highest_earning_country_percentage, 1)
    
    
    # highest_earning_country_percentage (ANSWER TO QUESTION 8)
    
    occupation_list = adult_data_df['occupation'].values.tolist()
    
    country_salary_occupation_data = {
        'Country': countries_list,
        'Salary': salaries_list,
        'Occupation': occupation_list
    }
    
    country_salary_occupation_df = pd.DataFrame(country_salary_occupation_data)
    country_salary_occupation_df = country_salary_occupation_df.set_index('Country')
    
    india_country_salary_occupation_df  =   country_salary_occupation_df.loc[country_salary_occupation_df.index.difference(['?','Cambodia','Canada','China','Columbia',
                                                                                'Cuba','Dominican-Republic','Ecuador', 'El-Salvador',
                                                                              'England','France','Germany','Greece','Guatemala','Haiti',
                                                                            'Holand-Netherlands','Honduras','Hong','Hungary','Iran','Ireland','Italy',
                                                                'Jamaica','Japan','Laos','Mexico','Nicaragua','Outlying-US(Guam-USVI-etc)','Peru',
                                                            'Philippines','Poland','Portugal','Puerto-Rico','Scotland','South','Taiwan','Thailand',
                                                                'Trinadad&Tobago','United-States','Vietnam','Yugoslavia'])]
    india_length = len(india_country_salary_occupation_df)
    
    india_salary = []
    india_occupation = []
    
    for salary in india_country_salary_occupation_df["Salary"]:
        india_salary.append(salary)
    
    for occupation in india_country_salary_occupation_df["Occupation"]:
        india_occupation.append(occupation)
    
    india_occupation_salary = pd.Series(india_occupation, index=india_salary)
    india_occupation_salary = india_occupation_salary.drop("<=50K")
    india_salary_above_50K = len(india_occupation_salary)
    
    india_occupation_above_50k = pd.Series(india_occupation_salary.index, index=india_occupation_salary.values)
    
    top_IN_occupation = india_occupation_above_50k.index.value_counts().idxmax()
  
    # top_IN_occupation (ANSWER TO QUESTION9 9)
    

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
run = True

print(calculate_demographic_data(run))
