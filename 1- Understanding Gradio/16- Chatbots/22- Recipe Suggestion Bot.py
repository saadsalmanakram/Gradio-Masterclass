import gradio as gr

def recipe_suggestion(message, history):
    recipes = {
        "egg": "You can make an omelette or scrambled eggs.",
        "tomato": "How about making a tomato soup or a salad?",
        "chicken": "Consider making chicken curry or grilled chicken.",
        "potato": "Potato chips or mashed potatoes are great options."
    }
    for ingredient in message.lower().split(","):
        ingredient = ingredient.strip()
        if ingredient in recipes:
            return recipes[ingredient]
    return "I don't have a recipe for that ingredient."

gr.ChatInterface(recipe_suggestion).launch()
