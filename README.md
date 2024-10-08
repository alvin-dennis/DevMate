# DevMate

DevMate is a chatbot that assists developers in finding the code they need. Built using Python, Pathway, OpenAI, and Streamlit, DevMate utilizes advanced language models and real-time data to generate accurate and relevant code snippets. With its user-friendly interface, developers can easily enter their queries and receive customized code solutions. Whether you're a beginner or an experienced developer, DevMate is here to streamline your coding process.

## Live Site

https://devmate.streamlit.app/

## Preview
<img src="https://github.com/alvin-dennis/DevMate/blob/main/assets/devmatedemo.png" alt="Demo Image" width="1000" height="1000"/>

## Features

- Code snippet generation: DevMate can generate code snippets based on user queries, making it easier for developers to find the code they need.
- Python integration: DevMate seamlessly integrates with Python projects, allowing for easy code integration.
- Pathway library: DevMate leverages the Pathway library to enhance code generation capabilities with live data and real-time pipelines.
- OpenAI integration: By utilizing OpenAI's powerful language models, DevMate provides accurate and relevant code snippets.
- Streamlit interface: DevMate's user-friendly interface is built using Streamlit, making it effortless to interact with the chatbot.

## Getting Started

To get started with DevMate, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/alvin-dennis/DevMate.git
    ```

2. Create and activate a virtual environment:

    ```shell
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Rename `.env.example` file to `.env` and insert the required credentials

5. Run Pathway Engine :
    ```bash
    python3 app.py
    ```

6. Run the Streamlit app:

    ```bash
    streamlit run main.py
    ```

7. Access the app in your browser at `http://localhost:8501`

## Libraries Used

DevMate utilizes the following libraries:

- Python
- Pathway
- Requests
- OpenAI
- Streamlit



## Usage

1. Enter your query in the input field.
2. Click the "Send" button to generate a code snippet based on your query.
3. Copy the generated code snippet and use it in your project.


## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/alvin-dennis/DevMate/blob/main/LICENSE) file for more information.
