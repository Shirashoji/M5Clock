# M5Stack Analog Clock

This project displays an analog clock and the current date on an M5Stack device. It's written in MicroPython and is designed to be a simple and elegant timepiece.

![M5Clock](https://user-images.githubusercontent.com/46389417/184781783-b0686b98-c360-4c8b-a708-02de42f82d81.jpeg)

## Features

*   **Analog Clock Display:** Shows the current time with hour and minute hands.
*   **Date Display:** Shows the current month and day.
*   **Automatic Time Sync:** Syncs with an NTP server to ensure the time is always accurate.

## Requirements

*   **Hardware:**
    *   M5Stack Core
*   **Software:**
    *   UIFlow (or a MicroPython environment for M5Stack)

## Usage

1.  **Connect to Wi-Fi:** The program will automatically connect to the Wi-Fi network configured in your M5Stack's settings.
2.  **Run the Code:** Flash the `main.py` file to your M5Stack device.
3.  **Enjoy:** The clock will automatically sync its time and display the current time and date.
