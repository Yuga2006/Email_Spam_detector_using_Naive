
---

# Email Spam Detection Model

## Overview

This project provides a machine learning model to classify emails as spam or ham (non-spam). The model uses a Naive Bayes classifier trained on a dataset of emails. It also includes functionality to integrate with Gmail for live email classification.

## Contents

- `spam_model.pkl`: The trained Naive Bayes model.
- `tfidf_vectorizer.pkl`: The TF-IDF vectorizer used for feature extraction.
- `email_spam_detection.py`: Python script for email classification.
- `credentials.json`: OAuth 2.0 credentials for Gmail API (replace with your own).
- `token.pickle`: Token file for storing OAuth 2.0 credentials (generated automatically).

## Setup

### Prerequisites

1. **Python 3.x**: Ensure you have Python 3.x installed.
2. **Required Libraries**: Install the required Python libraries using pip:

   ```bash
   pip install pandas scikit-learn gradio google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```

### Google Cloud Setup

1. **Create a Google Cloud Project**:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or select an existing one.
   - Enable the Gmail API for your project.

2. **Create OAuth 2.0 Credentials**:
   - Navigate to **APIs & Services > Credentials**.
   - Click **Create Credentials** and select **OAuth 2.0 Client IDs**.
   - Set the application type to **Desktop app** (or **Web application** if applicable).
   - Download the `credentials.json` file and place it in the project directory.

### Running the Spam Detection Script

1. **Train the Model** (if not already trained):
   Ensure you have a CSV file with email data (e.g., `email.csv`). Modify the `email_spam_detection.py` script to include your training code if you need to retrain the model.

2. **Run the Script**:
   Execute the script to authenticate with Gmail and classify emails:

   ```bash
   python email_spam_detection.py
   ```

### Integration with Gmail

The script will authenticate using OAuth 2.0 and fetch emails from your Gmail account. It classifies the emails using the trained spam detection model.

### Usage

1. **Authenticate with Gmail**:
   On the first run, the script will prompt you to authenticate and authorize access to your Gmail account. Follow the instructions in the browser to grant permissions.

2. **Email Classification**:
   The script fetches emails from your Gmail account and classifies them as spam or ham. It prints the email body and its classification.

## Example Output

```
Email Body:
Congratulations! You've won a $1,000 gift card. Click here to claim your prize now!
Classification: Spam

Email Body:
Hey, are we still meeting for dinner tomorrow at 7 PM?
Classification: Ham
```

## Notes

- Ensure that your `credentials.json` file is kept secure and not shared publicly.
- The `token.pickle` file is automatically created after the first authentication and stores your OAuth 2.0 credentials.
- For production use, handle pagination in Gmail API responses and improve error handling.

---

Feel free to modify and expand this README based on your specific requirements and project details.
