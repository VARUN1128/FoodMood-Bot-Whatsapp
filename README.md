# 🍽️ FoodMood-Bot

**FoodMood-Bot** is a WhatsApp bot powered by Flask, Twilio, and OpenAI, developed by HarshitaDS in June 2024. It suggests recipes based on the user's mood, providing brief, easy-to-follow instructions with ingredients and preparation time.

## Features

- 🌟 **Mood-Based Food Suggestions**: Get recipe recommendations based on your current mood.
- 📋 **Brief Recipes**: Each recipe is concise (not more than 1400 characters) and includes ingredients and preparation time.
- 👫 **Portion Size**: Ingredients list is prepared for 2 people.
- 🍽️ **Personalized Assistance**: Responds to thank you messages with amazing food-related quotes and offers further assistance.
- 🖼️ **Image Generation**: Generate images related to your query by starting your message with `/img`.

## How It Works

1. **Mood Detection**: The bot asks for your current mood and suggests a suitable recipe.
2. **Recipe Delivery**: Provides a brief recipe with a list of ingredients and the preparation time.
3. **Portion Control**: All recipes are tailored for 2 people.
4. **Image Generation**: Start your message with `/img` to receive a generated image related to your query.

## Example Interaction


User: I'm feeling happy today!
FoodMood-Bot: That's wonderful! How about celebrating with a refreshing fruit salad? 🍓🍊 Here's a quick recipe:

Ingredients:

- 1 cup strawberries, sliced
- 1 orange, peeled and segmented
- 1 apple, diced
- 1 tablespoon honey
- 1 tablespoon lemon juice

**Preparation Time:** 10 minutes

1. In a large bowl, combine the strawberries, orange segments, and apple.
2. Drizzle with honey and lemon juice.
3. Toss gently to mix. Enjoy your refreshing fruit salad!

User: Thank you!
FoodMood-Bot: "One cannot think well, love well, sleep well, if one has not dined well." - Virginia Woolf. I'm here for any further assistance you may need!


## Technologies Used

- **Flask**: For creating the web application.
- **Twilio**: For WhatsApp messaging API.
- **OpenAI**: For intelligent responses and mood analysis.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/HarshitaDS/FoodMood-Bot.git
    cd FoodMood-Bot
    ```
2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up your environment variables:
    - `TWILIO_ACCOUNT_SID`
    - `TWILIO_AUTH_TOKEN`
    - `OPENAI_API_KEY`

5. Run the Flask application:
    ```bash
    python run.py
    ```

## Usage

- Initiate a conversation with the bot on WhatsApp.
- Provide your current mood when prompted.
- Receive a personalized recipe suggestion.
- Start your message with `/img` to generate an image related to your query.
- Enjoy your meal!

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

Developed by Varun. For any inquiries, please reach out via GitHub.

---

Enjoy ur Meals! 🍴
