"""AI generated insights into vehicle choice"""
import cohere
from keys import COHERE_API_KEY

co = cohere.Client(COHERE_API_KEY)

def generate_msg(car, comment):
    uses = ', '.join(car["uses"])
    if comment != "": 
        return co.generate(
        model='command-xlarge-nightly',
        prompt=f'Sell a buyer a Ford {car["name"]} using these characteristics that they want in a car: {uses}. Directly address the buyer with \"you\". Use this pronoun for yourself: \"we\". Try to write an imaginary scenario that they could picture in their heads that would make them want to buy the car. Be sure to consider what they wrote here: {comment}',
        max_tokens=902,
        temperature=0.9,
        k=0,
        p=0.75,
        stop_sequences=[],
        return_likelihoods='NONE').generations[0].text
    return co.generate(
    model='command-xlarge-nightly',
    prompt=f'Think of a story that someone would tell a car dealer about their ideal car. Use personal pronouns \"I\", \"we\" and tie in personal facts that contribute to the type and features of the car they want.Think of a story that someone would tell a car dealer about their ideal car. Use personal pronouns \"I\", \"we\" and tie in personal facts that contribute to the type and features of the car they want. It\'s a {car["name"]}.',
    max_tokens=902,
    temperature=0.9,
    k=0,
    p=0.75,
    stop_sequences=[],
    return_likelihoods='NONE').generations[0].text
