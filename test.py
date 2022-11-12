import asyncio
from whatnots.whatnot import Whatnot

async def main():
    async with Whatnot() as whatnot:
        await whatnot.login("dineshtalwadker", "omshanti2005")

        # Get the whatnot account
        whatnot_user = await whatnot.get_user("dineshtalwadker")
        # OR await whatnot.get_user_by_id("21123")

        lives = await whatnot.get_user_lives(whatnot_user.id)

        # Print out all of the lives
        for live in lives:
            print(live.title)


asyncio.run(main())