# 📊 Pixela Habit Tracker

A command-line tool to log daily work hours to a [Pixela](https://pixe.la) habit-tracking graph. Built as part of Angela Yu's 100 Days of Python Bootcamp (Day 37), with a modification to automatically retry failed posts.

## ✨ Features

- Prompts for hours worked today and posts them to your Pixela graph
- Automatically retries failed posts (up to 10 attempts, 2 seconds apart) instead of failing silently
- Lets you update today's entry after a successful post

## 🔧 Modification from the original course project

The base course project sends a single POST request. This version wraps the POST in a retry loop, since Pixela's API can occasionally return a transient failure — useful when running the script unattended or on a flaky connection.

## 🚀 Setup

1. Create a free account and graph on [Pixela](https://pixe.la).
2. Install dependencies:
   ```bash
   pip install requests
   ```
3. Set your credentials as environment variables:
   - **Windows (Command Prompt):** `set PIXELA_TOKEN=your_secret_token_here`
   - **Mac/Linux:** `export PIXELA_TOKEN="your_secret_token_here"`
4. Run the script:
   ```bash
   python pixela_tracker.py
   ```

## 🌐 Embedding Your Tracker

Copy the code below to display your live graph on your personal portfolio:

```html
<iframe src="https://pixe.la/v1/users/komalraradhya/graphs/graph1.html" width="100%" height="200" frameborder="0"></iframe>
```

## 📝 Notes

- This is a learning project from Angela Yu's Python Bootcamp.
- If a post fails after all retry attempts, check your token, username, and graph ID.
- Never commit your Pixela token to GitHub — use environment variables as shown above.
