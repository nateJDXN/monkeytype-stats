# MonkeyType Stats

Welcome to the MonkeyType Stats project! This tool fetches and displays your typing statistics from the MonkeyType API on your GitHub README.

## Project Overview

The primary goal of this project is to automate the retrieval of typing statistics from the MonkeyType platform and update them in a structured format within the README file. It also served as a project to play with GitHub Actions. 

## Features

- **Fetch Typing Statistics**: Automatically retrieves the number of completed tests and personal bests for 15, 30, and 60-second typing tests.
- **Display Personal Bests**: Shows your Words Per Minute (WPM), accuracy, and difficulty level for each test duration.
- **Automated README Update**: Updates the README file with the latest statistics, ensuring your progress is always up-to-date.

## Roadmap

- [x] Add cron job to schedule commits
- [ ] Add option to use embedded tool

## Setup Instructions

1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/yourusername/monkeytype-stats.git
   cd monkeytype-stats
   ```

2. **Install Dependencies**: 
   Ensure you have Python installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables**: 
   Create a `.env` file in the root directory and add your MonkeyType API key:
   ```
   MONKEYTYPE_API_KEY=your_api_key_here
   ```

4. **Add Markdown markers**
    
    Add `<!--- START --->` and `<!--- END --->` to your README where you want the add-on to live.

5. **Run the Script**: 
   Execute the script to fetch and update your stats:
   ```bash
   python get-stats.py
   ```

## Notes

This repo can serve as a template for your own README. I would recommend checking out the official [documentation](https://docs.github.com/en/account-and-profile/how-tos/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme) to learn how to create your own README. 