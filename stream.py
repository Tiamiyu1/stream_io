import streamlit as st

st.title("Our First Web App")
st.sidebar.subheader("Nigeria States")
state = st.sidebar.radio("Choose the state", options =("Ibadan", 
                                                       "Lagos"))
name = st.text_input("Enter your name")
number = st.number_input('Insert a number')

def return_val(name, number, state):
    if state == "Ibadan":
        fact = "Hi {}! Did you know that {} is the largest city \
                    by area in Nigeria?".format(name, "Ibadan")
        num = "The multiple of {} is {}".format(number, 
                    (round(number * number, 2)))                                          
        return [fact,num]
    else:
        fact = "Hi {}! Did you know that {} is the most populous \
                    city in Nigeria?".format(name, state)
        num = "The multiple of {} is {}".format(number, 
                    (round(number * number, 2)))
        return [fact, num]
    
results = return_val(name, number, state)
if st.button("Get Fact"):
    st.success(results[0])
    st.write(results[1])