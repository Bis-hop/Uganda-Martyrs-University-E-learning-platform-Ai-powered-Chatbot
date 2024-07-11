# # # This files contains your custom actions which can be used to run
# # # custom Python code.
# # #
# # # See this guide on how to implement these action:
# # # https://rasa.com/docs/rasa/custom-actions


# # # This is a simple example for a custom action which utters "Hello World!"

# from excel_data_store_read import DataStore
# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# # #
# # #
# # # class ActionHelloWorld(Action):
# # #
# # #     def name(self) -> Text:
# # #         return "action_hello_world"
# # #
# # #     def run(self, dispatcher: CollectingDispatcher,
# # #             tracker: Tracker,
# # #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# # #
# # #         dispatcher.utter_message(text="Hello World!")
# # #
# # #         return []
# # # from rasa_sdk import Action, Tracker
# # # from rasa_sdk.executor import CollectingDispatcher
# # # from typing import Any, Text, Dict, List

# # # class ActionGreet(Action):
# # #     def name(self) -> Text:
# # #         return "action_greet"

# # #     def run(self, dispatcher: CollectingDispatcher,
# # #             tracker: Tracker,
# # #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

# # #         dispatcher.utter_message(text="Hello! How can I help you?")
# # #         return []
# #here

# # from typing import Any, Text, Dict, List
# # from rasa_sdk import Action, Tracker
# # from rasa_sdk.executor import CollectingDispatcher


# # class ActionHelloWorld(Action):
# #     def name(self) -> Text:
# #         return "action_hello_world"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #         dispatcher.utter_message(text="Hello, world!")
# #         return []


# # class ActionCustomResponse(Action):
# #     def name(self) -> Text:
# #         return "action_custom_response"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #         # Your custom logic to generate a response based on the conversation
# #         response = "This is a custom response!"
# #         dispatcher.utter_message(text=response)
# #         return []


# # class ActionGoodbye(Action):
# #     def name(self) -> Text:
# #         return "action_goodbye"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #         dispatcher.utter_message(text="Goodbye!")
# #         return []


# # from typing import Any, Text, Dict, List
# # from rasa_sdk import Action, Tracker
# # from rasa_sdk.executor import CollectingDispatcher
# # import requests

# # class ActionRespondToGreet(Action):
# #     def name(self) -> Text:
# #         return "action_respond_to_greet"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #         dispatcher.utter_message(template="utter_greet")
# #         return []


# # class ActionRespondToGoodbye(Action):
# #     def name(self) -> Text:
# #         return "action_respond_to_goodbye"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #         dispatcher.utter_message(template="utter_goodbye")
# #         return []


# # class ActionRespondToThanks(Action):
# #     def name(self) -> Text:
# #         return "action_respond_to_thanks"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #         dispatcher.utter_message(template="utter_iamabot")
# #         return []
    

# # def send_message_to_rasa(message):
# #     url = 'http://localhost:5005'
# #     data = {"sender": "user", "message": message}
# #     response = requests.post(url, json=data)
# #     if response.status_code == 200:
# #         return response.json()
# #     else:
# #         return {"error": "Failed to send message to Rasa server"}


# # from typing import Any, Text, Dict, List
# # from rasa_sdk import Action, Tracker
# # from rasa_sdk.executor import CollectingDispatcher
# # import requests


# # class ActionRespondToGreet(Action):
# #     def name(self) -> Text:
# #         return "action_respond_to_greet"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #         dispatcher.utter_message(text="utter_greet")
# #         return []


# # class ActionRespondToGoodbye(Action):
# #     def name(self) -> Text:
# #         return "action_respond_to_goodbye"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #         dispatcher.utter_message(text="utter_goodbye")
# #         return []


# # class ActionRespondToThanks(Action):
# #     def name(self) -> Text:
# #         return "action_respond_to_iamabot"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #         dispatcher.utter_message(text="utter_iamabot")
# #         return []

# # from typing import Any, Text, Dict, List
# # from rasa_sdk import Action, Tracker
# # from rasa_sdk.executor import CollectingDispatcher
# # import requests

# # class ActionRespondToGreet(Action):
# #     def name(self) -> Text:
# #         return "action_respond_to_greet"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #         # Define the greeting message
# #         greeting_message = "Hey! How are you?"

# #         # Send the greeting message to the user
# #         dispatcher.utter_message(text=greeting_message)

# #         return []

# # def send_message_to_rasa(message):
# #     url = 'http://localhost:5005/webhooks/rest/webhook'
# #     data = {"sender": "user", "message": message}
# #     response = requests.post(url, json=data)
# #     if response.status_code == 200:
# #         return response.json()
# #     else:
# #         return {"error": "Failed to send message to Rasa server"}


# # # Example usage
# # response = send_message_to_rasa("Hello")
# # print(response)

# # from typing import Any, Text, Dict, List
# # from rasa_sdk import Action, Tracker
# # from rasa_sdk.executor import CollectingDispatcher
# # import requests


# # class ActionRespondToGreet(Action):
# #     def name(self) -> Text:
# #         return "action_respond_to_greet"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #         # Define the greeting message
# #         greeting_message = "Hey! How are you?"

# #         # Send the greeting message to the user
# #         dispatcher.utter_message(text=greeting_message)

# #         return []


# # def send_message_to_rasa(message):
# #     url = 'http://localhost:5005'
# #     data = {"sender": "user", "message": message}
# #     response = requests.post(url, json=data)
# #     if response.status_code == 200:
# #         return response.json()
# #     else:
# #         return {"error": "Failed to send message to Rasa server"}


# # # Example usage
# # if __name__ == "__main__":
# #     response = send_message_to_rasa("Hello")
# #     print(response)
# # #New

# # from typing import Any, Text, Dict, List
# # from rasa_sdk import Action, Tracker
# # from rasa_sdk.executor import CollectingDispatcher
# # import requests


# # class ActionRespondToGreet(Action):
# #     def name(self) -> Text:
# #         return "action_respond_to_greet"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #         dispatcher.utter_message(template="utter_greet")
# #         return []


# # class ActionRespondToGoodbye(Action):
# #     def name(self) -> Text:
# #         return "action_respond_to_goodbye"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #         dispatcher.utter_message(template="utter_goodbye")
# #         return []


# # class ActionRespondToAffirm(Action):
# #     def name(self) -> Text:
# #         return "action_respond_to_affirm"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #         dispatcher.utter_message(template="utter_happy")
# #         return []


# # class ActionRespondToDeny(Action):
# #     def name(self) -> Text:
# #         return "action_respond_to_deny"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #         dispatcher.utter_message(template="utter_goodbye")
# #         return []


# # class ActionRespondToMoodGreat(Action):
# #     def name(self) -> Text:
# #         return "action_respond_to_mood_great"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #         dispatcher.utter_message(template="utter_happy")
# #         return []


# # class ActionRespondToMoodUnhappy(Action):
# #     def name(self) -> Text:
# #         return "action_respond_to_mood_unhappy"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #         dispatcher.utter_message(template="utter_cheer_up")
# #         dispatcher.utter_message(template="utter_did_that_help")
# #         return []


# # class ActionRespondToBotChallenge(Action):
# #     def name(self) -> Text:
# #         return "action_respond_to_bot_challenge"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #         dispatcher.utter_message(template="utter_iamabot")
# #         return []
    
# # def send_message_to_rasa(message):
# #     url = 'http://localhost:5005'
# #     data = {"sender": "user", "message": message}
# #     response = requests.post(url, json=data)
# #     if response.status_code == 200:
# #         return response.json()
# #     else:
# #         return {"error": "Failed to send message to Rasa server"}


# # # Example usage
# # if __name__ == "__main__":
# #     response = send_message_to_rasa("Hello")
# #     print(response)

# # actions.py
# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import SlotSet, EventType


# class ActionAddMessage(Action):
#     def name(self) -> Text:
#         return "action_add_message"

#     async def run(self, dispatcher: CollectingDispatcher,
#                 tracker: Tracker,
#                 domain: Dict[Text, Any]) -> List[EventType]:
#         # Your custom code here
#         dispatcher.utter_message(text="Message added!")
#         return []


# class ActionAppendEvents(Action):
#     def name(self) -> Text:
#         return "action_append_events"

#     async def run(self, dispatcher: CollectingDispatcher,
#                 tracker: Tracker,
#                 domain: Dict[Text, Any]) -> List[EventType]:
#         # Your custom code here
#         dispatcher.utter_message(text="Events appended!")
#         return []

# from excel_data_store_read import DataStore
# DDDDD
# from data_store import DataStore
# from typing import Any, Text, Dict, List, Union

# from rasa_sdk import Action, Tracker
# from rasa_sdk.events import EventType
# from rasa_sdk.forms import FormAction
# from rasa_sdk.executor import CollectingDispatcher


# class FormDataCollect(FormAction):
#     def name(self) -> Text:
#         return "student_form"

#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         return ["name", "email"]

#     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
#         return {
#             "name": [self.from_text()],
#             "email": [self.from_entity(entity="email")],
#         }

#     def submit(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[EventType]:
#         dispatcher.utter_message(
#             text=f"Here are the information that you provided:\n"
#             f"Name: {tracker.get_slot('name')},\n"
#             f"Email: {tracker.get_slot('email')}\n"
#             f"Do you want to save it?"
#         )
#         return []


# class ActionSaveData(Action):
#     def name(self) -> Text:
#         return "action_save_data"

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any]
#     ) -> List[Dict[Text, Any]]:
#         DataStore(
#             tracker.get_slot("name"),
#             tracker.get_slot("email"),
#         )
#         dispatcher.utter_message(text="Data Stored Successfully.")
#         return []
# DDDDD
# from excel_data_store_read import DataStore
# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# class FormDataCollect(FormAction):
#     def name(self) -> Text:
#         return "student"
#     @staticmethod
#     def required_slots(tracker: "Tracker") -> List[Text]:
#         return ["name","email"]

#     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
#         return {
#         "name":[self.from_text()],
#         "email":[self.from_entity(entity="email")],

#         }

#     def submit(
#         self,
#         dispatcher: "CollectingDispatcher",
#         tracker: "Tracker",
#         domain: Dict[Text, Any],
#     ) -> List[EventType]:

#         dispatcher.utter_message("Here are the information that you provided. Do you want to save it?\nName: {0},\nMobile Number: {1},\nEmail: {2},\nOccupation: {3}".format(
#         tracker.get_slot("name"),
#         tracker.get_slot("email"),


#         ))
#         return []
    

# class ActionSaveData(Action):


#     def name(self) -> Text:
#         return "action_save_data"


# def run(self, dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#     DataStore(
#             tracker.get_slot("name"),
#             tracker.get_slot("email"),
#             )
#     dispatcher.utter_message(text="Data Stored Successfully.")

#     return []
# from transformers import GPT2LMHeadModel, GPT2Tokenizer
# from transformers import pipeline
# from typing import Any, Dict, List, Text
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher


# class GenerateResponse(Action):
#     def name(self) -> Text:
#         return "action_generate_response"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         # Use your LLM here to generate a response based on tracker information
#         generated_response = your_llm_function(
#             tracker.latest_message.get("text"))

#         dispatcher.utter_message(text=generated_response)

#         return []


# generator = pipeline('text-generation', model='gp2')


# def your_llm_function(input_text):
#     return generator(input_text)[0]['generated_text']


# class GenerateResponse(Action):
#     def name(self):
#         return "action_generate_response"

#     def run(self, dispatcher, tracker, domain):
#         input_text = tracker.latest_message.get("text")

#         # Load pre-trained model and tokenizer
#         tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
#         model = GPT2LMHeadModel.from_pretrained('gpt2')

#         # Tokenize input text
#         input_ids = tokenizer.encode(input_text, return_tensors='pt')

#         # Generate response
#         output = model.generate(
#             input_ids, max_length=100, num_return_sequences=1)

#         # Decode and send response
#         generated_response = tokenizer.decode(
#             output[0], skip_special_tokens=True)
#         dispatcher.utter_message(text=generated_response)

#         return []


# NEW NEW NEW 
# from tkinter import Text
# from typing import Any, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from transformers import AutoTokenizer, AutoModelForCausalLM

# response_tokenizer = AutoTokenizer.from_pretrained("gpt2")
# response_model = AutoModelForCausalLM.from_pretrained("gpt2")


# class ActionGenerateResponse(Action):
#     def name(self) -> Text:
#         return "action_generate_response"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         user_message = tracker.latest_message.get("text")
#         inputs = response_tokenizer.encode(user_message, return_tensors="pt")
#         outputs = response_model.generate(
#             inputs, max_length=50, num_return_sequences=1)
#         response = response_tokenizer.decode(
#             outputs[0], skip_special_tokens=True)
#         dispatcher.utter_message(text=response)
#         return []


# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from transformers import pipeline

# # Load Hugging Face models
# qa_pipeline = pipeline('question-answering',
# model='distilbert-base-uncased-distilled-squad')
# generator = pipeline('text-generation', model='gpt2')


# class ActionQuestionAnswering(Action):

#     def name(self) -> str:
#         return "action_question_answering"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: dict) -> list:

#         # Get the latest user message
#         user_message = tracker.latest_message.get('text')

#         # Define context (this could be from previous conversations or a knowledge base)
#         context = "Your predefined context or knowledge base content here."

#         # Get the answer from the QA model
#         answer = qa_pipeline({'question': user_message, 'context': context})[
#             'answer']

#         # Send the answer back to the user
#         dispatcher.utter_message(text=answer)

#         return []


# class ActionGenerateResponse(Action):

#     def name(self) -> str:
#         return "action_generate_response"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: dict) -> list:

#         # Get the latest user message
#         user_message = tracker.latest_message.get('text')

#         # Generate a response
#         response = generator(user_message, max_length=50, num_return_sequences=1)[
#             0]['generated_text']

#         # Send the response back to the user
#         dispatcher.utter_message(text=response)

#         return []






# from typing import Dict, Text, Any, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher


# class ActionResourcesList(Action):

#     def name(self) -> Text:
#         return "action_resources_list"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         covid_resources = {
#             "type": "template",
#             "payload": {
#                 "template_type": "generic",
#                 "elements": [
#                     {
#                         "title": "MBMC",
#                         "subtitle": "FIND BED, SAVE LIFE.",
#                         "image_url": "assets/admissions.jpeg",
#                         "buttons": [
#                             {
#                                 "title": "Hospital Beds Availability",
#                                 "url": "https://www.covidbedmbmc.in/",
#                                 "type": "web_url"
#                             },
#                             {
#                                 "title": "MBMC",
#                                 "type": "postback",
#                                 "payload": "/affirm"
#                             }
#                         ]
#                     },
#                     {
#                         "title": "COVID.ARMY",
#                         "subtitle": "OUR NATION, SAVE NATION.",
#                         "image_url": "static/oxygen-cylinder-55-cft-500x554-500x500.jpg",
#                         "buttons": [
#                             {
#                                 "title": "RESOURCES AVAILABILITY",
#                                 "url": "https://covid.army/",
#                                 "type": "web_url"
#                             },
#                             {
#                                 "title": "COVID ARMY",
#                                 "type": "postback",
#                                 "payload": "/deny"
#                             }
#                         ]
#                     },
#                     {
#                         "title": "Innovate Yourself",
#                         "subtitle": "Get It, Make it.",
#                         "image_url": "static/test.jpg",
#                         "buttons": [
#                             {
#                                 "title": "Innovate Yourself",
#                                 "url": "https://www.innovationyourself.com/",
#                                 "type": "web_url"
#                             },
#                             {
#                                 "title": "Innovate Yourself",
#                                 "type": "postback",
#                                 "payload": "/greet"
#                             }
#                         ]
#                     },
#                     {
#                         "title": "RASA CHATBOT",
#                         "subtitle": "Conversational AI",
#                         "image_url": "assets/Ai head.jpeg",
#                         "buttons": [
#                             {
#                                 "title": "Rasa",
#                                 "url": "https://www.rasa.com",
#                                 "type": "web_url"
#                             },
#                             {
#                                 "title": "Rasa Chatbot",
#                                 "type": "postback",
#                                 "payload": "/greet"
#                             }
#                         ]
#                     }
#                 ]
#             }
#         }

#         print("Sending covid_resources: ", covid_resources)  # Debugging line

#         dispatcher.utter_message(attachment=covid_resources)
#         return []


#START

# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher


# class ActionShowCarousel(Action):

#     def name(self) -> Text:
#         return "action_show_carousel"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Sample data for carousel
#         items = [
#             {
#                 "title": "Course 1",
#                 "subtitle": "This is an introductory course on Python.",
#                 "image_url": "http://example.com/course1.jpg",
#                 "buttons": [
#                     {"title": "View Course",
#                         "url": "http://example.com/course1", "type": "web_url"},
#                     {"title": "Enroll", "payload": "/enroll_course_1"}
#                 ]
#             },
#             {
#                 "title": "Course 2",
#                 "subtitle": "Advanced Java programming concepts.",
#                 "image_url": "http://example.com/course2.jpg",
#                 "buttons": [
#                     {"title": "View Course",
#                         "url": "http://example.com/course2", "type": "web_url"},
#                     {"title": "Enroll", "payload": "/enroll_course_2"}
#                 ]
#             },
#             {
#                 "title": "Course 3",
#                 "subtitle": "Learn Data Science with R.",
#                 "image_url": "http://example.com/course3.jpg",
#                 "buttons": [
#                     {"title": "View Course",
#                         "url": "http://example.com/course3", "type": "web_url"},
#                     {"title": "Enroll", "payload": "/enroll_course_3"}
#                 ]
#             }
#         ]

#         # Construct carousel elements
#         carousel_elements = []
#         for item in items:
#             element = {
#                 "title": item["title"],
#                 "subtitle": item["subtitle"],
#                 "image_url": item["image_url"],
#                 "buttons": [
#                     {
#                         "type": "web_url",
#                         "url": button["url"],
#                         "title": button["title"]
#                     } if button.get("url") else {
#                         "type": "postback",
#                         "payload": button["payload"],
#                         "title": button["title"]
#                     } for button in item["buttons"]
#                 ]
#             }
#             carousel_elements.append(element)

#         # Send carousel message
#         dispatcher.utter_message(attachment={
#             "type": "template",
#             "payload": {
#                 "template_type": "generic",
#                 "elements": carousel_elements
#             }
#         })

#         return []

#NAYE
# 
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher


# class ActionShowCarousel(Action):

#     def name(self) -> Text:
#         return "action_show_carousel"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         test_carousel = {
#             "type": "template",
#             "payload": {
#                 "template_type": "generic",
#                 "elements": [
#                     {
#                         "title": "Title",
#                         "subtitle": "Subtitle",
#                         "image_url": "/static/images/test.png",
#                         "buttons": [
#                             {
#                                 "title": "Link name",
#                                 "url": "http://link.url",
#                                 "type": "web_url"
#                             },
#                             {
#                                 "title": "postback name",
#                                 "type": "postback",
#                                 "payload": "/greet"
#                             }
#                         ]
#                     },
#                     {
#                         "title": "Title",
#                         "subtitle": "Subtitle",
#                         "image_url": "/static/images/test.png",
#                         "buttons": [
#                             {
#                                 "title": "Link name",
#                                 "url": "http://link.url",
#                                 "type": "web_url"
#                             },
#                             {
#                                 "title": "postback name",
#                                 "type": "postback",
#                                 "payload": "/greet"
#                             }
#                         ]
#                     }
#                 ]
#             }
#         }

#         dispatcher.utter_message(attachment=test_carousel)
#         return []


from typing import Any, Coroutine, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


# class ActionShowCarousel(Action):

#     def name(self) -> Text:
#         return "action_show_carousel"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         test_carousel = {
#             "type": "template",
#             "payload": {
#                 "template_type": "generic",
#                 "elements": [
#                     {
#                         "title": "Title",
#                         "subtitle": "Subtitle",
#                         "image_url": "/static/images/test.png",
#                         "buttons": [
#                             {
#                                 "title": "Link name",
#                                 "url": "http://link.url",
#                                 "type": "web_url"
#                             },
#                             {
#                                 "title": "postback name",
#                                 "type": "postback",
#                                 "payload": "/greet"
#                             }
#                         ]
#                     },
#                     {
#                         "title": "Title",
#                         "subtitle": "Subtitle",
#                         "image_url": "/static/images/test.png",
#                         "buttons": [
#                             {
#                                 "title": "Link name",
#                                 "url": "http://link.url",
#                                 "type": "web_url"
#                             },
#                             {
#                                 "title": "postback name",
#                                 "type": "postback",
#                                 "payload": "/greet"
#                             }
#                         ]
#                     }
#                 ]
#             }
#         }

#         dispatcher.utter_message(attachment=test_carousel)
#         return []

# class ActionStartSession(Action):
#     def name(self) -> Text:
#         return "action_start_session"
    
#     def run(
#         self,
#         dispatecher: "CollectingDispatcher",
#         tracker: Tracker,
#         domain: "DomainDict",
#     ) -> List[Dict[Text, Any]]:
#         return [SlotSet("is_logged_in",True)]

import logging


class ActionCarousel(Action):
    def name(self) -> Text:
        return "action_show_carousel"

    def run(self, dispatcher, tracker: Tracker, domain: DomainDict) -> List[Dict[Text, Any]]:
        logging.info("Executing action_show_carousel")
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Carousel 1",
                        "subtitle": "$10",
                        "image_url": "assets/blue_head.jpg",
                        "buttons": [
                            {
                                "title": "Hi",
                                "payload": "Hi",
                                "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Carousel 2",
                        "subtitle": "$20",
                        "image_url": "assets/blue_head.jpg",
                        "buttons": [
                            {
                                "title": "Hello",
                                "payload": "Hello",
                                "type": "postback"
                            }
                        ]
                    }
                ]
            }
        }
        dispatcher.utter_message(json_message=message)
        return []
