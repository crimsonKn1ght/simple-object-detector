# Real-Time Object Detection

A web-based real-time object detection application utilizing YOLO model for rock-paper-scissor detection. The trained weights are present as the `game_weights.pt` file.

A standalone version is a genreal purpose real-time detector written with TensorFlow.js and the Coco-SSD model. Detect objects through your webcam directly in the browser with no server required.


## Demo

As for the rock-paper-scissors detector, install the requirements with:
```bash
pip install -r requirements.txt
```

Then run the `live-time-detector.py` normally:
```bash
python live-time-detector.py
```

[Make sure the env paths are set appropriately, which goes without saying.]

As for the standalone general purpose detector, just paste the open and run it on a modern browser as usual.

## Supported Objects

The Coco-SSD model can detect 80 different object classes including:
- People and body parts
- Animals (cats, dogs, birds, etc.)
- Vehicles (cars, bikes, trucks, etc.)
- Household items (chairs, tables, TVs, etc.)
- Food items (pizza, banana, wine glass, etc.)
- And many more!

The other one is self-explanatory, I guess.

## Privacy

- All processing happens locally in your browser
- No data is sent to external servers
- Camera feed is not recorded or stored

## Technical Details

**Rock-Paper-Scissors**
- **Model**: **YOLO11n** (You Only Look Once v11 - nano variant)
- **Framework**: **Ultralytics YOLO** (PyTorch backend)
- **Source**: **Custom-trained weights**
- Captures frames from webcam using **OpenCV**


**Standalone General Model**
- **Model**: Coco-SSD (Common Objects in Context - Single Shot MultiBox Detector)
- **Framework**: TensorFlow.js
- **Styling**: Tailwind CSS
- **Performance**: Optimized for real-time detection with requestAnimationFrame

<!-- ## File Structure

```
├── simple-detector.html          # Main application file
├── README.md                     # This file
└── LICENSE
``` -->

## Dataset

**Dataset:** Rock-Paper-Scissors-SXSW  
**Publisher:** Roboflow (via Universe)  
**URL:** https://universe.roboflow.com/roboflow-58fyf/rock-paper-scissors-sxsw/dataset/14  
**Accessed:** [10-08-2025]


## Contributing

Feel free to fork this project and submit pull requests for improvements.

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
- It might take a while to load the model (usually <30 secs), please be patient.
