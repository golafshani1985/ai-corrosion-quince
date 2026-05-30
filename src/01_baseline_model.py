#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from xgboost import XGBRegressor


# In[ ]:


df = pd.read_excel("../data/raw/all_article_data.xlsx")


# In[ ]:


df.head()


# In[ ]:


df1= pd.read_excel("../data/processed/clean_article_data.xlsx")


# In[ ]:


df1.head()


# In[ ]:


df1["method_code"] = df1["method"].map({"polarization": 0,"EIS": 1})
df1["acid_code"]=df1["acid_type"].map({"HCl":0,"H2SO4":1})


# ##### Check categorical feature encoding

# In[ ]:


df1[["method", "method_code"]].drop_duplicates()


# In[ ]:


df1[["acid_type", "acid_code"]].drop_duplicates()


# ## Version 2 - Correlation Analysis

# In[ ]:


correlation_data=df1[['temperature_K','qe_concentration_ppm','method_code','acid_code','IE_percent']]
correlation_matrix=correlation_data.corr()


# In[ ]:


correlation_matrix


# In[ ]:


plt.figure(figsize=(6,6))
sns.heatmap(correlation_matrix,cmap="coolwarm",annot=True,cbar=False)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("../reports/correlation_heatmap.png", dpi=300, bbox_inches="tight")
plt.show()


# In[ ]:


X= df1[['temperature_K','qe_concentration_ppm','method_code','acid_code']]


# In[ ]:


y= df1['IE_percent']


# In[ ]:


X.head()


# In[ ]:


y.head()


# In[ ]:


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=101)


# In[ ]:


lm=LinearRegression()


# In[ ]:


lm.fit(X_train,y_train)


# In[ ]:


pred_lm=lm.predict(X_test)


# In[ ]:


pred_lm


# In[ ]:


y_test


# In[ ]:


mae=mean_absolute_error(y_test,pred_lm)
print('MAE:',mae)


# In[ ]:


rmse=np.sqrt(mean_squared_error(y_test,pred_lm))
print('RMSE:',rmse)


# In[ ]:


r2=r2_score(y_test,pred_lm)
print('R2:',r2)


# In[ ]:


plt.scatter(y_test, pred_lm)
plt.xlabel('Actual IE%')
plt.ylabel('Predicted IE%')
plt.show()


# In[ ]:


lm.score(X_test,y_test)


# ### RandomForest

# In[ ]:


rfr=RandomForestRegressor(n_estimators=100,random_state=101)


# In[ ]:


rfr.fit(X_train,y_train)


# In[ ]:


pred_rf=rfr.predict(X_test)


# In[ ]:


rfr.score(X_test,y_test)


# In[ ]:


from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score


# In[ ]:


print('MAE:',mean_absolute_error(y_test,pred_rf))


# In[ ]:


print('MSE:',mean_squared_error(y_test,pred_rf))


# In[ ]:


print('RMSE:',np.sqrt(mean_squared_error(y_test,pred_rf)))


# ### XGBoost

# In[ ]:


xgb=XGBRegressor(n_estimators=100,learning_rate=0.1,max_depth=3,random_state=101)


# In[ ]:


xgb.fit(X_train,y_train)


# In[ ]:


pred_xgb=xgb.predict(X_test)


# In[ ]:


xgb_feature_importance=pd.DataFrame({"feature":X.columns,"importance":xgb.feature_importances_})
xgb_feature_importance=xgb_feature_importance.sort_values(by="importance",ascending=False)


# In[ ]:


xgb_feature_importance


# In[ ]:


plt.figure(figsize=(8, 5))
sns.barplot(data=xgb_feature_importance,x="feature",y="importance")
plt.xlabel("Feature")
plt.ylabel("Importance")
plt.title("XGBoost Feature Importance")
plt.xticks
plt.tight_layout()
plt.savefig("../reports/xgboost_feature_importance.png", dpi=300, bbox_inches="tight")
plt.show()


# ## Interpretation of Model Features
# 
# Both correlation analysis and XGBoost feature importance show that `qe_concentration_ppm` is the most influential feature for predicting inhibition efficiency.
# This result is scientifically reasonable because increasing the inhibitor concentration can improve surface coverage on St37 steel and reduce the contact between the metal surface and the acidic environment.
# The lower importance of `acid_code` and `method_code` does not mean that acid type or electrochemical method are irrelevant. It only means that, in the current dataset, inhibitor concentration has the strongest effect on `IE_percent`.
# 

# In[ ]:


print('MAE:', mean_absolute_error(y_test, pred_xgb))
print('MSE:', mean_squared_error(y_test, pred_xgb))
print('RMSE:', np.sqrt(mean_squared_error(y_test, pred_xgb)))
print('R2:', r2_score(y_test, pred_xgb))


# In[ ]:


plt.scatter(y_test, pred_xgb)
min_value = min(y_test.min(), pred_xgb.min())
max_value = max(y_test.max(), pred_xgb.max())
plt.plot([min_value, max_value], [min_value, max_value])
plt.xlabel("Actual IE%")
plt.ylabel("Predicted IE%")
plt.title("Actual vs Predicted IE% - XGBoost")
plt.savefig("../reports/xgboost_actual_vs_predicted.png",dpi=300,bbox_inches="tight")
plt.show()


# In[ ]:


def get_metrics(model_name,y_test,predictions):
    return {'model':model_name,
            'MAE':mean_absolute_error(y_test,predictions),
            'MSE':mean_squared_error(y_test,predictions),
            'RMSE':np.sqrt(mean_squared_error(y_test,predictions)),
            'R2':r2_score(y_test,predictions)}


# In[ ]:


results=[]
results.append(get_metrics('Linear Regression',y_test,pred_lm))
results.append(get_metrics('Random Forest',y_test,pred_rf))
results.append(get_metrics('XGBoost',y_test,pred_xgb))


# In[ ]:


results_df=pd.DataFrame(results)
results_df=results_df.round(3)
results_df.to_csv('../reports/model_comparison_results.csv',index=False)


# In[ ]:


results_df


# In[ ]:


models={"Linear Regression":LinearRegression(),
        "Random Forest":RandomForestRegressor(n_estimators=100,random_state=101),
        "XGBoost":XGBRegressor(n_estimators=100,learning_rate=0.1,max_depth=3,random_state=101)
        }
cv_results = []

for model_name, model in models.items():
    r2_scores = cross_val_score(model,X,y,cv=5,scoring="r2")
    mae_scores = cross_val_score(model,X,y,cv=5,scoring="neg_mean_absolute_error")
    rmse_scores = cross_val_score(model,X,y,cv=5,scoring="neg_root_mean_squared_error")

    cv_results.append({"model": model_name,"mean_R2": r2_scores.mean(),"std_R2": r2_scores.std(),"mean_MAE": -mae_scores.mean(),
                       "std_MAE": mae_scores.std(),"mean_RMSE": -rmse_scores.mean(),"std_RMSE": rmse_scores.std()})

cv_results_df = pd.DataFrame(cv_results)
cv_results_df = cv_results_df.round(3)
cv_results_df.to_csv("../reports/cross_validation_results.csv", index=False)


# In[ ]:


cv_results_df


# In[ ]:




