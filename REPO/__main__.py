"Module main."
import asyncio
import logging


async def main() -> int:
    "Main function."
    logger = logging.getLogger(__name__)
    logger.info("Hello world from $$REPO$$.")
    return 0


if __name__ == "__main__":
    asyncio.run(main())
