  
#import package
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import time
import pickle

#import the data

my_model = pd.read_pickle("rf_model.pkl")
#my_model = pickle.load(open("rf_model.p","rb"))
image = Image.open("kickstarter_header.png")
st.title("Welcome to the Kickstarter Success Prediction App")
st.image(image, use_column_width=True)

#checking the data
st.write("This is an application for predicting the success and failure of a kickstarter campaign!")

# List out the categorical variables

category = ['category_Academic',
 'category_Accessories',
 'category_Action',
 'category_Animals',
 'category_Animation',
 'category_Anthologies',
 'category_Apparel',
 'category_Apps',
 'category_Architecture',
 'category_Art',
 'category_Art Books',
 'category_Audio',
 'category_Bacon',
 'category_Blues',
 'category_Calendars',
 'category_Camera Equipment',
 'category_Candles',
 'category_Ceramics',
 "category_Children's Books",
 'category_Childrenswear',
 'category_Chiptune',
 'category_Civic Design',
 'category_Classical Music',
 'category_Comedy',
 'category_Comic Books',
 'category_Comics',
 'category_Community Gardens',
 'category_Conceptual Art',
 'category_Cookbooks',
 'category_Country & Folk',
 'category_Couture',
 'category_Crafts',
 'category_Crochet',
 'category_DIY',
 'category_DIY Electronics',
 'category_Dance',
 'category_Design',
 'category_Digital Art',
 'category_Documentary',
 'category_Drama',
 'category_Drinks',
 'category_Electronic Music',
 'category_Embroidery',
 'category_Events',
 'category_Experimental',
 'category_Fabrication Tools',
 'category_Faith',
 'category_Family',
 'category_Fantasy',
 "category_Farmer's Markets",
 'category_Farms',
 'category_Fashion',
 'category_Festivals',
 'category_Fiction',
 'category_Film & Video',
 'category_Fine Art',
 'category_Flight',
 'category_Food',
 'category_Food Trucks',
 'category_Footwear',
 'category_Gadgets',
 'category_Games',
 'category_Gaming Hardware',
 'category_Glass',
 'category_Graphic Design',
 'category_Graphic Novels',
 'category_Hardware',
 'category_Hip-Hop',
 'category_Horror',
 'category_Illustration',
 'category_Immersive',
 'category_Indie Rock',
 'category_Installations',
 'category_Interactive Design',
 'category_Jazz',
 'category_Jewelry',
 'category_Journalism',
 'category_Kids',
 'category_Knitting',
 'category_Latin',
 'category_Letterpress',
 'category_Literary Journals',
 'category_Literary Spaces',
 'category_Live Games',
 'category_Makerspaces',
 'category_Metal',
 'category_Mixed Media',
 'category_Mobile Games',
 'category_Movie Theaters',
 'category_Music',
 'category_Music Videos',
 'category_Musical',
 'category_Narrative Film',
 'category_Nature',
 'category_Nonfiction',
 'category_Painting',
 'category_People',
 'category_Performance Art',
 'category_Performances',
 'category_Periodicals',
 'category_Pet Fashion',
 'category_Photo',
 'category_Photobooks',
 'category_Photography',
 'category_Places',
 'category_Playing Cards',
 'category_Plays',
 'category_Poetry',
 'category_Pop',
 'category_Pottery',
 'category_Print',
 'category_Printing',
 'category_Product Design',
 'category_Public Art',
 'category_Publishing',
 'category_Punk',
 'category_Puzzles',
 'category_Quilts',
 'category_R&B',
 'category_Radio & Podcasts',
 'category_Ready-to-wear',
 'category_Residencies',
 'category_Restaurants',
 'category_Robots',
 'category_Rock',
 'category_Romance',
 'category_Science Fiction',
 'category_Sculpture',
 'category_Shorts',
 'category_Small Batch',
 'category_Software',
 'category_Sound',
 'category_Space Exploration',
 'category_Spaces',
 'category_Stationery',
 'category_Tabletop Games',
 'category_Taxidermy',
 'category_Technology',
 'category_Television',
 'category_Textiles',
 'category_Theater',
 'category_Thrillers',
 'category_Translations',
 'category_Typography',
 'category_Vegan',
 'category_Video',
 'category_Video Art',
 'category_Video Games',
 'category_Wearables',
 'category_Weaving',
 'category_Web',
 'category_Webcomics',
 'category_Webseries',
 'category_Woodworking',
 'category_Workshops',
 'category_World Music',
 'category_Young Adult',
 'category_Zines']



main_category = ['main_category_Comics',
 'main_category_Crafts',
 'main_category_Dance',
 'main_category_Design',
 'main_category_Fashion',
 'main_category_Film & Video',
 'main_category_Food',
 'main_category_Games',
 'main_category_Journalism',
 'main_category_Music',
 'main_category_Photography',
 'main_category_Publishing',
 'main_category_Technology',
 'main_category_Theater']

country = ['country_AU',
 'country_BE',
 'country_CA',
 'country_CH',
 'country_DE',
 'country_DK',
 'country_ES',
 'country_FR',
 'country_GB',
 'country_HK',
 'country_IE',
 'country_IT',
 'country_JP',
 'country_LU',
 'country_MX',
 'country_N,0"',
 'country_NL',
 'country_NO',
 'country_NZ',
 'country_SE',
 'country_SG',
 'country_US']

all_cats = category + main_category + country

# create selection boxes for each categorical option

main_cat = st.selectbox('main category', main_category, format_func = lambda x: x[14:])
sub_cat = st.selectbox('sub category', category, format_func = lambda x: x[9:])
'''
If this is a **tabletop game**, you should checkout my [other app](https://frozen-sierra-31974.herokuapp.com/)
'''
country_input = st.selectbox('country', country, index = 21, format_func = lambda x: x[8:])

st.write(country.index('country_US'))

# set sliders to assign duration and campaign goal

duration = st.number_input('duration of campaign', 1,95,1)
goal = st.number_input('campaign goal',1,10000000000,1)

# create empty array of zeros

test_array = np.array([0] * 196)

test_array[all_cats.index(sub_cat)] = 1
test_array[all_cats.index(main_cat)] = 1
test_array[all_cats.index(country_input)] = 1
test_array[-2] = goal
test_array[-1] = duration

features = np.array([duration])
prediction = my_model.predict(test_array.reshape(1,-1))

st.title('Is this is a kickstarter success or fail?')
success = st.empty()

if prediction[0] == 1:
    success.image(Image.open("success_image.png"), use_column_width=True)
if prediction[0] == 0:
    success.image(Image.open("failure_image.png"), use_column_width=True)

    
st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

