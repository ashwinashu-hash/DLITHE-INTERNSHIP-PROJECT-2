#!/usr/bin/env python
# coding: utf-8

# In[1]:


cd Desktop


# In[2]:


import pandas as pd
data = pd.read_csv('Symptoms.csv')


# In[3]:


print(data)


# In[4]:


data.info()


# In[5]:


data.describe()


# In[6]:


data.drop('id',inplace=True,axis=1)


# In[7]:


print(data)


# --> The above steps represent the first step i.e, the Data Collection.
# --> Here i have 134 columns which has various symptoms for particular dieases.
# --> I have got the details of 39 dieases.
# --> As id is not necessary i have dropped it

# In[8]:


x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values


# --->Pandas provide a unique method to retrieve rows from a Data frame. Dataframe.iloc[] method is used when the index label of a data frame is something other than numeric series of 0, 1, 2, 3….n or in case the user doesn’t know the index label. 
# Rows can be extracted using an imaginary index position which isn’t visible in the data frame.

# In[9]:


from sklearn.preprocessing import LabelEncoder
laben = LabelEncoder()
y = laben.fit_transform(y)


# --> Label encoding convert the data in machine readable form, but it assigns a unique number(starting from 0) to each class of data.
# --> As there are 39 dieases here i have imported Label Encoder to make my work simpler.

# In[10]:


print(x)


# In[11]:


print(y)


# In[12]:


from sklearn.model_selection import train_test_split as tts
x_train,x_test,y_train,y_test=tts(x,y,test_size=0.25,random_state=42)


# In[13]:


from sklearn.linear_model import LogisticRegression as logreg
model_logreg = logreg() 
model_logreg.fit(x_train,y_train)


# ----> Logistic regression is a statistical model that in its basic form uses a logistic function to model a binary dependent variable, although many more complex extensions exist. In regression analysis, logistic regression (or logit regression) is estimating the parameters of a logistic model (a form of binary regression).
# 
# ----> Am using logistic regression as it is a classification problem.

# In[14]:


y_p=model_logreg.predict(x_test)


# In[15]:


print(y_p)


# In[16]:


print(y_test)


# In[17]:


accuracy=model_logreg.score(x_test,y_test)


# In[18]:


print(accuracy)


# In[19]:


choice=input("Want to check for new entries(yes/no)?: ")
if(choice=="yes"):
    itching=float(input("Enter 1 if the patient has itching or else enter 0:"))
    skin_rash=float(input("Enter 1 if the patient has skin rashes or else enter 0:"))
    nodal_skin_eruptions=float(input("Enter 1 if the patient has nodal skin eruptions or else enter 0:"))
    continuous_sneezing=float(input("Enter 1 if the patient has continuos sneezing or else enter 0:"))
    shivering=float(input("Enter 1 if the patient has shivering or else enter 0:"))
    chills=float(input("Enter 1 if the patient has chills or else enter 0:"))
    joint_pain=float(input("Enter 1 if the patient has joint pain or else enter 0:"))
    stomach_pain=float(input("Enter 1 if the patient has stomach pain or else enter 0:"))
    acidity=float(input("Enter 1 if the patient has acidity or else enter 0:"))
    ulcers_on_tongue=float(input("Enter 1 if the patient has ulcers on tounge or else enter 0:"))
    muscle_wasting=float(input("Enter 1 if the patient has muscle wasting else enter 0:"))
    vomiting=float(input("Enter 1 if the patient has vomiting or else enter 0:"))
    burning_micturition=float(input("Enter 1 if the patient has burning micturition or else enter 0:"))
    spotting_urination=float(input("Enter 1 if the patient has spotting urination or else enter 0:"))
    fatigue=float(input("Enter 1 if the patient has fatigue or else enter 0:"))
    weight_gain=float(input("Enter 1 if the patient has gained weight or else enter 0:"))
    anxiety=float(input("Enter 1 if the patient has anxiety or else enter 0:"))
    cold_hands_and_feets=float(input("Enter 1 if the patient has cold hands and feet or else enter 0:"))
    mood_swings=float(input("Enter 1 if the patient has mood swings or else enter 0:"))
    weight_loss=float(input("Enter 1 if the patient has lost weight or else enter 0:"))
    restlessness=float(input("Enter 1 if the patient has restlesness or else enter 0:"))
    lethargy=float(input("Enter 1 if the patient has lethargy or else enter 0:"))
    patches_in_throat=float(input("Enter 1 if the patient has patches in throat or else enter 0:"))
    irregular_sugar_level=float(input("Enter 1 if the patient has irregular Blood Sugar Level or else enter 0:"))
    cough=float(input("Enter 1 if the patient has caugh or else enter 0:"))
    high_fever=float(input("Enter 1 if the patient has high fever or else enter 0:"))
    sunken_eyes=float(input("Enter 1 if the patient has sunken eyes or else enter 0:"))
    breathlessness=float(input("Enter 1 if the patient breathlessness symptom or else enter 0:"))
    sweating=float(input("Enter 1 if the patient has sweating or else enter 0:"))
    dehydration=float(input("Enter 1 if the patient has dehydration or else enter 0:"))
    indigestion=float(input("Enter 1 if the patient has indigestion or else enter 0:"))
    headache=float(input("Enter 1 if the patient has headache or else enter 0:"))
    yellowish_skin=float(input("Enter 1 if the patient has yellowish skin or else enter 0:"))
    dark_urine=float(input("Enter 1 if the patient has dark urine or else enter 0:"))
    nausea=float(input("Enter 1 if the patient has nausea or else enter 0:"))
    loss_of_appetite=float(input("Enter 1 if the patient has loss of appetite or else enter 0:"))
    pain_behind_the_eyes=float(input("Enter 1 if the patient has pain behind eyes or else enter 0:"))
    back_pain=float(input("Enter 1 if the patient has back pain or else enter 0:"))
    constipation=float(input("Enter 1 if the patient has constipation or else enter 0:"))
    abdominal_pain=float(input("Enter 1 if the patient has abdominal pain or else enter 0:"))
    diarrhoea=float(input("Enter 1 if the patient has diarrhoea or else enter 0:"))
    mild_fever=float(input("Enter 1 if the patient has mild fever or else enter 0:"))
    yellow_urine=float(input("Enter 1 if the patient has yellow urine or else enter 0:"))
    yellowing_of_eyes=float(input("Enter 1 if the patient has yellowing of eyes or else enter 0:"))
    acute_liver_failure=float(input("Enter 1 if the patient had acute liver failure or else enter 0:"))
    fluid_overload=float(input("Enter 1 if the patient has fluid overload or else enter 0:"))
    swelling_of_stomach=float(input("Enter 1 if the patient has swelling of stomach or else enter 0:"))
    swelled_lymph_nodes=float(input("Enter 1 if the patient has swelling of lymph nodes or else enter 0:"))
    malaise=float(input("Enter 1 if the patient has malaise or else enter 0:"))
    blurred_and_distorted_vision=float(input("Enter 1 if the patient has blurres and disorted vision or else enter 0:"))
    phlegm=float(input("Enter 1 if the patient has phlegm or else enter 0:"))
    throat_irritation=float(input("Enter 1 if the patient has throat irritation or else enter 0:"))
    redness_of_eyes=float(input("Enter 1 if the patient has redness of eyes or else enter 0:"))
    sinus_pressure=float(input("Enter 1 if the patient has sinus or else enter 0:"))
    runny_nose=float(input("Enter 1 if the patient has runny nose or else enter 0:"))
    congestion=float(input("Enter 1 if the patient has congestion or else enter 0:"))
    chest_pain=float(input("Enter 1 if the patient has chest pain or else enter 0:"))
    weakness_in_limbs=float(input("Enter 1 if the patient has weakness in limbs or else enter 0:"))
    fast_heart_rate=float(input("Enter 1 if the patient has fast heart rate or else enter 0:"))
    pain_during_bowel_movements=float(input("Enter 1 if the patient has pain during bowel movements or else enter 0:"))
    pain_in_anal_region=float(input("Enter 1 if the patient has pain in anal region or else enter 0:"))
    bloody_stool=float(input("Enter 1 if the patient has bloody stool or else enter 0:"))
    irritation_in_anus=float(input("Enter 1 if the patient has irritation in anus or else enter 0:"))
    neck_pain=float(input("Enter 1 if the patient has neck pain or else enter 0:"))
    dizziness=float(input("Enter 1 if the patient has dizziness or else enter 0:"))
    cramps=float(input("Enter 1 if the patient has cramps or else enter 0:"))
    bruising=float(input("Enter 1 if the patient has bruising or else enter 0:"))
    obesity=float(input("Enter 1 if the patient has obesity or else enter 0:"))
    swollen_legs=float(input("Enter 1 if the patient has swollen legs or else enter 0:"))
    swollen_blood_vessels=float(input("Enter 1 if the patient has swollen blood vessels or else enter 0:"))
    puffy_face_and_eyes=float(input("Enter 1 if the patient has puffy face and eyes or else enter 0:"))
    enlarged_thyroid=float(input("Enter 1 if the patient has enlarged thyroid or else enter 0:"))
    brittle_nails=float(input("Enter 1 if the patient has brittle nails or else enter 0:"))
    swollen_extremeties=float(input("Enter 1 if the patient has swollen extremeties or else enter 0:"))
    excessive_hunger=float(input("Enter 1 if the patient has excessive hunger or else enter 0:"))
    extra_marital_contacts=float(input("Enter 1 if the patient has ectra martial contacts or else enter 0:"))
    drying_and_tingling_lips=float(input("Enter 1 if the patient has drying and tingling lips or else enter 0:"))
    slurred_speech=float(input("Enter 1 if the patient has slurred speech or else enter 0:"))
    knee_pain=float(input("Enter 1 if the patient has knee pain or else enter 0:"))
    hip_joint_pain=float(input("Enter 1 if the patient has hip joint pain or else enter 0:"))
    muscle_weakness=float(input("Enter 1 if the patient has muscle weakness or else enter 0:"))
    stiff_neck=float(input("Enter 1 if the patient has stiff neck or else enter 0:"))
    swelling_joints=float(input("Enter 1 if the patient has swelling joints or else enter 0:"))
    movement_stiffness=float(input("Enter 1 if the patient has mpvement stiffness or else enter 0:"))
    spinning_movements=float(input("Enter 1 if the patient has spinning movements or else enter 0:"))
    loss_of_balance=float(input("Enter 1 if the patient has loss of balance  or else enter 0:"))
    unsteadiness=float(input("Enter 1 if the patient is unsteady or else enter 0:"))
    weakness_of_one_body_side=float(input("Enter 1 if the patient has weakness of one body side or else enter 0:"))
    loss_of_smell=float(input("Enter 1 if the patient has loss of smell or else enter 0:"))
    bladder_discomfort=float(input("Enter 1 if the patient has bladder discomfort or else enter 0:"))
    foul_smell_of_urine=float(input("Enter 1 if the patient has foul smell of urine or else enter 0:"))
    continuous_feel_of_urine=float(input("Enter 1 if the patient has continuos feel of urine or else enter 0:"))
    passage_of_gases=float(input("Enter 1 if the patient has passage of gases or else enter 0:"))
    internal_itching=float(input("Enter 1 if the patient has internal itching or else enter 0:"))
    toxic_look=float(input("Enter 1 if the patient has toxic look or else enter 0:"))
    depression=float(input("Enter 1 if the patient has depression or else enter 0:"))
    irritability=float(input("Enter 1 if the patient has irritanility or else enter 0:"))
    muscle_pain=float(input("Enter 1 if the patient has muscle pain or else enter 0:"))
    altered_sensorium=float(input("Enter 1 if the patient has altered sensorium or else enter 0:"))
    red_spots_over_body=float(input("Enter 1 if the patient has red spots over body or else enter 0:"))
    belly_pain=float(input("Enter 1 if the patient has belly pain or else enter 0:"))
    abnormal_menstruation=float(input("Enter 1 if the patient has abnormal mensturation or else enter 0:"))
    dischromic_patches=float(input("Enter 1 if the patient has dischromic patches or else enter 0:"))
    watering_from_eyes=float(input("Enter 1 if the patient has watering from eyes or else enter 0:"))
    increased_appetite=float(input("Enter 1 if the patient has increased appetite or else enter 0:"))
    polyuria=float(input("Enter 1 if the patient has polyuria or else enter 0:"))
    family_history=float(input("Enter 1 if the patient's family had this disease or else enter 0:"))
    mucoid_sputum=float(input("Enter 1 if the patient has mucoid sputum or else enter 0:"))
    rusty_sputum=float(input("Enter 1 if the patient has rusty sputum or else enter 0:"))
    lack_of_concentration=float(input("Enter 1 if the patient has lack of concentration or else enter 0:"))
    visual_disturbances=float(input("Enter 1 if the patient has visual disturbances or else enter 0:"))
    receiving_blood_transfusion=float(input("Enter 1 if the patient has recieved blood transfusion or else enter 0:"))
    receiving_unsterile_injections=float(input("Enter 1 if the patient had injections or else enter 0:"))
    coma=float(input("Enter 1 if the patient had been in coma or else enter 0:"))
    stomach_bleeding=float(input("Enter 1 if the patient has stomach bleeding or else enter 0:"))
    distention_of_abdomen=float(input("Enter 1 if the patient has distention of abdomen or else enter 0:"))
    history_of_alcohol_consumption=float(input("Enter 1 if the patient is alcoholic or else enter 0:"))
    fluid_overload=float(input("Enter 1 if the patient has fluid overloador else enter 0:"))
    blood_in_sputum=float(input("Enter 1 if the patient has blodd in sputum or else enter 0:"))
    prominent_veins_on_calf=float(input("Enter 1 if the patient has prominent veins on calf or else enter 0:"))
    palpitations=float(input("Enter 1 if the patient has palpitations or else enter 0:"))
    painful_walking=float(input("Enter 1 if the patient has painful walking or else enter 0:"))
    pus_filled_pimples=float(input("Enter 1 if the patient has puss filled pimples or else enter 0:"))
    blackheads=float(input("Enter 1 if the patient has blackheads or else enter 0:"))
    scurring=float(input("Enter 1 if the patient has scurring or else enter 0:"))
    skin_peeling=float(input("Enter 1 if the patient has skin peeling or else enter 0:"))
    silver_like_dusting=float(input("Enter 1 if the patient has silver like dusting or else enter 0:"))
    small_dents_in_nails=float(input("Enter 1 if the patient has small dents in nails or else enter 0:"))
    inflammatory_nails=float(input("Enter 1 if the patient has inflammatory nails or else enter 0:"))
    blister=float(input("Enter 1 if the patient has blister or else enter 0:"))
    red_sore_around_nose=float(input("Enter 1 if the patient has red sore around nose or else enter 0:"))
    yellow_crust_ooze=float(input("Enter 1 if the patient has yellow crust ooze or else enter 0:"))
    X=[[itching,skin_rash,nodal_skin_eruptions,continuous_sneezing,
    shivering,
    chills,
    joint_pain,
    stomach_pain,
    acidity,
    ulcers_on_tongue,
    muscle_wasting,
    vomiting,
    burning_micturition,
    spotting_urination,
    fatigue,
    weight_gain,
    anxiety,
    cold_hands_and_feets,
    mood_swings,
    weight_loss,
    restlessness,
    lethargy,
    patches_in_throat,
    irregular_sugar_level,
    cough,
    high_fever,
    sunken_eyes,
    breathlessness,
    sweating,
    dehydration,
    indigestion,
    headache,
    yellowish_skin,
    dark_urine,
    nausea,
    loss_of_appetite,
    pain_behind_the_eyes,
    back_pain,
    constipation,
    abdominal_pain,
    diarrhoea,
    mild_fever,
    yellow_urine,
    yellowing_of_eyes,
    acute_liver_failure,
    fluid_overload,
    swelling_of_stomach,
    swelled_lymph_nodes,
    malaise,
    blurred_and_distorted_vision,
    phlegm,
    throat_irritation,
    redness_of_eyes,
    sinus_pressure,
    runny_nose,
    congestion,
    chest_pain,
    weakness_in_limbs,
    fast_heart_rate,
    pain_during_bowel_movements,
    pain_in_anal_region,
    bloody_stool,
    irritation_in_anus,
    neck_pain,
    dizziness,
    cramps,
    bruising,
    obesity,
    swollen_legs,
    swollen_blood_vessels,
    puffy_face_and_eyes,
    enlarged_thyroid,
    brittle_nails,
    swollen_extremeties,
    excessive_hunger,
    extra_marital_contacts,
    drying_and_tingling_lips,
    slurred_speech,
    knee_pain,
    hip_joint_pain,
    muscle_weakness,
    stiff_neck,
    swelling_joints,
    movement_stiffness,
    spinning_movements,
    loss_of_balance,
    unsteadiness,
    weakness_of_one_body_side,
    loss_of_smell,
    bladder_discomfort,
    foul_smell_of_urine,
    continuous_feel_of_urine,
    passage_of_gases,
    internal_itching,
    toxic_look,
    depression,
    irritability,
    muscle_pain,
    altered_sensorium,
    red_spots_over_body,
    belly_pain,
    abnormal_menstruation,
    dischromic_patches,
    watering_from_eyes,
    increased_appetite,
    polyuria,
    family_history,
    mucoid_sputum,
    rusty_sputum,
    lack_of_concentration,
    visual_disturbances,
    receiving_blood_transfusion,
    receiving_unsterile_injections,
    coma,
    stomach_bleeding,
    distention_of_abdomen,
    history_of_alcohol_consumption,
    fluid_overload,
    blood_in_sputum,
    prominent_veins_on_calf,
    palpitations,
    painful_walking,
    pus_filled_pimples,
    blackheads,
    scurring,
    skin_peeling,
    silver_like_dusting,
    small_dents_in_nails,
    inflammatory_nails,
    blister,
    red_sore_around_nose,
    yellow_crust_ooze ]]
    y_pred=model_logreg.predict(X)
    print("The disease of the patient is :",y_pred)


# ----> Please Entwr all the symptoms you have and then check for the disease
# ----> The output would be between 1 to 40. So please refer the redme file to knw the disease respective with their number.

# In[20]:


import seaborn as sn


# In[21]:


sn.heatmap(data.corr(),annot=True)


# In[ ]:




