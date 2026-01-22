#!/usr/bin/env python3
"""
EMOTIONS IN TRANSIT - TOTEM CONTROL
Multi-screen IoT Dashboard System

Hardware Setup:
- Screen 1 (7" Aurevita): Weather Display
- Screen 2 (24" Dell): TMB Transit Live
- Screen 3 (15.6" UFYQL Vertical): Smart Citizen Data + Generative Art

Author: Raquel (Emotions in Transit TFM)
Date: January 2026
"""

import time
import webbrowser
import os
import sys
from pathlib import Path

# Configuration
SCREENS = {
    'weather': {
        'file': 'pantalla1-clima.html',
        'name': 'Weather Dashboard',
        'size': '7" Aurevita',
        'position': 'top'
    },
    'transit': {
        'file': 'pantalla2-tmb-transit.html',
        'name': 'TMB Transit Live',
        'size': '24" Dell',
        'position': 'center'
    },
    'sensors': {
        'file': 'pantalla3-smart-citizen.html',
        'name': 'Smart Citizen + Generative Art',
        'size': '15.6" UFYQL Vertical',
        'position': 'bottom'
    }
}

def print_banner():
    """Display startup banner"""
    print("\n" + "="*60)
    print("   EMOTIONS IN TRANSIT - TOTEM DATA")
    print("   Sistema de Visualización IoT Multi-Pantalla")
    print("="*60)
    print("\n📺 Hardware Configuration:")
    for key, screen in SCREENS.items():
        print(f"   {screen['position'].upper():8} → {screen['name']}")
        print(f"            {screen['size']} - {screen['file']}")
    print("\n" + "="*60 + "\n")

def check_files():
    """Verify all HTML files exist"""
    print("🔍 Verificando archivos...")
    all_exist = True
    
    for key, screen in SCREENS.items():
        file_path = Path(screen['file'])
        if file_path.exists():
            print(f"   ✓ {screen['file']}")
        else:
            print(f"   ✗ {screen['file']} - NO ENCONTRADO")
            all_exist = False
    
    print()
    return all_exist

def launch_screen(screen_key):
    """Launch a single screen in browser"""
    screen = SCREENS[screen_key]
    file_path = Path(screen['file']).absolute()
    url = f"file://{file_path}"
    
    print(f"🚀 Lanzando: {screen['name']}")
    print(f"   Archivo: {screen['file']}")
    print(f"   URL: {url}\n")
    
    try:
        webbrowser.open(url, new=2)  # Open in new tab/window
        return True
    except Exception as e:
        print(f"   ❌ Error: {e}\n")
        return False

def launch_all_screens():
    """Launch all screens sequentially"""
    print("🚀 Iniciando todas las pantallas...\n")
    
    success_count = 0
    for key in SCREENS.keys():
        if launch_screen(key):
            success_count += 1
            time.sleep(2)  # Wait 2 seconds between launches
    
    print("="*60)
    print(f"✓ {success_count}/{len(SCREENS)} pantallas iniciadas correctamente")
    print("="*60 + "\n")
    
    return success_count == len(SCREENS)

def main():
    """Main control function"""
    print_banner()
    
    # Check files
    if not check_files():
        print("❌ ERROR: Algunos archivos no se encontraron.")
        print("   Asegúrate de que todos los archivos HTML están en el directorio actual.")
        sys.exit(1)
    
    print("✓ Todos los archivos encontrados\n")
    
    # Launch screens
    if launch_all_screens():
        print("\n💡 INSTRUCCIONES:")
        print("   1. Posiciona cada ventana del navegador en su pantalla correspondiente")
        print("   2. Presiona F11 en cada ventana para modo pantalla completa")
        print("   3. Las visualizaciones se actualizarán automáticamente")
        print("\n📊 APIS CONFIGURADAS:")
        print("   • OpenWeatherMap: Barcelona (ID: 3128760)")
        print("   • TMB Transit: Barcelona Metro/Bus/Bicing")
        print("   • Smart Citizen Kit: Device 9657 (Fabra i Puig)")
        print("\n⚡ El tótem está ONLINE y funcionando")
        print("   Presiona CTRL+C para detener\n")
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n\n👋 Cerrando Emotions in Transit Totem...")
            print("   Las ventanas del navegador permanecerán abiertas\n")
    else:
        print("❌ Hubo errores al iniciar las pantallas")
        sys.exit(1)

if __name__ == "__main__":
    main()
