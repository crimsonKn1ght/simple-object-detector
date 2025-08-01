# Real-Time Object Detection

A web-based real-time object detection application powered by TensorFlow.js and the Coco-SSD model. Detect objects through your webcam directly in the browser with no server required.

## Features

- 🎥 **Real-time detection** - Live object detection through your webcam
- 🏷️ **80+ object classes** - Detects people, animals, vehicles, furniture, and more
- 🎯 **Bounding boxes** - Visual indicators showing detected objects with confidence scores
- 📱 **Mobile friendly** - Responsive design that works on desktop and mobile devices
- 🌙 **Dark mode support** - Automatic dark/light theme detection
- 🚀 **No installation required** - Runs entirely in the browser

## Demo

Simply open the HTML file in any modern web browser and click "Start Webcam" to begin detecting objects in real-time.

## How It Works

The application uses:
- **TensorFlow.js** - Machine learning library for JavaScript
- **Coco-SSD** - Pre-trained object detection model
- **WebRTC** - For accessing the device camera
- **Canvas API** - For drawing bounding boxes and labels

## Supported Objects

The Coco-SSD model can detect 80 different object classes including:
- People and body parts
- Animals (cats, dogs, birds, etc.)
- Vehicles (cars, bikes, trucks, etc.)
- Household items (chairs, tables, TVs, etc.)
- Food items (pizza, banana, wine glass, etc.)
- And many more!

## Browser Requirements

- Modern web browser with WebRTC support (Chrome, Firefox, Safari, Edge)
- Camera/webcam access
- JavaScript enabled

## Usage

1. Open `simple-detector.html` in your web browser
2. Click "Start Webcam" button
3. Allow camera access when prompted
4. Watch as objects are detected and highlighted in real-time
5. Click "Stop Webcam" to end the session

## Privacy

- All processing happens locally in your browser
- No data is sent to external servers
- Camera feed is not recorded or stored

## Technical Details

- **Model**: Coco-SSD (Common Objects in Context - Single Shot MultiBox Detector)
- **Framework**: TensorFlow.js
- **Styling**: Tailwind CSS
- **Performance**: Optimized for real-time detection with requestAnimationFrame

## File Structure

```
├── simple-detector.html          # Main application file
├── README.md                     # This file
└── LICENSE
```

## Contributing

Feel free to fork this project and submit pull requests for improvements such as:
- Additional model options
- Performance optimizations
- UI/UX enhancements
- Mobile-specific features

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Troubleshooting

**Camera not working?**
- Ensure you've granted camera permissions
- Try using HTTPS (required for camera access on many browsers)
- Check if another application is using the camera

**Poor detection performance?**
- Ensure good lighting conditions
- Keep objects at a reasonable distance from the camera
- Try using a device with better processing power

**Model loading slowly?**
- The Coco-SSD model is ~27MB and loads on first use
- Subsequent uses will be faster due to browser caching
