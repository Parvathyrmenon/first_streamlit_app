import streamlit
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.title("My Parents' new healthy diner")
streamlit.header("Breakfast Menu")
streamlit.text("🥣Omega 3 & Blueberry oatmeal")
streamlit.text("🥗Kale, spinach and rocket smoothie")
streamlit.text("🐔Hard boiled free range egg")
streamlit.text("🥑🍞Avocado toast")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.dataframe(my_fruit_list)
