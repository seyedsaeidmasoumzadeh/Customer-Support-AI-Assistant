## Enhancing Customer Support in Order and Delivery Service with a Large Language Model AI Assistant
 
<br>

### Build container 
- This is the first thing you need to do 

```
make build
```

### Running jupyter lab
- Provides an interactive environment to explore the notebook used for Data Analysis, Motivations, Model implementations, and Evaluations.  
- You can also see the HTML version of the notebook [here](https://nbviewer.org/github/seyedsaeidmasoumzadeh/Customer-Support-AI-Assistant/blob/master/notebook/ai_assistant.ipynb).

```
make jupyter
```


### Running Fast API
- Allows you to have access to the APIs using the final trained model (by notebook) to response

```
make run
```
### Get the response from the APP

1. Start FastAPI by running the command `make run` in your terminal.

2. Open another terminal and launch IPython.

3. In IPython, execute the following code snippet:

```python
import requests

# Define the endpoint URL
url = "http://0.0.0.0:8000/multiple_response"

# Define the comment to be completed
comment = "After waiting for five days, I still haven't received my delivery, which was expected to arrive the day after the purchase."

# Create a payload with the comment
payload = {"comment": comment}

# Send a POST request to the endpoint
result = requests.post(url, json=payload)

# Check the response status code
if result.status_code == 200:
    # Extract the response from the result
    output = result.json()["response"]
    print("output:", output)
else:
    print("Request failed with status code:", response.status_code)
```

1. If you are using your local machine with a CPU to run the model, please understand that it may take some time as it is programmed to produce five different options or answers to your comment. 

2. This is an example of what the model generated for the above code

```
output: [
    'You are welcome to make an appointment. Please be sure to check the status of your order and to ensure the delivery has been made to your address.',
    'I am very sorry for your inconvenience, however, I will do my best to expedite your order for you.',
    "I'll keep you updated on the status.",
    "I'm not sure if you received the wrong order, or that the product was defective. If you are not satisfied with the product, there is no way to refund the money that you paid.",
    'I will do my best to reach out for your assistance in the future. I will be adding you to the list of items that have been shipping.'
    ]
```


