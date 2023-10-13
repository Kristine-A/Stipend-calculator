#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#==================== Base Funding, 2023-24 ==================== 
#From https://physiology.utoronto.ca/2023-24-temerty-faculty-medicine-harmonized-base-funding-agreement

stipend_23_24 = {
    #Domestic stipends
    "Domestic_MSc_Admitted23_24": 37339.68,
    "Domestic_MSc_Admitted_before_23_24": 37159.68,
    "Domestic_PhD_Admitted" : 40159.68,

    #International stipends
    "International_MSc" : 60605.68,
    "International_PhD" : 40915.68 
}


# In[ ]:


#==================== SickKids Awards ==================== 

#Restracomp 
Restracomp = 26000

Restracomp_one_semester = Restracomp / 3
Restracomp_one_semester = round(Restracomp_one_semester,2)


#CSTP_50K 
CSTP_50K_total = 50000
CSTP_50K_RTC = 40000
CSTP_50K_PI = 10000

CSTP_50K_one_semester = CSTP_50K_total / 3
CSTP_50K_one_semester = round(CSTP_50K_one_semester,2)


#CSTP_60K 
CSTP_60K_total = 60000
CSTP_60K_RTC = 50000
CSTP_60K_PI = 10000

CSTP_60K_one_semester = CSTP_60K_total / 3
CSTP_60K_one_semester = round(CSTP_60K_one_semester,2)


# In[ ]:


#==================== Common External Awards ==================== 

### OGS 
#OGS - normal 
OGS_normal = 15000

OGS_normal_one_term = OGS_normal / 3
OGS_normal_one_term = round(OGS_normal_one_term,2)


#OGS - PI support 
OGS_award_support = 10000
OGS_PI_support = 5000

OGS_award_support_one_term = OGS_award_support / 3
OGS_award_support_one_term = round(OGS_award_support_one_term,2)

OGS_PI_support_one_term = OGS_PI_support / 3
OGS_PI_support_one_term = round(OGS_PI_support_one_term,2)


### CIHR CGS-M  
CGS_M = 17500 
CGS_M_one_term = CGS_M / 3
CGS_M_one_term = round(CGS_M_one_term,0)


### CIHR CGS-D with ResAllow 
CGS_D_RA = 30000
CGS_D_RA_one_term = CGS_D_RA  / 3
CGS_D_RA_one_term = round(CGS_D_RA_one_term,0)


### CIHR CGS-D without ResAllow
CGS_D = 35000
CGS_D_one_term = CGS_D / 3
CGS_D_one_term = round(CGS_D_one_term,0)


# In[ ]:


#==================== Academic Year Selection ==================== 
#current program only calculates stipend for 23-24 academic yr

Year = input("Select academic year: (i.e. Sept 2021-Aug 2022, Sept 2022-Aug 2023, Sept 2023-Aug 2024)")


# In[1]:


Awards = input("Is the student a recipient of any awards? (Type Yes or No)")


# In[2]:


if Awards == "Yes": 
    int_awards = input("Does the student any awards held at SickKids (i.e. Restracomp, CSTP, CGS-D, etc.)? (Type Yes or No)")


# In[3]:


menu_int_awards = ('Restracomp', 'CSTP', 'CIHR CGS-D', 'other')


# In[5]:


if int_awards == "Yes": 
    menu_int_awards


# In[ ]:


Restracomp_start = input("What is the start date of the Restracomp Award?")


# In[ ]:


Restracomp_end = input("What is the end date of the Restracomp Award?")

