# Installation Guide

This guide will help you get AI Image Generator up and running on your system.

## Prerequisites

Before installing AI Image Generator, make sure you have:

- Python 3.8 or higher
- pip (Python package installer)
- Git (optional, for development)

## Installation Steps

1. Clone the repository (optional):

   ```bash
   git clone https://github.com/JoeBuydemDips/ai-image-gen.git
   cd ai-image-gen
   ```

2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install the package:
   ```bash
   pip install -r requirements.txt
   ```

## Verifying the Installation

To verify that AI Image Generator is installed correctly, run:

```bash
python -c "import ai_image_gen; print(ai_image_gen.__version__)"
```

You should see the version number printed to the console.

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

## Next Steps

- Check out the [Quick Start Guide](quickstart.md) to begin using AI Image Generator
- Read the [Basic Usage](user-guide/basic-usage.md) documentation
- Explore the [API Reference](api-reference/overview.md)

## Troubleshooting

If you encounter any issues during installation:

1. Make sure all prerequisites are met
2. Check that your Python version is compatible
3. Verify your internet connection
4. Ensure you have the necessary permissions

For additional help, please:

- Check the [FAQ](../user-guide/faq.md)
- Open an [issue](https://github.com/JoeBuydemDips/ai-image-gen/issues)
- Join our community discussions
