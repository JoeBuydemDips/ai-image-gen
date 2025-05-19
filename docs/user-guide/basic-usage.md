# Basic Usage Guide

Learn how to use all features of AI Image Generator effectively.

## Interface Overview

The application has a simple two-panel layout:

- **Left Sidebar**: All your controls and settings
- **Main Area**: Where your generated image appears

## Using the Application

### 1. API Key Setup

- Enter your Replicate API key in the sidebar
- The key is stored securely in your session
- Get your key from [Replicate](https://replicate.com/account/api-tokens)

### 2. Writing Prompts

#### Basic Prompt Structure

- Start with the main subject
- Add descriptive details
- Include style and mood
- Example: "A peaceful mountain lake at sunset, with orange clouds reflecting on the water, photorealistic style"

#### Prompt Tips

- Be specific about what you want
- Include lighting and atmosphere
- Mention the style (photorealistic, artistic, etc.)
- Add details about composition

### 3. Image Settings

#### Aspect Ratios

- **1:1** (Square): Good for social media, profile pictures
- **16:9** (Widescreen): Perfect for wallpapers, landscapes
- **4:3** (Standard): Classic photo ratio
- **3:2** (Classic): Traditional photography ratio

#### Output Formats

- **webp**: Best for web use, good quality/size balance
- **png**: Highest quality, larger file size
- **jpg**: Smaller file size, good for photos

#### Quality Settings

- **Output Quality** (1-100)

  - 80-90: Good balance of quality and speed
  - 90-100: Highest quality, slower generation
  - Below 80: Faster but lower quality

- **Safety Tolerance** (1-5)

  - 4: Recommended for general use
  - 5: Strictest filtering
  - 3: More permissive
  - 1-2: Not recommended

- **Prompt Upsampling**
  - Enabled: Better quality, slower generation
  - Disabled: Faster generation, basic quality

### 4. Generating Images

1. Enter your prompt
2. Choose your settings
3. Click "Generate Image"
4. Wait for the image to appear
5. Use the "Download" button to save

### 5. Downloading Images

- Click the "Download" button below the image
- The image saves in your chosen format
- Filename includes the format extension

## Troubleshooting

### Common Issues

1. **API Key Problems**

   - Make sure the key is correct
   - Check your internet connection
   - Verify the key is active

2. **Generation Issues**

   - Try a simpler prompt
   - Check your settings
   - Ensure stable internet connection

3. **Quality Problems**
   - Increase output quality
   - Enable prompt upsampling
   - Try a different aspect ratio

## Best Practices

1. **For Best Results**

   - Use detailed, specific prompts
   - Start with quality at 80-90
   - Keep safety at 4
   - Enable prompt upsampling

2. **For Faster Generation**

   - Use simpler prompts
   - Lower the quality setting
   - Disable prompt upsampling
   - Use webp format

3. **For Highest Quality**
   - Use detailed prompts
   - Set quality to 90-100
   - Enable prompt upsampling
   - Use png format

## Limitations

### Technical Limitations

- Maximum image dimensions are fixed based on aspect ratio
- Generation speed depends on your internet connection and Replicate's servers
- API key is required and subject to Replicate's rate limits
- Images are generated on Replicate's servers, not locally

### Model Limitations

- The model may not always perfectly match your prompt
- Complex scenes might need multiple attempts
- Some artistic styles may be challenging to achieve
- Text in images may not be accurate or readable
- Faces and people may not always be photorealistic

### Usage Limitations

- Commercial usage depends on Replicate's terms of service
- API usage is subject to Replicate's rate limits
- Generated images are not stored on our servers
- Each generation requires an active internet connection

## Frequently Asked Questions

### General Questions

**Q: How long does it take to generate an image?**  
A: Generation time varies based on your settings. Typically:

- Basic settings: 10-20 seconds
- High quality: 20-30 seconds
- With prompt upsampling: 30-40 seconds

**Q: What's the maximum image size?**  
A: The maximum dimensions depend on the aspect ratio:

- 1:1: 1024x1024 pixels
- 16:9: 1024x576 pixels
- 4:3: 1024x768 pixels
- 3:2: 1024x683 pixels

**Q: Can I use the generated images commercially?**  
A: Please check Replicate's terms of service and the Flux 1.1 Pro model's license for commercial usage rights.

### Technical Questions

**Q: Why is my API key not working?**  
A: Common reasons include:

- Incorrect key entered
- Expired or revoked key
- Network connectivity issues
- Rate limiting from Replicate

**Q: What's the difference between the output formats?**  
A: Each format has its strengths:

- webp: Best for web, good compression
- png: Highest quality, no compression
- jpg: Smaller size, good for photos

**Q: What does safety tolerance do?**  
A: It controls content filtering:

- 5: Strictest filtering
- 4: Standard filtering (recommended)
- 3: More permissive
- 1-2: Minimal filtering (not recommended)

### Tips and Tricks

**Q: How can I get better results?**  
A: Try these techniques:

- Be specific in your prompts
- Include style and mood words
- Use quality settings 80-90
- Enable prompt upsampling
- Experiment with different aspect ratios

**Q: What are good prompts to start with?**  
A: Start with these elements:

- Main subject
- Setting or environment
- Lighting and atmosphere
- Style (photorealistic, artistic, etc.)
- Example: "A peaceful mountain lake at sunset, with orange clouds reflecting on the water, photorealistic style"

**Q: How can I speed up generation?**  
A: For faster generation:

- Use simpler prompts
- Lower quality settings (60-70)
- Disable prompt upsampling
- Use webp format
- Ensure stable internet connection

## Next Steps

- Learn about [Advanced Features](advanced-features.md)
- Explore the [API Reference](../api-reference/overview.md)
- Read the [Contributing Guide](../contributing/guide.md)
