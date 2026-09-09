# Building Guide

## Prerequisites

- Python 3.11+
- Git
- Virtual environment tool (venv, poetry, or pipenv)
- Home Assistant (optional, for local control)

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/mshelby/Electronic-Bible.git
cd Electronic-Bible
```

### 2. Set Up Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure

```bash
cp config/example.yaml config/config.yaml
# Edit config/config.yaml with your settings
```

### 5. Run

```bash
python src/main.py
```

## Development Setup

### Install Development Dependencies

```bash
pip install -r requirements-dev.txt
```

### Run Tests

```bash
pytest tests/
```

### Lint and Format

```bash
black src/
flake8 src/
mypy src/
```

## Hardware Assembly

### Components Required

- Main board (ARM Cortex-A55)
- Microphone array (4-mic circular)
- Speaker driver (3" full-range)
- Tweeter (1" silk dome)
- Amplifier (Class D)
- DAC (24-bit/96kHz)
- Battery (5000mAh Li-Po)
- USB-C PD charging module

### Assembly Steps

1. **Mount Main Board**: Secure to chassis with M3 screws
2. **Install Microphone Array**: Attach to top panel with adhesive
3. **Connect Speaker Driver**: Wire to amplifier output
4. **Install Tweeter**: Mount to top module with screws
5. **Connect Amplifier**: Wire to DAC and speaker outputs
6. **Install Battery**: Secure to base with Velcro
7. **Connect Charging Module**: Wire to battery and main board
8. **Final Assembly**: Close chassis with magnetic closure

### Wiring Diagram

```
[Main Board]
    │
    ├──→ [Amplifier] → [Speaker Driver]
    │
    ├──→ [DAC] → [Amplifier]
    │
    ├──→ [Microphone Array]
    │
    ├──→ [USB-C PD Module] → [Battery]
    │
    └──→ [Touch Panel]
```

## Testing

### Audio Tests

```bash
python tests/test_audio.py
```

### Database Tests

```bash
python tests/test_database.py
```

### Integration Tests

```bash
python tests/test_integration.py
```

## Troubleshooting

### Common Issues

1. **Audio Not Playing**
   - Check speaker connections
   - Verify audio output configuration
   - Test with `python -m src.audio_test`

2. **Database Not Found**
   - Ensure database path is correct in config
   - Run `python src/init_db.py` to create database

3. **Home Assistant Not Connecting**
   - Verify network connectivity
   - Check Home Assistant API configuration
   - Ensure local network is properly configured

## Deployment

### Production Build

```bash
python scripts/build.py --release
```

### Docker Deployment (Optional)

```bash
docker build -t electronic-bible .
docker run -d --name electronic-bible electronic-bible
```

## Resources

- [Project Goals](Project_Goals.md)
- [Design Decisions](Design_Decisions.md)
- [Hardware Specifications](Hardware_Specifications.md)
- [Software Architecture](Software_Architecture.md)
