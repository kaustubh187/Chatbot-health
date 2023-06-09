from flask import Flask, request, jsonify,render_template
import openai


#Open AI key
openai.api_key = "very-secret-key"


app = Flask(__name__)

# Chat page
@app.route('/')
def home():
    return render_template('home.html')



#Response Message
@app.route('/chat', methods=['POST'])
def chat():
    #Getting the response
    data = request.get_json()

    #Storing the user message
    user_message = data['message']
    
    # Assigning the roles and setting the context of the chat
    messages = [
    {"role": "system", "content": "To serve as helpdesk for health conditions and severity of condition."},]
    
    # Appending the user message
    messages.append(
            {"role": "user", "content": user_message},
        )
    # Process the user's message and generate a bot response
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages) 

    # 
    bot_response = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": bot_response})
    response = {
        'response': bot_response
    }
    return jsonify(response)


app.run(debug=True)
