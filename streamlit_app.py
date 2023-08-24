import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
#

streamlit.title('My Parents New Healthy Dinner');
streamlit.header('Breakfast Menu');

streamlit.text('🥣 Omega3 & Blueberry Oatmeal');
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie');
streamlit.text('🐔 Hard-Boiled Free-Range Egg');
streamlit.text('🥑🍞 Avocado Toast');

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index) , ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)


# streamlit.text(fruityvice_response.json())
streamlit.header('FruitVice Fruit Advice!')

try:

  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice
    streamlit.error('Please select a fruit to get info');
  else :
    streamlit.write('The user entered ', fruit_choice)
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
except URL Error as e:
streamlit. error()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
#my_data_row = my_cur.fetchone()
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contain:")
streamlit.dataframe(my_data_rows)

streamlit.stop()

streamlit.header("Fruityvice Fruit Advice! •")

fruit_enter = streamlit.text_input('What fruit would you like information about?','jackfruit')

streamlit.write('The user entered ', fruit_enter)

my_cur2 = my_cnx.cursor()
my_cur2.execute("insert into fruit_load_list ( FRUIT_NAME ) values ('"+fruit_enter+"') ")
# my_data_rows = my_cur.fetchall()
# streamlit.dataframe(my_data_rows)







