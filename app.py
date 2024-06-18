import streamlit as st

st.title('title -> Hello Geeks')
st.header('Header -> welcome here')
st.subheader('subheader -> gfg') 
st.text('Text -> GeeksforGeeks')

st.markdown('# Hi')
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')

st.success('success!')
st.info('Information!')
st.warning('warning!')
st.error('error!')
st.exception(ZeroDivisionError('div not possible'))

st.help(ZeroDivisionError)

st.write("range(1,10)")
st.write(range(1,10))
st.write(1+2+3)
st.write("1*2*3")

st.subheader('code')
st.code('x = 10\n'
        'for i in range(x):\n'
        '\tprint(i)')

st.subheader('Checkbox')
st.checkbox('Male')
if(st.checkbox('Adult')):
    st.write("you are an Adult!")

st.subheader('Radio Button') 
radioButton = st.radio('select : ',('Male','Female','Other'))  
if(radioButton == 'Male'):
    st.write("you are a Male")
elif(radioButton == 'Female'):
    st.write("you are a Female")
elif(radioButton == 'Other'):
    st.write("you are an Other") 

st.subheader('select Box')   
selectBox = st.selectbox("Data science : ", ['Data Analysis','web Scraping','Machine Learning'
                                             ,'Deep Learning','Natural language processing','Computer vision','Image processing']) 

st.write("you've selected : ",selectBox)    

st.subheader('Multiselect Box')
multiSelBox = st.multiselect("Data science : ", ['Data Analysis','web Scraping','Machine Learning'
                                             ,'Deep Learning','Natural language processing','Computer vision','Image processing']) 
st.write("you've selected : ",len(multiSelBox) , 'courses')

st.subheader("Button")
if(st.button('Click me')):
    st.write('Thanks for clicking me')

st.subheader("slider")
vol = st.slider('select the volume',0,100,step = 1)
st.write('Volume is : ',vol)

st.subheader("Text Input")
username = st.text_input('Username : ')
password = st.text_input('Password : ',type = 'password')

st.subheader("Text Area")
st.text_area('write something about you')

st.subheader("Input number")
st.number_input('select your age',18,110)

st.subheader("Input Date")
st.date_input('Date')

st.subheader("Input Time")
st.time_input('Time') 