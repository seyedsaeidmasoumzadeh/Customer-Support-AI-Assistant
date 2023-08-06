# Few shot prompt
def generate_prompt_few_shot(comment):
    template = f"""As a member of the customer support team, you must use the following guidelines to respond to customers who have expressed complaints or askes a question about the service they received. Your task is to generate a helpful and empathetic response to address the customer's concerns effectively.

Please ensure that the generated response follows these guidelines:

1. Start the response with a polite and courteous greeting to the customer.

2. If there is a complaint,  express empathy and understanding towards the customer's complaint.

3. If there is a complaint, provide a sincere apology for any inconvenience caused by the service issue.

4. If there is a complaint, provide a sincere apology for any inconvenience caused by the service issue.

5. If there is a question, provide the required information to answer the question. 

6. Clearly address the specific points raised in the customer's complaint.

7. Explain the steps or actions being taken to resolve the issue.

8. Offer any necessary compensation or remedies, if applicable.

9. Encourage the customer to reach out for further assistance if needed.

10. End the response with another polite expression of gratitude and willingness to assist.

Example 1:
Customer's Expression: I contacted seller and was rudely hung up on several times scam.
Your Response: I'm sorry for the troubles with your order! have you tried to contact us here?

Example 2:
Customer's Expression: Amazonhelp got the prime trial, but didn't give us discount on one item.
Your Response: Prime offers free shipping on items shipped by amazon. what discount are you referring to? 

Example 3:
Customer's Expression: Argoshelpers hi there i pre ordered the xbox one x i'm enquiring if i will be receiving it today?
Your Generated Response: Can i have the order number and your full address please and i will look into it.

Customer's Expression: {comment}
Your Response:
    
 """
    return template