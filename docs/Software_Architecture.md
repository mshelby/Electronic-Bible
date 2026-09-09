# Software Architecture

## Overview

Electronic Bible is built on a layered architecture designed for modularity, scalability, and offline-first operation.

## Architecture Layers

### 1. Presentation Layer
- **UI Framework**: Custom minimal interface (Qt or similar)
- **Rendering Engine**: Text rendering with customizable fonts
- **Audio Output**: Real-time audio processing pipeline

### 2. Application Layer
- **Core Logic**: Business logic and data management
- **Audio Engine**: Text-to-speech synthesis and playback
- **Database Manager**: Local SQLite database for text library
- **Configuration Manager**: YAML/JSON configuration handling

### 3. Integration Layer
- **Home Assistant API**: Local control and automation
- **Music Assistant API**: Multi-room audio support
- **Local Network Discovery**: mDNS/Bonjour for device discovery

### 4. Hardware Abstraction Layer
- **Audio I/O**: Microphone capture and speaker output
- **Sensor Interface**: Touch, proximity, and presence sensors
- **Power Management**: Battery monitoring and charging control

## Component Diagram

```
┌─────────────────────────────────────────┐
│           Presentation Layer            │
│  ┌──────────┐  ┌──────────┐  ┌───────┐ │
│  │   UI     │  │  Audio   │  │ Touch │ │
│  │  Engine  │  │  Output  │  │ Panel │ │
│  └──────────┘  └──────────┘  └───────┘ │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│           Application Layer             │
│  ┌──────────┐  ┌──────────┐  ┌───────┐ │
│  │  Core    │  │  Audio   │  │Database│ │
│  │  Logic   │  │  Engine  │  │Manager │ │
│  └──────────┘  └──────────┘  └───────┘ │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│           Integration Layer             │
│  ┌──────────┐  ┌──────────┐  ┌───────┐ │
│  │ Home     │  │ Music    │  │ Local │ │
│  │Assistant │  │Assistant │  │Network│ │
│  └──────────┘  └──────────┘  └───────┘ │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│        Hardware Abstraction Layer       │
│  ┌──────────┐  ┌──────────┐  ┌───────┐ │
│  │ Audio    │  │ Sensors  │  │Power  │ │
│  │  I/O     │  │Interface │  │Mgmt   │ │
│  └──────────┘  └──────────┘  └───────┘ │
└─────────────────────────────────────────┘
```

## Data Flow

1. **User Input** → UI Layer → Application Layer
2. **Text Request** → Database Manager → Text Library
3. **Audio Synthesis** → Audio Engine → Speaker Output
4. **Local Control** → Home Assistant API → Integration Layer
5. **Sensor Data** → Hardware Abstraction → Application Layer

## Configuration

All configuration is handled via YAML files:

```yaml
# config/audio.yaml
audio:
  sample_rate: 48000
  bit_depth: 24
  channels: 2
  output_volume: 75

# config/database.yaml
database:
  path: /data/electronic_bible.db
  backup_interval: 3600
  encryption: true
```

## Event-Driven Communication

Components communicate via an event bus:

- `audio:play` → Triggers audio playback
- `text:change` → Updates displayed text
- `sensor:touch` → Handles touch input
- `network:discover` → Discovers local devices

## Security

- All data encrypted at rest (AES-256)
- Local network only (no external API calls)
- No telemetry or data collection
- Encrypted database sync
```