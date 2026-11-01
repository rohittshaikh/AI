import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori , association_rules

transaction = [
    ["Milk","Bread"],
    ["Milk","Bread","Bread"],
    ["Milk","Bread"],
    ["Bread"]
    ]

encoder = TransactionEncoder()
encoded = encoder.fit(transaction).transform(transaction)
df = pd.DataFrame(encoded,columns = encoder.columns_)

items = apriori(df,min_support = 0.4 ,use_colnames = True)
print("frequent items : \n" , items )

rules = association_rules(items, metric= "confidence" , min_threshold = 0.6)
print("Association rules : \n" , rules[[ 'antecedents','consequents' , 'support' , 'confidence']])
