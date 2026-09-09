# Design Decisions

## Quiet Quality Philosophy

- **Minimalism**: No visible fasteners, clean lines, intentional shadow gaps
- **Material Choice**: Matte PETG for tactile premium feel
- **Acoustic Focus**: Dual drivers, optimized internal volume (~3.0L)
- **Modularity**: Serviceable design for maintenance and upgrades

## Tech Stack

- Python 3.11+ for core logic
- Home Assistant integration for local control
- FFmpeg for audio encoding/decoding
- SQLite for local database management

## Architecture

- Layered design: Audio Engine → Microphone → Speaker
- Event-driven communication between components
- Configurable via YAML/JSON for easy customization

## Key Decisions

- **Offline-first**: All data stored locally, no cloud dependency
- **Privacy-focused**: No telemetry, no external API calls
- **Modular construction**: Easy to upgrade individual components
- **Clean interface**: Minimalist UI inspired by classic design
- **Text-to-speech**: Natural voice synthesis for accessibility

## Color, Texture & Surface Finish

### Barrel Main
- **Color:** Concrete Gray Matte  
- **Approximate Hex:** `#DEDEDE` (warm light gray / concrete)
- **Why chosen:** Provides a soft, neutral, architectural base that feels substantial and timeless. Matte finish reduces glare, hides minor layer lines, and supports the quiet luxury aesthetic. Complements both dark modules and colored trim rings without competing with them.

### Speaker Trim Rings (Front & Rear) + Upper / Lower Trim Rings
- **Color:** Matte Navy  
- **Approximate Hex:** `#1E3A5F` (deep navy)
- **Why chosen:** Creates elegant contrast against the light gray barrel while remaining refined and classic. Navy reads as "quiet luxury" rather than bright or trendy. Separate printed rings allow easy color experimentation (wood-look, charcoal, etc.) without reprinting the entire barrel.

### Modules (Top & Bottom Caps)
- **Color:** Concrete Gray Matte (same as Barrel Main)
- **Approximate Hex:** `#A8A29E` (warm light gray / concrete)
- **Why chosen:** Matches barrel main for a clean aesthetic while allowing individual trim lines to appear more prominent.

### Diffuser Ring
- Translucent / Clear PETG (or light smoke gray) so LEDs glow cleanly through without harsh hotspots.

### Surface Finish Notes
- Primary finish: Matte PETG throughout for a soft, high-end tactile feel.
- Optional: Orca Slicer "Fuzzy Skin" on the barrel exterior (still under evaluation — test on a sample first).
- No high-gloss surfaces preferred — they fight the quiet, refined character of the design.

All decisions prioritize the balance of premium appearance, printability, and sound quality.
```

<parameter=path>
docs/Design_Decisions.md