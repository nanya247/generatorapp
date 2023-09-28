from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key here
OPENAI_API_KEY = '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'
openai.api_key = OPENAI_API_KEY

@app.route('/', methods=['GET', 'POST'])
def index():
    generated_content = None
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = openai.Completion.create(
            engine="davinci",  # You can choose other engines as needed
            prompt=prompt,
            max_tokens=50,  # Adjust the max tokens as needed
            n=1,
            stop=None,
        )
        generated_content = response.choices[0].text

    return render_template('generationapp.html', generated_content=generated_content)

if __name__ == '__main__':
    app.run(debug=True)
