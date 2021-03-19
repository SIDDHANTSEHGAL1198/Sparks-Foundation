#!/usr/bin/env python
# coding: utf-8

# # Siddhant Sehgal

# ### Task 4- Perform Exploratory Data Analysis on dataset Global Terrorism

# # Importing dataset

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
import plotly.express as px
import chart_studio.plotly as py
get_ipython().run_line_magic('matplotlib', 'inline')

import cufflinks as cf

from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
init_notebook_mode(connected=True)
cf.go_offline()


# In[2]:


dataset=pd.read_csv(r'G:\Study Material\Projects\Data Analysis for Terrorism Dataset\globalterrorismdb_0718dist.csv',encoding='ISO-8859-1',engine='python')


# In[3]:


dataset.isnull().sum()


# In[4]:


dataset=dataset.dropna(thresh=160000,axis=1)
dataset


# In[ ]:





# In[5]:


dataset.columns


# In[6]:


dataset=dataset.drop(['eventid'],axis=1)
dataset


# In[7]:


dataset.isnull().sum()


# In[8]:


print("Country attcked most number of times",dataset['country_txt'].value_counts().index[0])
print("Region attcked most number of times",dataset['region_txt'].value_counts().index[0])
print(f"Maximum number of people killed is {dataset['nkill'].max()} that took place in {dataset.loc[dataset['nkill'].idxmax()].country_txt}")
print(f"Year with most number of attacks = {dataset['iyear'].value_counts().idxmax()}")
print(f"Month with most number of attacks = {dataset['imonth'].value_counts().idxmax()}")
print(f"Most common attcks={dataset['attacktype1_txt'].value_counts().idxmax()}")


# In[9]:


dataset['Casualities']=dataset['nkill'].fillna(0)+dataset['nwound'].fillna(0)
countries_affected = dataset.groupby(['country_txt'])['Casualities'].sum().sort_values(ascending = False)


# In[10]:


countries_affected


# In[ ]:





# In[11]:


import plotly.graph_objects as go


# In[12]:


trace=go.Bar(x=countries_affected[:15].index,
            y=countries_affected[:15].values)

layout=go.Layout(title="Countries with most casualities",xaxis=dict(title="Countries"),yaxis=dict(title="Num of Casualiies"))

fig=go.Figure(data=[trace],layout=layout)
iplot(fig)


# Fom the above graph we can tell that Iraq is the most affected by Terrorism as there are about 214k casualities.
# After that comes countries like Afganistan,Pakistan and India which are asian countries and are most targeted by terrorist.

# In[ ]:





# In[13]:


yearly_killed=dataset.groupby(['iyear'])['nkill'].sum().reset_index()
yearly_wounded=dataset.groupby(['iyear'])['nwound'].sum().reset_index()

trace1=go.Bar(x=yearly_killed['iyear'],
             y=yearly_killed['nkill'],
              name="Killed",
             marker=dict(color='black'))

trace2=go.Bar(x=yearly_wounded['iyear'],
             y=yearly_wounded['nwound'],
              name="Wounded",
             marker=dict(color='red',
                        opacity=0.4))

layout=go.Layout(title="Casualties caused yearwise", xaxis=dict(title="Year"),barmode='stack')

fig=go.Figure(data=[trace1,trace2],layout=layout)

iplot(fig)


# Attacks which were successful yearwise

# In[14]:


s1=dataset[dataset['success']==1]
sucess_attck=dataset.groupby(['iyear'])['success'].sum()


# In[ ]:





# In[15]:


trace1=go.Bar(x=sucess_attck.index,
             y=sucess_attck.values,
              name="Success Attack",
             marker=dict(color='red'))


# In[16]:


layout=go.Layout(title="Terrorism attacks successful year wise", xaxis=dict(title="Year"))

fig=go.Figure(data=[trace1],layout=layout)

iplot(fig)


# There were more than 14k successful terrorist attacks happened in year 2014.
# We can see over the years the attempts to attcak is been increased from year 2008

# In[ ]:





# In[17]:


dataset['targtype1_txt'].value_counts()


# In[18]:


trgt1=dataset['targtype1_txt'].value_counts()[:10]
trgt1


# In[19]:


l1=trgt1.index.tolist()


# In[20]:


l1


# In[21]:


trace=go.Pie(values=trgt1.values,
            labels=l1)


fig=go.Figure(data=[trace])

iplot(fig)


# Most common target has been Private Citizens and Milatary departments

# In[ ]:





# In[22]:


k=dataset['attacktype1_txt'].value_counts()


# In[23]:


k


# In[24]:


trace=go.Bar(x=k.index,
            y=k.values)

layout=go.Layout(title="Most attacks caused by", xaxis=dict(title="Attack Type"))

fig=go.Figure(data=[trace],layout=layout)
iplot(fig)


# In[ ]:





# In[ ]:





# Terrorist group which attacks more frequently

# In[25]:


l1=dataset['gname'].value_counts()[1:11]


# In[26]:


l1


# These are top 10 terrorist organisations which have attacked more frequently over the years

# In[ ]:





# In[27]:


trace=go.Bar(x=l1.index,
      y=l1.values,
            marker_color='lightslategrey')

layout=go.Layout(title="Notorious Terrorist Groups b/w 1970-2017",xaxis=dict(title="Terrorist groups"),yaxis=dict(title="Number of times"))

fig=go.Figure(data=[trace],layout=layout)

iplot(fig)


# In[ ]:





# In[28]:


dataset


# In[29]:


dataset.isnull().sum()


# In[30]:


df=pd.DataFrame()


# In[31]:


col=['iyear','Casualities','country_txt','region_txt','gname','nkill','nwound','latitude','longitude']
df=pd.DataFrame(dataset[col])


# In[32]:


df


# In[33]:


df=df.dropna(axis=0).reset_index()


# In[34]:


df


# In[35]:


import plotly.express as px
px.set_mapbox_access_token(open(r"C:\Users\user\mapbox_token.txt").read())
fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", size='Casualities' , hover_data=['region_txt','country_txt','iyear' ] ,color="Casualities",color_continuous_scale="Portland", size_max=15, zoom=10,height=700)
fig.update_layout(mapbox_style="basic")
fig.show()


# In[36]:


col1=['iyear','region_txt','country_txt','crit1','crit2','crit3','weaptype1_txt','Casualities']
df1=pd.DataFrame(dataset[col1])
df1


# When Violent attack is aimed for Different criterias
# 

# In[37]:


ct1=df1[df1['crit1']==1]
ct1


# In[38]:


ct2=df1[df1['crit2']==1]
ct2


# In[39]:


ct3=df1[df1['crit3']==1]
ct3


# In[40]:


plt.figure(figsize=(20,12))
sns.lineplot(y='Casualities',x='iyear',data=ct1,color='red')
sns.lineplot(y='Casualities',x='iyear',data=ct2,color='blue')
sns.lineplot(y='Casualities',x='iyear',data=ct3,color='black')


# In[41]:


ind=dataset[dataset['country_txt']=='India']
ind


# In[42]:


ind=ind.dropna(axis=0).reset_index()
ind


# So we can see in this dataframe that India has been attacked so many times

# In[ ]:


# fig=px.scatter_geo(ind,lat="latitude",lon="longitude",hover_data=['Casualities','imonth','iday','attacktype1_txt'],hover_name='provstate',animation_frame="iyear",color_continuous_scale="Portland")
fig.update_layout(title='Attacked India over the span of years')
fig.update_layout(mapbox_style="open-street-map",mapbox_center_lon=0)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


# In[44]:


dataset['dbsource'].unique()


# In[45]:


dbg=dataset.groupby(['dbsource'])['nkill'].sum().sort_values(ascending=False)
dbg


# In[46]:


lr=dbg[:10].index.to_list()
lr


# In[47]:


trace=go.Pie(values=dbg[:10].values,
            labels=lr)

layout=go.Layout(title="Field iddentifying attack at that time")

fig=go.Figure(data=[trace],layout=layout)
iplot(fig)


# In[ ]:





# In[48]:


kid=dataset[dataset['ishostkid']==1]
kid


# In[49]:


kid = kid.groupby(['country_txt'])['Casualities'].sum().sort_values(ascending = False)


# In[50]:


hostage_count=kid[:15]
hostage_count


# In[51]:


trace=go.Bar(x=hostage_count.index,
            y=hostage_count.values,
            marker_color=hostage_count.values)

layout=go.Layout(title="Countries in which kids were hostage",xaxis=dict(title="Countries"),yaxis=dict(title="How many times it happened"))

fig=go.Figure(data=[trace],layout=layout)
iplot(fig)


# In[ ]:




