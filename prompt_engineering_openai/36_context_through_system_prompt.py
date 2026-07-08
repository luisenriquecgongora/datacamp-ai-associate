from get_response import get_response_system_user

service_description = """
Welcome to MyPersonalDelivery, your trusted and versatile delivery service partner. At MyPersonalDelivery, we are committed to providing you with a seamless and efficient delivery experience for a wide range of items. Whether you need groceries, documents, electronics, or even furniture, we've got you covered.

Our Services:
We offer a diverse range of delivery services to cater to your unique needs. From same-day delivery for urgent items to scheduled deliveries that fit your convenience, we have the flexibility to meet your busy lifestyle. Our real-time tracking system ensures that you can monitor the status of your delivery every step of the way.

What We Deliver:
Our service is designed to handle various items, including everyday essentials such as groceries and medications. Need to send important documents? No problem, we'll ensure they reach their destination securely. We also specialize in transporting larger items like electronics, clothing, and even furniture. However, please note that we currently do not offer delivery for hazardous materials or items that are extremely fragile and require special handling.

Safety and Care:
Your items' safety is our top priority. We take pride in our secure handling practices to ensure that your deliveries arrive intact. Our contactless delivery option minimizes physical contact, adding an extra layer of safety during these times. We understand that each item is valuable, and you can trust us to treat your belongings with the utmost care.

Why Choose MyPersonalDelivery:
- Wide variety of items delivered
- Flexible delivery options
- Real-time tracking for peace of mind
- Secure handling and contactless delivery
- Reliable service with a commitment to excellence

Whether you need a small package delivered across town or a larger item transported across the city, you can rely on MyPersonalDelivery to provide a reliable, secure, and efficient delivery solution. Your satisfaction is our driving force, and we look forward to serving you with our dedicated and customer-centric approach.

Feel free to ask any questions you may have about our services, and we'll be more than happy to assist you.
"""

# Define the system prompt
system_prompt = f"Act as a customer service chatbot for a delivery service that responds in a gentle way. The service description is delimited by the three backticks ```{service_description}```"
user_prompt = "What benefits does MyPersonalDelivery offer?"

# Get the response to the user prompt
response = get_response_system_user(system_prompt, user_prompt)

print(response)