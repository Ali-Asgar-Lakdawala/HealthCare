import pickle
from random import choice
from sklearn.svm import SVC
import streamlit as st

pickle_in= open('models\\brest_cancer_detection 1.pkl','rb')
brest_cancer_detection=pickle.load(pickle_in)

def main():
    activities=["Home", "Brest Cancer Detection", "About","Contack Us","Error and Solutions"]
    choice=st.sidebar.selectbox('SElect Activity',activities)

    if choice == "Home":
        st.title("Wellcome aliens")
        st.header('Select a ML project from the sidebar')       
        html_temp_home1 = """<div style="background-color:#6D7B8D;padding:10px">
                                            <h4 style="color:white;text-align:center;">
                                            Bike sharing demand prediction.</h4>
                                            </div>
                                            </br>"""
    
    if choice== 'Brest Cancer Detection':
        st.header('Brest Cancer Detection')

        radius_mean=st.number_input("radius_mean",min_value=0.0)
        texture_mean=st.number_input("texture_mean",min_value=0.0)
        perimeter_mean=st.number_input("perimeter_mean",min_value=0.0)
        area_mean=st.number_input("area_mean",min_value=0.0)
        smoothness_mean=st.number_input("smoothness_mean",min_value=0.0)
        compactness_mean=st.number_input("compactness_mean",min_value=0.0)
        concavity_mean=st.number_input("concavity_mean",min_value=0.0)
        concave_points_mean=st.number_input("concave points_mean",min_value=0.0)
        symmetry_mean=st.number_input("symmetry_mean",min_value=0.0)
        fractal_dimension_mean=st.number_input("fractal_dimension_mean",min_value=0.0)
        radius_se=st.number_input("radius_se",min_value=0.0)
        texture_se=st.number_input("texture_se",min_value=0.0)
        perimeter_se=st.number_input("perimeter_se",min_value=0.0)
        area_se=st.number_input("area_se",min_value=0.0)
        smoothness_se=st.number_input("smoothness_se",min_value=0.0)
        compactness_se=st.number_input("compactness_se",min_value=0.0)
        concavity_se=st.number_input("concavity_se",min_value=0.0)
        concave_points_se=st.number_input("concave points_se",min_value=0.0)
        symmetry_se=st.number_input("symmetry_se",min_value=0.0)
        fractal_dimension_se=st.number_input("fractal_dimension_se",min_value=0.0)
        radius_worst=st.number_input("radius_worst",min_value=0.0)
        texture_worst=st.number_input("texture_worst",min_value=0.0)
        perimeter_worst=st.number_input("perimeter_worst",min_value=0.0)
        area_worst=st.number_input("area_worst",min_value=0.0)
        smoothness_worst=st.number_input("smoothness_worst",min_value=0.0)
        compactness_worst=st.number_input("compactness_worst",min_value=0.0)
        concavity_worst=st.number_input("concavity_worst",min_value=0.0)
        concave_points_worst=st.number_input("concave points_worst",min_value=0.0)
        symmetry_worst=st.number_input("symmetry_worst",min_value=0.0)
        fractal_dimension_worst=st.number_input("fractal_dimension_worst",min_value=0.0)

        if st.button("Predict"):

            result=brest_cancer_detection.predict([[radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,
                                        concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,
                                        smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,
                                        texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,
                                        symmetry_worst,fractal_dimension_worst]])
            if result=='M':
                predict='Sorry! you are Suffering from Cancer'
            else:
                predict='Congrats ! you are Healthy'

            st.success('The output is {}'.format(predict))

if __name__=='__main__':
    main()