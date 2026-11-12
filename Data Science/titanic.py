import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

# 1. Load the Titanic Dataset
# Using Seaborn's built-in dataset repository
df = sns.load_dataset('titanic')

# Alternatively, you can load it via CSV URL:
# url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
# df = pd.read_csv(url)

print(df)
print('--- First 5 Rows of the Dataset ---')
print(df[['survived', 'sex', 'pclass', 'age']].head())

# 2. Quick Statistical Analysis: Survival Rate by Gender
# survived: 0 = Died, 1 = Alive
survival_rates = df.groupby('sex')['survived'].mean() * 100
print('\n--- Survival Rate by Gender ---')
print(survival_rates.round(2).astype(str) + '% survived')

# 3. Data Preprocessing for Machine Learning
# Drop rows with missing values in our selected features
df_clean = df.dropna(subset=['survived', 'sex', 'age', 'pclass']).copy()

# Encode 'sex' into numerical values (male: 0, female: 1)
df_clean['sex_encoded'] = df_clean['sex'].map({'male': 0, 'female': 1})

# Define Features (X) and Target (y)
# Target: survived (0 = Died, 1 = Alive)
X = df_clean[['sex_encoded', 'pclass', 'age']]
y = df_clean['survived']

# 4. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Train a Logistic Regression Model
model = LogisticRegression()
model.fit(X_train, y_train)

# 6. Evaluate the Model
y_pred = model.predict(X_test)

print('\n--- Model Evaluation ---')
print(f'Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%')
print('\nClassification Report:')
print(
    classification_report(
        y_test, y_pred, target_names=['Died (0)', 'Alive (1)']
    )
)

# 7. Test a Custom Prediction
# Example: Predict for a Female (1) in 1st Class (1) aged 25
# and a Male (0) in 3rd Class (3) aged 30
sample_passengers = pd.DataFrame(
    {'sex_encoded': [1, 0], 'pclass': [1, 3], 'age': [25, 30]}
)

predictions = model.predict(sample_passengers)
print('\n--- Custom Predictions ---')
for i, pred in enumerate(predictions):
    status = 'Alive (Survived)' if pred == 1 else 'Died'
    print(f'Passenger {i+1}: Predicted Status -> {status}')