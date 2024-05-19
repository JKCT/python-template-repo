"Test module main function."
import pytest

from $$REPO$$.__main__ import main


@pytest.mark.asyncio
class TestMain:
    "Test module main function."

    async def test_main(self) -> None:
        """
        Test main function.
        Should return exit code 0 for success.
        """
        assert await main() == 0
