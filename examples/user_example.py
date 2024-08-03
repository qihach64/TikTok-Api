from TikTokApi import TikTokApi
import asyncio
import os
import sys

# ms_token = os.environ.get(
#     "ms_token", 'None'
# )  # set your own ms_token, think it might need to have visited a profile
ms_token = "X050LW9xSEx6d0fiJGfE0lV8fsHYBMZM6W5qv2qSEatSs3W-Z7YkOTLS3kEJaA8ckiYMkUF5wG9Wsj5tFI66ZrB3E7Z-t1s6J43QvP3SKShpiQFclCOElmrjuB13ucpyHTLfBnWdokqN"

arguments = sys.argv[1:]
user_name = arguments[0]
max_video_cnt = int(arguments[1]) if len(arguments) > 1 else 10000

async def user_example():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)
        user = api.user(username=user_name)
        videos = []
        async for vid in user.videos(count=max_video_cnt):
            # url = f"https://www.tiktok.com/@{user_name}/video/{vid.id}"
            # video_info = await api.video(url=url).info()
            # duration = int(video_info.get("video").get("duration"))
            play_count = vid.stats.get('playCount')
            videos.append((vid.id, play_count))
            # videos.append((vid.id, play_count, duration))
        videos = sorted(videos, key=lambda x: x[1], reverse=True)
        urls = [ f"https://www.tiktok.com/@{user_name}/video/{vc[0]}" for vc in videos]
        # urls_60s = [ f"https://www.tiktok.com/@{user_name}/video/{vc[0]}" for vc in videos if vc[2] > 60]
        all_file = f"{user_name}.txt"
        # files_60s = f"{user_name}_>60s.txt"
        print(f"💪 写入完毕 保存结果到 {all_file}")
        write_urls_to_file(urls, all_file)
        # print(f"💪 写入完毕 保存结果到 {files_60s}")
        # write_urls_to_file(urls_60s, files_60s)

def write_urls_to_file(urls, file_name, batch_size=20):
    # Calculate the number of batches
    num_batches = len(urls) // batch_size + (1 if len(urls) % batch_size > 0 else 0)
    
    with open(file_name, 'w+') as file:
        for i in range(num_batches):
            # Extract the current batch of URLs
            start_index = i * batch_size
            end_index = min((i + 1) * batch_size, len(urls))
            batch_urls = urls[start_index:end_index]
            # Open a file for the current batch and write the URLs
            for url in batch_urls:
                file.write(url + '\n')
            file.write('\n')

if __name__ == "__main__":
    asyncio.run(user_example())
