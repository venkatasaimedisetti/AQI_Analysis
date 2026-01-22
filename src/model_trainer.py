from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

def train_prediction_model(df):
    # Encoding categorical 'state' into numeric codes
    # This is a lightweight alternative to OneHotEncoding for high-cardinality features
    df['state_id'] = df['state'].astype('category').cat.codes
    
    X = df[['state_id']] 
    y = df['aqi_value']
    
    # 80-20 split is standard for a dataset of this size (~235k rows)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Chosen Random Forest because it handles outliers in pollution data 
    # better than simple Linear Regression.
    regressor = RandomForestRegressor(n_estimators=50, max_depth=10, random_state=42)
    regressor.fit(X_train, y_train)
    
    # Evaluate performance
    y_pred = regressor.predict(X_test)
    accuracy_score = r2_score(y_test, y_pred)
    
    return accuracy_score