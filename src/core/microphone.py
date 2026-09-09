"""Microphone Module.

Handles microphone array input and beamforming.
"""

import logging
from typing import Optional

logger = logging.getLogger(__name__)


class Microphone:
    """Microphone array handler for voice capture."""

    def __init__(self, config: dict):
        """Initialize the microphone array.

        Args:
            config: Dictionary containing microphone configuration.
        """
        self.config = config
        self.num_mics = config.get("num_mics", 4)
        self.array_geometry = config.get("array_geometry", "circular")
        self.sample_rate = config.get("sample_rate", 48000)
        self.beamforming_enabled = config.get("beamforming", True)
        self.is_listening = False

        logger.info(f"Microphone initialized: {self.num_mics} mics, "
                    f"{self.array_geometry} array")

    def capture(self, duration: float = 1.0) -> bytes:
        """Capture audio from microphone array.

        Args:
            duration: Duration in seconds to capture.

        Returns:
            Raw audio bytes.
        """
        logger.info(f"Capturing audio for {duration}s")
        self.is_listening = True
        # TODO: Implement microphone capture
        self.is_listening = False
        return b""

    def enable_beamforming(self, enable: bool = True) -> None:
        """Enable or disable beamforming.

        Args:
            enable: True to enable beamforming, False to disable.
        """
        self.beamforming_enabled = enable
        logger.info(f"Beamforming {'enabled' if enable else 'disabled'}")

    def get_direction(self) -> Optional[str]:
        """Get the current beamforming direction.

        Returns:
            Direction string or None if not enabled.
        """
        if not self.beamforming_enabled:
            return None
        # TODO: Implement direction detection
        return "front"

    def get_status(self) -> dict:
        """Get current microphone status.

        Returns:
            Dictionary containing status information.
        """
        return {
            "is_listening": self.is_listening,
            "num_mics": self.num_mics,
            "array_geometry": self.array_geometry,
            "beamforming_enabled": self.beamforming_enabled,
        }
