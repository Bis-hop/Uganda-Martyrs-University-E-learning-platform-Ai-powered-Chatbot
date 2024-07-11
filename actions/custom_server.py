# # custom_server.py
# from sanic import Sanic
# from sanic.response import json
# from rasa.core.run import configure_app
# from rasa.core import server


# def custom_add_message(request, conversation_id):
#     # Implement your custom logic here
#     return json({"status": "Message added!"})


# def custom_append_events(request, conversation_id):
#     # Implement your custom logic here
#     return json({"status": "Events appended!"})


# def main():
#     app = Sanic("custom_rasa_server")
#     configure_app(app)

#     # Add custom endpoints
#     app.post("/conversations/<conversation_id:path>/messages")(custom_add_message)
#     app.post(
#         "/conversations/<conversation_id:path>/tracker/events")(custom_append_events)

#     # Run the app
#     app.run(host="0.0.0.0", port=5005)


# if __name__ == "__main__":
#     main()
