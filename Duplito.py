################################################################################################
#									HackerCamp Summer 2018 - Innovaccer
#												Analytics
#													By
#											Dhruvraj Singh Rawat
#                               https://www.linkedin.com/in/dhruvrajrawat/
################################################################################################



################################################################
# 					Importing Data-Set				I
################################################################

print('Importing Dataset')
import pandas as pd #Importing Pandas library for Data-Analysis
df=pd.read_csv('dataset/Deduplication Problem - Sample Dataset.csv') #Reading the Dataset


################################################################
# 		Vectorization the Text & Seperation of Dates
################################################################
print('Preparing the Dataset')

from sklearn.feature_extraction.text import CountVectorizer #Importing CountVectorizer for Vectorizing the Text

#Splitting the Dob to different coloumn
df['day']=pd.to_datetime(df['dob']).dt.day
df['month']=pd.to_datetime(df['dob']).dt.month
df['year']=pd.to_datetime(df['dob']).dt.year

df.drop('dob',axis=1,inplace=True) #After splitting dob droping the original column

# Splitting Gender the categorical value into 2 columns -Male and Female
gender_dummie=pd.get_dummies(df['gn']) 
df=pd.concat([df,gender_dummie],axis=1)
df.drop('gn',axis=1,inplace=True)

#Vectorizing the First-Name and Last-Name and creating dataframe for the Same
vectorizer = CountVectorizer()
Vect1=vectorizer.fit_transform(df['fn'])
vectorizer.get_feature_names()
FirstNameCol=pd.DataFrame(Vect1.toarray(),columns=vectorizer.get_feature_names())

vectorizer=CountVectorizer()
Vect2=vectorizer.fit_transform(df['ln'])
SecondNameCol=pd.DataFrame(Vect2.toarray(),columns=vectorizer.get_feature_names())

Final=pd.concat([df,FirstNameCol,SecondNameCol],axis=1) #Concatting the Vectorized First-Name & Last-Name to the original df
Final.drop(['ln','fn'],axis=1,inplace=True) #Dropping the Non-vectorized First-Name & Last-Name


################################################################
# 					Creating a Manual Feature

#		Respobile for learning Similarity between names
################################################################

from sklearn.metrics.pairwise import cosine_similarity #Using cosine similarity for finding similarity
len_fn=[]
len_ln=[]

for i in range(len(df)):
    len_fn.append('fn'+str(i)) # creating the column label for fn's
    len_ln.append('ln'+str(i)) # creating the Column label for ln's

fn_df=pd.DataFrame(3*cosine_similarity(Vect1[:], Vect1),columns=len_fn) #finding similarity coef of a given fn with other fn's
ln_df=pd.DataFrame(3*cosine_similarity(Vect2[:], Vect2),columns=len_ln) #finding similarity coef of a given ln with other ln's

Final_1=pd.concat([Final,fn_df,ln_df],axis=1) #concatting the similarity coef's to the main dataframe


################################################################
# 						Evaluation
################################################################
print('Creating Model')
# Silhouette_score function returns the mean Silhouette Coefficient over all samples.
# To obtain the values for each sample, we used silhouette_samples.
from sklearn.metrics import silhouette_score,silhouette_samples 

from sklearn.cluster import KMeans # Importing KMeans clustering algorithm

# Here we are passing different value of cluster (k) and finding the Silhouette for the same
score=[]
for i in range(2,100):
    Kmeans_model=KMeans(n_clusters=i).fit(Final_1)
    labels=Kmeans_model.labels_
    score.append(silhouette_score(Final_1,labels))

print ("The Optimum number of clusters have been found to be "+str(score.index(max(score))+2)+" with Silhouette Score of "+str(max(score)))

# Fitting the KMeans Model to Cluster Number having Highest Silhouette Score
Kmeans_model=KMeans(n_clusters=score.index(max(score))+2).fit(Final_1)
labels=Kmeans_model.labels_

# <EXTRA> Creating a CSV-File for better understand which samples are clustering to which cluster 
cluster_no=pd.DataFrame(labels,columns=['Cluster Number'])
pd.concat([df,cluster_no],axis=1).to_csv("Insider.csv",index=False)

# Creating a dataframe that contain only those samples that have highest Silhouette Score for a given cluster.
# Thus effectively removing all the duplicate samples and leaving those which sample which represents a given Cluster accurately
df1=pd.read_csv('dataset/Deduplication Problem - Sample Dataset.csv')
rst=pd.DataFrame({'Cluster No':labels,'Silhouette Score':silhouette_samples(Final_1,labels)})
result=pd.concat([df1,rst],axis=1)
result.drop_duplicates(subset=['Cluster No','Silhouette Score'],keep='first',inplace=True)
result.sort_values(by=['Silhouette Score','Cluster No'],ascending=[False,True],inplace=True)
result.drop_duplicates(subset=['Cluster No'],keep='first',inplace=True)

result.drop(['Cluster No','Silhouette Score'],axis=1).to_csv('result.csv',index=False) # Saving the above df to a CSV File
print('Duplicate Samples Removed! Check containing Result.csv for model output')