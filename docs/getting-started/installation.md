# Installation Guide

Get AI Image Generator up and running in just a few steps.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Quick Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/JoeBuydemDips/ai-image-gen.git
   cd ai-image-gen
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Getting Your API Key

1. Go to [Replicate](https://replicate.com/account/api-tokens)
2. Sign in or create an account
3. Generate a new API token
4. Copy the token - you'll need it when running the application

## Running the Application

Start the application with:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

## Next Steps

- Check out the [Quick Start Guide](quickstart.md) to generate your first image
- Read the [Basic Usage](../user-guide/basic-usage.md) guide for detailed instructions

## Configuration

AI Image Generator uses environment variables and Streamlit's built-in configuration system. The main configuration is handled through:

1. **Replicate API Key**:

   - You can set it as an environment variable:
     ```bash
     export REPLICATE_API_TOKEN="your-api-key"
     ```
   - Or enter it directly in the application's sidebar when running

2. **Application Settings**:
   The following settings can be configured through the application's interface:

   - Aspect ratio (1:1, 16:9, 4:3, 3:2)
   - Output format (webp, png, jpg)
   - Output quality (1-100)
   - Safety tolerance (1-5)
   - Prompt upsampling (enabled/disabled)

3. **Streamlit Configuration**:
   The application uses Streamlit's default configuration. You can customize Streamlit's behavior by creating a `.streamlit/config.toml` file in your project directory:
   ```toml
   [theme]
   primaryColor = "#4B8BBE"
   backgroundColor = "#FFFFFF"
   secondaryBackgroundColor = "#F0F2F6"
   textColor = "#262730"
   font = "sans serif"
   ```

## Troubleshooting

If you encounter any issues during installation:

1. Make sure all prerequisites are met
2. Check that your Python version is compatible
3. Verify your internet connection
4. Ensure you have the necessary permissions

For additional help, please:

- Check the [Basic Usage Guide](../user-guide/basic-usage.md) for troubleshooting tips
- Open an [issue](https://github.com/JoeBuydemDips/ai-image-gen/issues) if you need help
