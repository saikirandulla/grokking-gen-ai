This script scrapes job descriptions with MT4 tag from Linkedin. It currently only works for some job listings. 

To run the script, install the required packages by `requirements.txt` file:

1. Save it in the same directory as your Python script.
2. Open a terminal or command prompt.
3. Navigate to the directory containing your script and the `requirements.txt` file.
4. Run the following command to install the required packages:

   ```
   pip install -r requirements.txt
   ```

This will install the specified versions of requests and beautifulsoup4. The csv module will already be available as part of your Python installation.

Remember, it's a good practice to use a virtual environment for your projects. You can create one using:

```
python -m venv env
```

And activate it with:

```
source env/bin/activate  # On Unix or MacOS
env\Scripts\activate.bat  # On Windows
```

Then install the requirements and run your script within this environment. This helps keep your project dependencies isolated from your global Python installation.