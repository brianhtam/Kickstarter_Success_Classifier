# Classifying Kickstarter Success

## Description: 
Ever fantasized about producing the next innovative, groundbreaking idea? But soon reality hits you in the face that… well, you need money. After some researching and planning, you decided to use Kickstarter to fund your campaign.

But before publishing your idea, it is wise to ask: Am I going to succeed?

Based on 300,000 past Kickstarter campaigns, I designed an interactive app to you help predict whether your idea is likely to be fully funded or underfunded. There’s also some tips and tricks along the way!

## Objective: 
Crowdfunding is all-or-nothing. If it fails, project teams will not receive any funds to actualize their visions, project backers will not receive rewards, and Kickstarter will not receive a percent of the donated funds. Essentially, every part of whole Kickstarter community get hit.

The goal of this project is to help independent creators pinpoint factors that could help or hinder a potential campaign.

## Methodology: 
The dataset I used was obtained from https://www.kaggle.com/kemical/kickstarter-projects/data#
Here are the features I worked with:
- goal, the goal amount the Kickstarter project team is aiming for in USD$
- project_duration, the campaign duration in days
- the main category of the Kickstarter campaign
- the subcategory of the campaign
- the country that the campaign is based off
All in all, I used classification model to design a machine learning app.

The machine learning model was trained on Kickstarter data from 2009 to 2018. 

Two types of error weree considered:
A false positive is campaign that was predicted to succeed, but would have failed. 
Meanwhile, a false negative is a campaign that was predicted to failed, but would have succeeded.

This model uses F1 which strikes a good balance between precision and recall.




## Results: <br>
The best model was Random Forest, but I chose to use Logistic Regression Classifier for the speed, scalability, and model interpretability. <br>
In terms of F1, logistic regression had a score of 0.57 was scored on the test set

If we ignore the main categories, the results indicate that on average: <br>
- Category matters. Certain categories of campaigns just have a better track record of succeeding in the market and have more generous perameters for sucess.
- Having a shorter project duration is crucial, specifically 30 days or less
- having a reasonable goal amount helps

The app is currently hosted at: 
http://kickstarter-success-classifier.herokuapp.com/
