import openai
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("OPENAI_API")


class Chatbot:
    def __init__(self):
        openai.api_key = api_key

    def get_response(self, user_input):
        # parameters:
        #   engine: str of the AI model that is being used.
        #   prompt: user input
        #   max_tokens, set to 4000. This will be the amount of words that it will return, the maximum is 4080
        #   temperature: 0 to 1, closer to 0 will produce more accurate answers, but will be less diverse
        #                   higher temperature will be more diverse, but less accurate
        # chained with .choice
        #       gives a list, need the first index of that list and extract the text property from it
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt= user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    test = Chatbot()
    response_test = test.get_response("Tell me a joke")
    print(response_test)
