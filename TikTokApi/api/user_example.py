# from TikTokApi import TikTokApi
from ..tiktok import TikTokApi
import asyncio
import os
import sys

ms_token = os.environ.get(
    "ms_token", None
)  # set your own ms_token, think it might need to have visited a profile

arguments = sys.argv[1:]
user_name = arguments[0]

async def user_example():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)
        print(user_name)
        user = api.user(user_name)
        user_data = await user.info()
        total_num_videos = 0
        async for video in user.videos(count=4):
            print(f"https://www.tiktok.com/@{user_name}/video/{video.id}")
            play_count = video.stats.get('playCount')
            print(play_count)
            total_num_videos += 1

        print(f"total_num_videos = {total_num_videos}")


if __name__ == "__main__":
    asyncio.run(user_example())
