import aiohttp
import asyncio

SITES = {
    "telegram": "https://t.me/{}",
    "instagram": "https://instagram.com/{}",
    "tiktok": "https://tiktok.com/@{}",
    "github": "https://github.com/{}",
    "reddit": "https://reddit.com/user/{}",
    "twitter": "https://twitter.com/{}"
}

async def check(session, name, url):
    try:
        async with session.get(url, timeout=5) as r:
            return f"{name}: found" if r.status == 200 else f"{name}: not found"
    except:
        return f"{name}: error"

async def username_scan(username):
    async with aiohttp.ClientSession() as session:
        tasks = [
            check(session, k, v.format(username))
            for k, v in SITES.items()
        ]
        res = await asyncio.gather(*tasks)

    score = sum("found" in r for r in res)

    return "username report\n\n" + "\n".join(res) + f"\nscore: {score}/{len(SITES)}"
