from get_response import get_response

# Example tickets and their extracted entities for the few-shot prompt
ticket_1 = "Hi, my name is John Smith. I purchased your XYZ Smartphone two weeks ago, but the battery drains within a couple of hours even when I'm not using it. Could you assist me with this issue?"
entities_1 = """* Customer Details:
  - Name: John Smith
* Product/Service Mentions:
  - Product: XYZ Smartphone"""

ticket_2 = "Hello, this is Emily Johnson. I subscribed to your FastNet internet service last month, but the connection keeps dropping every evening. I would appreciate it if someone could look into this."
entities_2 = """* Customer Details:
  - Name: Emily Johnson
* Product/Service Mentions:
  - Service: FastNet (internet service)"""

ticket_3 = "Good afternoon, my name is Michael Brown. I ordered a PowerMax Laptop from your online store, and it arrived with a cracked screen. I would like to request a replacement as soon as possible."
entities_3 = """* Customer Details:
  - Name: Michael Brown
* Product/Service Mentions:
  - Product: PowerMax Laptop"""

# New ticket to extract entities from
ticket_4 = "Greetings, I am facing technical difficulties with your software, ABC Editor. My name is Sarah Lee, and I recently upgraded to the latest version. However, whenever I try to save my work, the software crashes. Can you please help me resolve this problem?"

# Craft a few-shot prompt to get the ticket's entities
prompt = f"""
 Ticket: {ticket_1} Entities: {entities_1}
 Ticket: {ticket_2} Entities: {entities_2}
 Ticket: {ticket_3} Entities: {entities_3}
 Ticket: {ticket_4} Entities:
"""

response = get_response(prompt)

print("Ticket: \n", ticket_4)
print("Entities: \n", response)
