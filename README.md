# 🎨 Emotions in Transit - IoT Totem

> Multi-screen real-time visualization system for urban environmental data in Barcelona

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)

An interactive IoT data totem combining real-time environmental sensors, public transport tracking, and generative art to visualize the emotional climate of Barcelona's urban transit system.

---

## 📺 System Architecture

The totem uses **three synchronized displays** showing complementary data streams:

```
┌─────────────────────────────────────┐
│  SCREEN 1 (Top - 7" Aurevita)     │
│  🌤️ WEATHER DASHBOARD              │
│  Real-time Barcelona climate       │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│  SCREEN 2 (Center - 24" Dell)     │
│  🚇 TMB TRANSIT LIVE               │
│  Metro • Bus • Bicing tracking     │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│  SCREEN 3 (Bottom - 15.6" Vertical)│
│  📊 SMART CITIZEN + MATRIX         │
│  Environmental sensors + Terminal  │
└─────────────────────────────────────┘
```

---

## ✨ Features

### Screen 1: Weather Dashboard (7")
- 🌡️ Real-time temperature, humidity, pressure
- 💨 Wind speed and direction
- 🌤️ Weather conditions with icons
- Updates every **10 minutes**

### Screen 2: TMB Transit Live (24")
- 🚇 **8 metro lines** (L1-L5, L9-L11) with official TMB colors
- 🚌 **Live bus tracking** with animated routes
- 🚲 **Bicing stations** with real-time availability
- ⚠️ **Incident alerts** and service disruptions
- 🎨 Interactive animations and glowing effects
- Updates every **30 seconds**

### Screen 3: Smart Citizen + Matrix Terminal (15.6" Vertical)
- 📊 **4 environmental sensors**:
  - 🔊 Ambient noise (dBA)
  - 🌡️ Temperature (°C)
  - 💨 PM2.5 particles (µg/m³)
  - 💡 Light intensity (lux)
- 💻 **Matrix-style terminal** with scrolling data
- 🟢 Cyberpunk green phosphor effect
- 🔄 Mixed TMB + sensor data streams
- Updates every **30 seconds**

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript ES6+
- **Visualization**: p5.js (generative art)
- **Typography**: Inter (Google Fonts)
- **APIs**: 
  - OpenWeatherMap
  - TMB Open Data
  - Smart Citizen Kit
- **Control**: Python 3
- **Hardware**: MacBook Pro, UGREEN Revodok Pro 209

---

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Modern web browser (Chrome/Safari recommended)
- Internet connection

### Installation

```bash
# Clone the repository
git clone https://github.com/Raquel-bena/emotions-in-transit-totem.git
cd emotions-in-transit-totem

# Launch the totem
python3 launch_totem.py
```

The script will:
1. ✅ Verify all HTML files exist
2. ✅ Open 3 browser windows (one per screen)
3. ✅ Display positioning instructions

### Manual Launch

```bash
# Open each screen individually
open pantalla1-clima.html
open pantalla2-tmb-transit.html
open pantalla3-smart-citizen.html
```

Then:
1. Drag each window to its designated screen
2. Press **F11** for fullscreen mode
3. Let the visualizations run

---

## 🔌 API Configuration

All API credentials are pre-configured in the code:

### OpenWeatherMap (Weather)
```javascript
API_KEY: '2a36e28d26f35bd287084d12d7492576'
CITY_ID: '3128760' // Barcelona
```

### TMB Barcelona (Transit)
```javascript
APP_ID: 'c6f33d0c'
APP_KEY: 'e3fb4615a39da174072051f5b2ccc5b3'
```

### Smart Citizen Kit (Sensors)
```javascript
DEVICE_ID: '9657'
LOCATION: 'Fabra i Puig – Meridiana'
```

---

## 📁 Project Structure

```
emotions-in-transit-totem/
├── pantalla1-clima.html          # Weather display (7")
├── pantalla2-tmb-transit.html    # TMB transit (24")
├── pantalla3-smart-citizen.html  # Smart Citizen + Matrix (15.6")
├── launch_totem.py               # Python launcher script
├── README.md                     # This file
└── .gitignore                    # Git ignore rules
```

---

## 🎨 Design Principles

### Color Palette
- **Primary**: `#E3000F` (TMB Red)
- **Secondary**: `#0E4C9A` (TMB Blue)
- **Metro Lines**: Official TMB corporate colors
- **Matrix Effect**: `#00FF64` (Phosphor Green)
- **Background**: `#000000` (Pure Black)

### Typography
- **Primary Font**: Inter (Google Fonts)
- **Weights**: 300, 400, 500, 600, 700, 800, 900
- **Terminal**: Monospace (Matrix effect only)

### Animations
- Smooth transitions (0.3s ease)
- 60 FPS performance target
- GPU-accelerated effects
- Responsive to sensor data

---

## 📊 Data Sources

### Smart Citizen Kit #9657
- **Location**: Third floor balcony, Fabra i Puig – Meridiana
- **Sensors**: Noise, Temperature, PM2.5, Light, Humidity
- **Owner**: menyscotxes
- **Tags**: Barcelona, BarcelonaNoise, Outside
- **API**: https://api.smartcitizen.me/v0/devices/9657

### TMB Open Data
- **Service**: Barcelona Public Transport
- **Coverage**: Metro, Bus, Bicing
- **Real-time**: Train positions, ETAs, incidents
- **API**: https://api.tmb.cat/v1/

### OpenWeatherMap
- **Location**: Barcelona, Catalonia
- **Data**: Temperature, humidity, pressure, wind, conditions
- **Update**: Every 10 minutes
- **API**: https://api.openweathermap.org/

---

## 🎓 Academic Context

This project is part of the **Master's Thesis** (TFM):

**Title**: *Emotions (in) Transit*  
**Focus**: Analysis of Barcelona's urban environmental climate through data visualization and generative art  
**Approach**: Combining real-time environmental data, public transit patterns, and emotional interpretation through ambient data rather than biometric surveillance  
**Author**: Raquel  
**Date**: January 2026

---

## 📝 License

MIT License

---

## 📧 Contact

**Raquel** - [@Raquel-bena](https://github.com/Raquel-bena)

**Project Link**: [https://github.com/Raquel-bena/emotions-in-transit-totem](https://github.com/Raquel-bena/emotions-in-transit-totem)

---

<p align="center">Made with 💚 for Barcelona's urban transit ecosystem</p>
<p align="center">🚇 🚲 🌡️ 💨 🎨</p>
