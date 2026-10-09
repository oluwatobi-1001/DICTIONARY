dictionary = {
    "apple": "A round fruit that is usually red, green, or yellow.",
    "brave": "Having courage and not being afraid.",
    "candle": "A stick of wax with a wick that produces light when burned.",
    "dance": "To move the body rhythmically, usually to music.",
    "eagle": "A large bird of prey with a powerful beak and sharp claws.",
    "family": "A group of people related to one another.",
    "garden": "A piece of land where plants and flowers are grown.",
    "happy": "Feeling or showing pleasure and joy.",
    "island": "A piece of land completely surrounded by water.",
    "journey": "The act of travelling from one place to another.",

    "knowledge": "Information and understanding gained through learning or experience.",
    "language": "A system of words and symbols used for communication.",
    "mountain": "A very high natural elevation of the earth's surface.",
    "nature": "The physical world and everything that exists in it.",
    "ocean": "A very large body of salt water.",
    "peace": "A state of calm and freedom from conflict.",
    "question": "A sentence used to ask for information.",
    "river": "A large natural stream of flowing water.",
    "school": "A place where people go to learn.",
    "teacher": "A person who teaches others.",

    "umbrella": "An object used to protect someone from rain or sunlight.",
    "victory": "Success in a competition, battle, or struggle.",
    "window": "An opening in a wall fitted with glass.",
    "youth": "The period of life when a person is young.",
    "zealous": "Showing great energy and enthusiasm for something.",
    "ability": "The power or skill to do something.",
    "beautiful": "Pleasing to the senses or mind.",
    "courage": "The ability to face fear or difficulty.",
    "delight": "Great pleasure or happiness.",
    "education": "The process of gaining knowledge and skills.",

    "freedom": "The power or right to act and speak without unnecessary restrictions.",
    "generous": "Willing to give or share freely.",
    "honest": "Truthful and sincere.",
    "imagination": "The ability to create ideas or pictures in the mind.",
    "justice": "Fair treatment according to what is right.",
    "kindness": "The quality of being friendly and helpful.",
    "liberty": "The state of being free.",
    "miracle": "An extraordinary event that seems impossible or unexpected.",
    "necessary": "Needed or required.",
    "opportunity": "A suitable chance to do or achieve something.",

    "patience": "The ability to wait calmly without becoming annoyed.",
    "quality": "The standard or level of excellence of something.",
    "respect": "A feeling of admiration or consideration for someone or something.",
    "success": "The achievement of a desired goal.",
    "talent": "A natural ability or skill.",
    "understanding": "The ability to understand or comprehend something.",
    "valuable": "Worth a lot or considered important.",
    "wisdom": "The ability to make good decisions based on knowledge and experience.",
    "adventure": "An exciting or unusual experience.",
    "brilliant": "Very intelligent, impressive, or excellent.",

    "creative": "Having the ability to produce new and original ideas.",
    "determination": "The quality of being firmly decided to achieve something.",
    "excellent": "Extremely good or of very high quality.",
    "friendship": "A relationship between people who care about each other.",
    "gratitude": "The feeling of being thankful.",
    "happiness": "The state of feeling happy.",
    "inspiration": "Something that gives someone the idea or motivation to create or do something.",
    "joyful": "Feeling or expressing great happiness.",
    "leadership": "The ability to guide or influence others.",
    "motivation": "The reason or desire that makes someone want to do something.",
    "noble": "Having good moral qualities and high character.",
    "optimistic": "Expecting good things to happen.",
    "powerful": "Having great strength, influence, or ability.",
    "responsible": "Having a duty to take care of something or someone.",
    "strength": "The quality of being physically or mentally strong.",
    "trust": "A strong belief that someone or something is reliable.",
    "unique": "Being the only one of its kind.",
    "volunteer": "A person who willingly offers to do something without being forced.",
    "wonderful": "Extremely good, enjoyable, or impressive.",
    "achievement": "Something successfully accomplished.",

    "balance": "A state in which different parts are equal or properly arranged.",
    "communication": "The process of sharing information, ideas, or feelings.",
    "discipline": "The ability to control yourself and follow rules or plans.",
    "energy": "The ability to do work or cause change.",
    "focus": "The ability to concentrate attention on something.",
    "growth": "The process of becoming larger, stronger, or more developed.",
    "hope": "A feeling of expecting or wanting something good to happen.",
    "innovation": "A new idea, method, or invention.",
    "knowledgeable": "Having a lot of knowledge about something.",
    "learning": "The process of gaining knowledge or skills.",

    "mindful": "Being aware and thoughtful about what is happening.",
    "progress": "Movement toward a better or more developed state.",
    "resourceful": "Good at finding ways to solve problems.",
    "smart": "Having a good ability to learn, understand, or solve problems.",
    "thoughtful": "Showing care and consideration for others.",
    "unity": "The state of being joined together.",
    "vision": "An idea or picture of what you want to achieve in the future.",
    "ambition": "A strong desire to achieve something.",
    "confidence": "Belief in your own abilities.",
    "empathy": "The ability to understand another person's feelings.",
     "curious": "Wanting to learn or know more about something.",
    "perseverance": "The ability to continue trying even when something is difficult."
}
print("Welcome to Patience's Dictionary!")
print("\n")
print("Here are some words you can look up:")

for word in dictionary:
    print("-", word)
while True:
    word = input("\nEnter a word to find its meaning: ").lower()
    # /n is used to create a new line in the output, making it easier to read and separate the input prompt from the previous output. The .lower() method is used to convert the user's input to lowercase, ensuring that the word can be found in the dictionary regardless of how the user types it (e.g., "Apple", "APPLE", or "apple" will all be treated as "apple").
    
    # the use of break statement is to exit the loop when the user types 'exit'

    if word in dictionary:
        print("Meaning:", dictionary[word])
    else:
        print("Sorry, that word is not in the dictionary.")
    leave= input("Do you want to look up another word? (1/0), 1 for yes, 0 for no: ")
    if leave.lower() != "1":
        print("Goodbye!")
        break
    elif leave.lower() == "1":
        continue
    # continue is a fixed statement that skips the rest of the code in the loop and goes back to the beginning of the loop to ask for another word