# testing for convert string having dict properties into dict type

'''
import json
str1 = '{"prod12":2,"prod13":2}'
result = json.loads(str1)
print(str1,type(str1))
print(result,type(result))
'''

#testing for delivery two responses at a time(simultaneousoly)
### SEE THE PRINTED VALUE CAREFULLY THEY HAVE MORE DIFFERENCES
"""
import json 
response1 = [{"product_name": "watch", "price": 239, "quantity": 2}, {"product_name": "laptops", "price": 354, "quantity": 2}]
response2 = [{"text": "your order has confirmed for delivery", "time": "2023-07-03"}, {"text": "your product is shipped", "time": "2023-07-03"}, {"text": "your product reached at lucknow store.", "time": "2023-07-03"}]

response = response1 + response2
print(response)     #  --> see below
'''
[{"product_name": "watch", "price": 239, "quantity": 2}, {"product_name": "laptops", "price": 354, "quantity": 2}, {"text": "your order has confirmed for delivery", "time": "2023-07-03"}, {"text": "your product is shipped", "time": "2023-07-03"}, {"text": "your product reached at lucknow store.", "time": "2023-07-03"}]
'''
response = json.dumps(response,default=str)
print(response)     #  --> see below
'''
[{"product_name": "watch", "price": 239, "quantity": 2}, {"product_name": "laptops", "price": 354, "quantity": 2}, {"text": "your order has confirmed for delivery", "time": "2023-07-03"}, {"text": "your product is shipped", "time": "2023-07-03"}, {"text": "your product reached at lucknow store.", "time": "2023-07-03"}]
'''
response = [response1 , response2]
print(response)     #  --> see below
'''
[[{"product_name": "watch", "price": 239, "quantity": 2}, {"product_name": "laptops", "price": 354, "quantity": 2}], [{"text": "your order has confirmed for delivery", "time": "2023-07-03"}, {"text": "your product is shipped", "time": "2023-07-03"}, {"text": "your product reached at lucknow store.", "time": "2023-07-03"}]]
'''

"""