
# coding: utf-8

# In[8]:


# -*- coding: utf-8 -*-

import sys
import pandas
import csv
import postselenium as ps
import hashtags
import FileIO

#location of spread
path = "D:/User/Desktop/Insta/Posts.xlsx"

#append in end of description
description_end = '''👉 Segue @bolsos_cheios 👈\n👇 Menciona alguém que precise disto 🔖\n🤝 Partilha para ajudar os outros 😃'''


# In[4]:


#fetch credentials
credentials = FileIO.getJsonFromFile("credentials.json")

#log into facebook creator studio
driver = ps.LogIn(credentials)


# In[10]:



#fetch
df = pandas.read_excel(path,'Posts')


#find  all files ready to upload and fetch only fields to upload
df_uploadableData = df.loc[df['State']=='🔼'][['Name','Description','Hashtags','Post Date','Post Time']]

#iterate all uploadable posts
for  index,row in df_uploadableData.iterrows():
    print(row)
    
    #set full path
    row['Image']="D:\\User\Desktop\\Insta\\Posts\\" + row['Name'] + ".png"
    
    #ready up description
    row_hashtags = hashtags.GetTextFromHashtaglist(row['Hashtags'].split())
    row['Description'] = row['Description'] + "\n \n" + description_end +"\n \n" + row_hashtags
    
    #Post It
    ps.SchedulePost(row,driver)
    


# In[17]:


#change state
df.loc[df['State']=='🔼','State']='✅'

#Save back the file
df.to_excel(path,index=False)

driver.quit()